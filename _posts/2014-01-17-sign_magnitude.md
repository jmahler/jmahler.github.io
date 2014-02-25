---
layout: post
title: "Magnitude of Signed/Unsigned 16-bit"
date: 2014-01-17 1:00
category: Programming
tags: [Programming, Numbers, Interview, Electrical Engineering]
---

# Question

Plot the magnitude of both a signed and unsigned 16-bit number.

# Answer

Some may be able to remember the ranges for signed and unsigned easily.
If I can't remember I will try a trivial example to jog my memory.
Once the solution is found with this example it can be easily
applied to the more elaborate case (16-bit).

Instead of 16-bits, try 2-bits.

Recall how to convert 2s compliment numbers.
Invert the bits (not) and add one.

    10 (2s) -> 01 + 1 = 10 (-2)

Then create a table of all the cases.

      2-bit
    --------
    00  0  0
    01  1  1
    10  2 -2
    11  3 -1

Now the equations for the magnitude can be easily found.

    unsigned: 0           to  (2^b - 1)
      signed: -(2^(b - 1) to  (2^(b-1) - 1)

Then use these equations for the 16-bit case.

    unsigned: 0            to  (2^16 - 1)
      signed: -(2^(16 - 1) to  (2^(16 - 1) - 1)
              -2^15        to  2^15 - 1

And finally, produce a plot:

![plot16]({{site.url}}/images/plot16.svg)

# Background

This question was given during an interview on 1/17/2014 for
a firmware test engineer position.
