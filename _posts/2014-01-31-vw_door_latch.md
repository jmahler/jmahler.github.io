---
layout: post
title: "Failure Analysis of a Volkswagen Mk4 Door Latch"
date: 2014-01-31 1:00
category: Electrical Engineering
tags: Electrical Engineering, Automotive
---

## Affected Vehicles

<table>
<tr><td>year</td><td>1999 - 2005</td></tr>
<tr><td>make</td><td>Volkswagen</td></tr>
<tr><td>model</td><td>Golf, Jetta, New Beetle</td></tr>
<tr><td valign="top">part number</td><td>3B1 837 015 J (left)<br>
						Other numbers possible.</td></tr>
</table>

## Symptoms

Opening and closing front door does not produce the normal events.
Dome light and puddle light may be always off, always on, or work
sporadically.
The door chime for the driver side does not sound when driver door
is opened or it chimes continuously.
The alarm behaves incorrectly, locking the car, or sounding when
door is opened.

## Background and Operation

![door_latch]({{site.url}}/images/door_latch/door_latch-x300.jpg)

The door latch (F220) consists of several mechanical switches as
shown in the wiring diagram below.
Notice that it is composed entirely of passive components:
several switches and one motor.
The switch on pin 8 near 304 is the door open/closed detection switch.
There is a ground connection at 206 which serves all the switches in the latch.

![Door Latch Schematic]({{site.url}}/images/door_latch/door_latch_schematic.png)

The table below shows the expected operation at the pins of the 8-pin
connector on the door latch.  Not all operations have been determined.

<table>
<tr><th>pin</th><th>operation</th></tr>
<tr><td valign="top">1 - 2</td><td>motor<br>
						10 ohm resistance<br>
						0.5 sec 10 volt pulse in one direction.<br>
						Exact operation unknown.</td></tr>
<tr><td>4 - 7</td><td>normally open, key clockwise, switch closed</td></tr>
<tr><td>6 - 7</td><td>normally open, key counter-clockwise, switch closed</td></tr>
<tr><td>3 - 7</td><td>unknown</td></tr>
<tr><td>5 - 7</td><td>unknown</td></tr>
<tr><td valign="top">7 - 8</td><td>door open, switch closed<br>
						door closed, switch open</td></tr>
</table>

The switch across pins 7-8 which detects the door open/close position
is the one that fails.
Interestingly, as shown below, it is the only switch that is exposed to the outside.
All the other switches are encased inside a moisture resistant enclosure.

![door_latch_switch]({{site.url}}/images/door_latch/door_latch_switch-x300.jpg)

## Diagnosis

First it should be verified that none of the door open/close
events produce the expected result.
The dome light and puddle light never go on or always stay on.
If it is a driver side door latch, the door chime never comes on or
always stays on.
Keep it mind that it is possible that the dome light, puddle light, and
door chime are all faulty.
Incorrectly diagnosing these faults as a door latch should be avoided.

Once it has been determined that the door latch switch is most likely at fault
the next step is to disassemble the door to gain access to the latch.
As a final check the continuity between pins 7-8 on the door latch
can be checked to verify the failure.

## Repair

To fix this problem, the door latch should be replaced.

It may be possible to repair the latch by replacing the contact switch
and/or re-flowing the solder joints inside the enclosure.
But this option has not been explored.
