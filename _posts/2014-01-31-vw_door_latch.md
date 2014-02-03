---
layout: post
title: "Failure Analysis of VW Mk4 Door Latch"
date: 2014-01-31 1:00
category: Electrical Engineering
tags: Electrical Engineering, Automotive
---

The front door latch found on 1999 to 2005 (Mk4) Volkswagen Jettas, Golfs
and Beetles is a common failure item.
Typically, when they fail, they behave as if the door is always
open or always closed.
And in some cases this failure is sporadic.

<table>
<tr><td>year</td><td>1999 - 2005</td></tr>
<tr><td>make</td><td>Volkswagen</td></tr>
<tr><td>model</td><td>Golf, Jetta</td></tr>
<tr><td valign="top">part number</td><td>3B1 837 015 J (left)<br>
						Other numbers possible.</td></tr>
</table>

There are several goals of this document:

1.  Determine the root cause of failure.
1.  Describe its operation (electrical switches).
1.  Devise absolutely certain method of diagnosis.


## Operation

Before determining how the door latch has failed it is necessary to
understand its operation.
The wiring diagram related to the door latch, F220, is shown below.
Notice that it appears to be composed entirely of passive components;
switches and one motor.
There is ground connection at 206 which goes through the latch and
out on 304.
There is a push button switch near 304.
There is no indication of which switches correspond to which operation.
And there is no indication of what voltage is present on these wires.
In particular, what voltage is used to drive the motor.

![Door Latch Schematic]({{site.url}}/images/door_latch/door_latch_schematic.png)

## Diagnosis

Typically if the door puddle light is out this is a good indication
that the switch inside that latch that indicates open/closed has failed.
But this is not a foolproof indicator.  What if the bulb has failed?
A good secondary check would be to examine the interior light above
the rear view mirror.  If it reacts normally it is likely the bulb
in the puddle light.  If it does not it may still be a latch.
Another secondary check is to listen for a door chime when they key is
inserted and the door is opened.
Many of these checks can suggest a door latch switch failure but none
of them are definitive.

This document is a work in progress, check back for updates...
