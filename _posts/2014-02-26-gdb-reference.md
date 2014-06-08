---
layout: post
title: "Gdb Refernce"
date: 2014-02-26 1:00
category: Linux
tags: [Linux]
---

## Running GDB

    $ gdb <cmd>

    (gdb) quit

If the program takes arguments specifying them when starting gdb will
not work.  Instead they must be specified when run is called.

    $ gdb <cmd>
    (gdb) run <arg 1> ...
    (gdb) run 1>/dev/null

To run with a ncurses view of the source code.

    $ gdb -tui <cmd>

## Command Reference

    run <argv> ...
    kill

    step                                forward, including functions
    next                                forward, skip functions

    backtrace
    frame <n>

    print <var name>                    print a variable

    break 19                            break at line 19
    break object.c:132                  break at line 132 in object.c

    break LinkedList<int>::remove       break at a pattern
    break Node<int>::Node

    info breakpoints                    list the break points

    clear <location>                    clear all breakpoints
    delete <number>                     delete a breakpoint

    condition 1 item_to_remove==1

    x 0x00101                           examine memory

