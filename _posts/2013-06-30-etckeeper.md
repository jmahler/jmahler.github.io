---
layout: post
title: "Using Git to Manage /etc With Etckeeper"
date: 2013-06-30 12:00
category: Git
tags: [Git, Etckeeper]
author: Jeremiah Mahler
summary: Using Git to Manage /etc With Etckeeper
---

Using [Git][Git] to manage files in `/etc` seems easy
enough.  Just `init` the directory and start making changes.
But there are several problems.  The repo may be modified
by multiple administrators.  Superuser (root) privileges
are necessary to edit the files.  The commit messages
should reflect the actual user, not root.

 [Git]: http://git-scm.com

Another complication involves permissions.  A newly cloned
version of `/etc` should recreate all the original permissions.
Git by itself does not support storage of this metadata.

One program that resolves all these issues is [Etckeeper][Etckeeper].

 [Etckeeper]: https://github.com/joeyh/etckeeper

# Etckeeper Initialization

To initialize the `/etc` directory only takes a few steps.
By default, `etckeeper` will update `/etc` so the `-d` option
is not needed to specify an alternate directory.

The first step is to run `init`.

    $ sudo etckeeper init
    
This will create a `.git`, `.gitignore` and `.etckeeper`.
This is a good time to add additional exclusions to the `.gitignore`
such as `passwd*` and `shadow*`.  Also be sure to remove the
cached add.

	$ sudo git rm --cached shadow*
	$ sudo git rm --cached passwd*

Next `pre-commit` needs to be run so that `.etckeeper` is updated to
reflect the current owners, groups and permissions.

    $ sudo etckeeper pre-commit

And finally commit the changes.

    $ etckeeper commit

Why was `etckeeper commit` used instead of `git commit`?
A commit using Etckeeper determines the proper user name.
Git commit would just save it as root, which isn't very helpful
when trying to figure out who changed what.  Excluding the commit
command, git can be used directly (add, rm, status, log, etc).

# User Commits

Commits in `/etc` can be performed as root but this is not a
very good solution because it obscures which user actually made the
change.  A better solution is to use the `-E` option to `sudo`
which is used to "preserve the user environment" and allow the user
to be identified.

    jeri@hudson:/etc$ sudo -E git commit

# Pushing Remotes

Setting up the remote for `etckeeper` is no different than
for any other Git repo.

    jeri@hudson:/etc$ sudo git remote add origin git@hudson.localdomain:servers/hudson/etc
    jeri@hudson:/etc$ sudo git push -u origin master

There is one caveat, the root account must have a public ssh key setup
in [Gitolite][Gitolite] so that it has access.

 [Gitolite]: https://github.com/sitaramc/gitolite

# Clone/Commit in Alternate Location

Cloning `/etc` is done in the usual Git manner except
for an additional Etckeeper step to set the file ownership and permissions.

    jeri@hudson:~/tmp$ git clone git@hudson.localdomain:servers/hudson/etc
    jeri@hudson:~/tmp$ cd etc/

At this point the checked out files have the user permissions, not those
that were originally in `/etc`.  To apply the permissions it applies
the commands in `.etckeeper`.

    jeri@hudson:~/tmp$ sudo -E etchkeeper init -d .

The `-d` options tells `etckeeper` to use the given directory instead
of `/etc`.

# Upgrade Autocommit

One amazingly useful feature of Etckeeper is that it will
automatically commit the changes in `/etc` on an `apt-get upgrade`.

    root@hudson:/etc# git log
    commit 53ff2f5e36bc93b7b56dd834f83a2d662975303f
    Author: root <root@hudson.localdomain>
    Date:   Wed Jul 3 20:01:17 2013 -0700
    
        committing changes in /etc after apt run
        
        Package changes:
        -accountsservice 0.6.30-2
        +accountsservice 0.6.34-1
        -appstream-index 0.3.1-1
        -apt 0.9.8.2
        +appstream-index 0.3.1-2
        +apt 0.9.9
        -apt-utils 0.9.8.2
        +apt-utils 0.9.9
        -aptdaemon 0.45-2
        -aptdaemon-data 0.45-2
        +aptdaemon 0.45-3
        +aptdaemon-data 0.45-3
        -cdbs 0.4.121
        +cdbs 0.4.122
        -cpp 4:4.8.1-1
        +cpp 4:4.8.1-2
        -cpp-4.8 4.8.1-4
        +cpp-4.8 4.8.1-5
        -debhelper 9.20130626
        +debhelper 9.20130630
    ...
