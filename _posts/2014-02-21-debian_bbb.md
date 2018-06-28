---
layout: post
title: "Debian Install on a Beagle Bone Black"
date: 2014-02-21 1:00
category: Linux
tags: [Linux, Debian]
---

# Introduction

There are many sources of information on howto install
[Debian][deb] on a [Beagle Bone Black][bbb].
This document describes the specific steps that were
used to complete a successful install using only a
serial console (no display).

  [deb]: http://www.debian.org
  [bbb]: http://beagleboard.org/Products/BeagleBone+Black

# Requirements

The following components were used to complete the install.
Other versions may work as well.

<table>
<tr><td>Beagle Bone Black, Rev A5A</td></tr>
<tr><td><a href="http://www.adafruit.com/products/284">FTDI Friend</a></td></tr>
<tr><td>5V power supply</td></tr>
<tr><td>USB Type A to Mini-B cable</td></tr>
<tr><td>8 GB microSD flash card</td></tr>
<tr><td>microSD flash card to usb adapter</td></tr>
</table>

# Boot Image Preparation

The first step is to prepare the boot image on the microSD flash card.
Here a netinstall image created by Robert Nelson will be used.
It includes a script that takes care of all the image preparation and
downloading steps.

    $ git clone git://github.com/RobertCNelson/netinstall.git
    $ cd netinstall/

To prepare the image and write it to the flash card the following command
is run.  Note, here it is assumed that the flash card is located at /dev/sdb.
Also, the *-serial image is chosen because the FTDI Friend serial
interface is being used.

    $ sudo ./mk_mmc.sh --mmc /dev/sdb --dtb am335x-bone-serial --distro wheezy-armhf

If all went will the image should be created and ready to use.
Remove it from the host computer and install it in to the Beagle Bone Black.

# Debian Installation

This installation will be performed using a serial console.
The connection with the FTDI Helper is shown below.

![Config Check]({{ site.url }}/images/debian_bbb/board-50.jpg)

To start the serial console run the screen command.

    $ screen /dev/ttyUSB0 115200 8N1

With the 5V power supply connected the power button can be pressed
to reset the board.  Lots of output should be seen on the console as it
boots up.  The first screen of the install process should be the
language selection screen as shown below.

![Config Check]({{ site.url }}/images/debian_bbb/first_screen-80.png)

From here the usual Debian install steps are performed.
And if all goes well it should reboot in to the new system.
