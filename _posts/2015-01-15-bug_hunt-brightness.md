---
layout: post
title: "Bug Hunt #1: Inconsistent Brightness"
date: 2015-01-10 1:00
category: Linux
tags: [Linux]
---

[1]: https://lkml.org/lkml/2015/1/8/679
[2]: https://lkml.org/lkml/2015/1/9/21
[3]: https://lkml.org/lkml/2015/1/10/189

I encountered some strange behavior on my Lenovo X1 Carbon laptop
running Linux.  Sometimes, after resuming from a suspend, the backlight
brightness would be nearly off instead of at the correct level.
As soon as I pressed a key it would reset to the correct level so this
was not a big deal.

Sometimes I leave the machine idle long enough for the screen to power
off.  Then, instead of waking it up to use it, I just close the lid to
put it to sleep.  It is these times when the problem occurs.  And sure
enough, I can reproduce the problem by running the following commands.

    xset dpms force off
    sleep 1
    sudo systemctl suspend

Now that I can reproduce the problem I need to answer several questions.
Has it worked in the past? And do other machines have this problem?

The machine is currently running kernel 3.18 (linux-next-20150107).
Going back to an old 3.16.3 kernel and the problem is not present.

All other machines that I have available behave as I expect and resume
with the screen on and not nearly off.

Now that I know of a working and non-working kernel version I can
perform a bisect to find the patch which introduced the problem.
Unfortunately, there are almost 40 thousand patches between the working
and non-working kernel versions.  Git bisect would take far too long.
So I perform a manual bisect with linux-next versions.

    20150107 bad
    20141231 bad
    20141210 bad
    20141201 bad
    ???
    20141128 XXX - doesn't boot
    20141001 XXX - has other problems, doesn't suspend/resume

So I reached a bad linux-next version that boots and one that doesn't
boot.  So I continue from the working bad commit and start looking at
interesting commits related to the driver.  In this case the i915 drm
driver is being used so `git log` is used to find interesting commits.

    ~/linux-next$ git log drivers/gpu/drm/

Continuing the manual bisect more bad but functional commits are found.

    305ec7ab bad
    ed3d6cff bad
    f7faa1ef bad
    c549f738 bad
    6a2c4232 bad
    69f627f5 bad
    b7277357 bad
    b2efb3f0 bad
    7963e9db bad
    f68d697e good

Now the problem is confined to a small area with just over one thousand
commits.

    ~/linux-next$ git log f68d697e..7963e9db --pretty=oneline | wc -l
    1077

Proceeding with the git bisect

    ~/linux-next$ git bisect start
    ~/linux-next$ git bisect good f68d697e
    ~/linux-next$ git bisect bad 7963e9db
    ...

the following commit was found to have introduced the problem.

    From 6dda730e55f412a6dfb181cae6784822ba463847 Mon Sep 17 00:00:00 2001
    From: Jani Nikula <jani.nikula@intel.com>
    Date: Tue, 24 Jun 2014 18:27:40 +0300
    Subject: [PATCH] drm/i915: respect the VBT minimum backlight brightness
    
    Historically we've exposed the full backlight PWM duty cycle range to
    the userspace, in the name of "mechanism, not policy". However, it turns
    out there are both panels and board designs where there is a minimum
    duty cycle that is required for proper operation. The minimum duty cycle
    is available in the VBT.
    
    The backlight class sysfs interface does not make any promises to the
    userspace about the physical meaning of the range
    0..max_brightness. Specifically there is no guarantee that 0 means off;
    indeed for acpi_backlight 0 usually is not off, but the minimum
    acceptable value.
    
    Respect the minimum backlight, and expose the range acceptable to the
    hardware as 0..max_brightness to the userspace via the backlight class
    device; 0 means the minimum acceptable enabled value. To switch off the
    backlight, the user must disable the encoder.
    
    As a side effect, make the backlight class device max brightness and
    physical PWM modulation frequency (i.e. max duty cycle)
    independent. This allows a follow-up patch to virtualize the max value
    exposed to the userspace.
    
    Signed-off-by: Jani Nikula <jani.nikula@intel.com>
    Reviewed-by: Jesse Barnes <jbarnes@virtuousgeek.org>
    [danvet: s/BUG_ON/WARN_ON/]
    Signed-off-by: Daniel Vetter <daniel.vetter@ffwll.ch>

Success!  I found the patch which introduced the bug.  Next, I notify all
the authors by sending a email \[[1]\].

The reply I got back was a bit surprising \[[2]\].

    On Fri, 09 Jan 2015, Jeremiah Mahler <jmmahler@gmail.com> wrote:
    > Jani, all,
    >
    > On a Lenovo X1 Carbon if the display is off when suspend is entered
    > it will be off when it is resumed.  A key must be pressed to restore
    > normal brightness.
    
    Please file a bug on [1] and attach dmesg with drm.debug=14 set, from
    boot to reproducing the problem.
    
    Thanks for the report.
    
    BR,
    Jani.

He made no mention of what I had found and it seemed like he could care
less whether this was fixed or not.  He basically said: Thanks noob, why
don't you go file a bug report and maybe we'll look in to it.

Usually when I tell someone that their patch introduced a bug they are
a bit embarrassed and this makes them interested in fixing it.
And since they know their patch better than anyone, they can
usually figure out what is wrong just from my description.

So I had to decide what to do next.  I could file a bug report and cross
my fingers hoping somebody else gets around to fixing it.  I could reply
and say why don't you fix your broken code!.  Or I could fix it myself.
I certainly won't make any new friends with the second option.  The
first option is easy but slow.  The third option is difficult and
requires a lot of work.  I decided to proceed with the third option.

I am not a specialist with display drivers or backlight operation so
I will have to learn how these systems work as a go.

The first step is to look at the patch which introduced the problem and
see if there is anything obvious.  Unfortunately the patch is
substantial in size (160+ lines) and there are not obvious faults.

The patch introduced functions to scale the backlight levels.  There
are both hardware and user levels which are scaled to and from each
other.  Operations to get the minimum brightness from the BIOS were
also introduced.

The next step is to add print statements and see if any of the values
look strange.  Looking at the `scale_hw_to_user()` function, which calls
`scale()`, it looks like they are correctly calculating the backlight levels.

    scale_hw_to_user(0, 4437) => 52
      scale(0, 0, 4437, 52, 4437) => 52

The `scale()` function takes an input value for the input min/max range
and scales it to the output min/max range.

The minimum value of 52 seems strange so I decide to investigate where
it comes from.  It is retrieved as the value 3 from the BIOS and then
scaled to the value 52.

    get_backlight_min_vbt
      scale(3, 0, 255, 0, 4437) => 52

This seems reasonable.  The minimum brightness is simply non-zero.

When the screen is powered off the backlight level is set to the
minimum of 52.

    scale_hw_to_user(0, 4437) => 52
      scale(0, 0, 4437, 52, 4437) => 52

When the machine is resumed the panel is enabled by a call to
`intel_panel_enable_backlight()`.  This function has a check for the case
when the backlight level is set zero in which case it will set the level
to the maximum.  So in cases where it is enabled after the screen was
off the screen will still be turned on.

    drivers/gpu/drm/i915/intel_panel.c
    965         if (panel->backlight.level == 0) {
    966                 panel->backlight.level = panel->backlight.max;
    967                 if (panel->backlight.device)
    968                         panel->backlight.device->props.brightness =
    969                                 scale_hw_to_user(connector,
    970                                                  panel->backlight.level,
    971                                                  panel->backlight.device->props.max_brightness);
    972         }

Checking this behavior found that this case was entered during a resume
on an Acer C720 which uses the same driver.  This case is not entered on
the X1 Carbon.  The Acer C720 also did not exhibit the problem.
Closer examination found that minimum brightness was zero for the Acer
C720.

The root cause of this problem is the check for minimum brightness being
equal to zero when it can be a non-zero value.  Changing the comparison
to check for the minimum value fixes the problem.

    diff --git a/drivers/gpu/drm/i915/intel_panel.c b/drivers/gpu/drm/i915/intel_panel.c
    index 4d63839..4ef4d66 100644
    --- a/drivers/gpu/drm/i915/intel_panel.c
    +++ b/drivers/gpu/drm/i915/intel_panel.c
    @@ -962,7 +962,7 @@ void intel_panel_enable_backlight(struct intel_connector *connector)
     
     	WARN_ON(panel->backlight.max == 0);
     
    -	if (panel->backlight.level == 0) {
    +	if (panel->backlight.level == panel->backlight.min) {
     		panel->backlight.level = panel->backlight.max;
     		if (panel->backlight.device)
     			panel->backlight.device->props.brightness =
    -- 

And finally, I submitted a patch to fix the problem \[[3]\].

# References

  \[1\] [https://lkml.org/lkml/2015/1/8/679][1]

  \[2\] [https://lkml.org/lkml/2015/1/9/21][2]

  \[3\] [https://lkml.org/lkml/2015/1/10/189][3]

