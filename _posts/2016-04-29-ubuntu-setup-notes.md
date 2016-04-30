---
layout: post
title: "Ubuntu Setup Notes"
date: 2016-04-29 1:00
category: Linux
tags: [Linux]
---

The following are my notes for setting up Ubuntu 12.04 LTS
and 14.04 LTS systems.

# Customize The Desktop

Install the extra configuration tools.

    # (Ubuntu 12.04 and 14.04)
    apt-get install \
      compizconfig-settings-manager \
      compiz-pluins

    # (Ubuntu 14.04)
    apt-get install \
      unity-tweak-tool

Add keyboard shortcuts for launching terminals and browsers.
Disable shortcuts which annoying.

    System Settings -> Keyboard
      Shortcuts -> Launchers
        -> Launch help browser -> Disabled
        -> Launch terminal -> Alt+F1
        -> Launch web browser -> Alt+F3
    
    ccsm -> Ubuntu Unity Plugin
      -> General -> Key to show the HUD when tapped -> Disabled
      -> Launcher -> Key to give keyboard-focus to the Launcher -> Disabled

Enable workspaces and make them a horizontal row of four instead of a
grid.

    System Settings -> Appearance -> Behavior
      -> Enable workspaces
    
    unity-tweak-tool -> Window Manager -> Workspace Settings
      -> Horizontal workspace -> 4
      -> Vertical workspace -> 1

# Install My Favorite Packages

    apt-get install \
      tmux \
      vim-gtk

