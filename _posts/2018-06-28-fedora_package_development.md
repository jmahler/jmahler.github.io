---
layout: post
title: "Fedora Package Development Notes"
date: 2018-06-28 1:00
category: Linux
tags: [Linux, Packaging]
---

[1]: https://fedoraproject.org/wiki/How_to_create_a_GNU_Hello_RPM_package
[2]: https://developer.fedoraproject.org/tools/docker/docker-images.html
[3]: https://fedoraproject.org/wiki/Using_the_Koji_build_system
[4]: https://koji.fedoraproject.org/koji/
[5]: https://fedoraproject.org/wiki/Reproducible_Builds
[6]: https://tests.reproducible-builds.org/rpms/fedora-23.html
[7]: https://tests.reproducible-builds.org/rpms/fedora-23/x86_64/fail2ban/fail2ban-0.9.3-1.fc23.noarch.rpm.html
[8]: https://fedoraproject.org/wiki/Join_the_package_collection_maintainers
[9]: http://ftp.rpm.org/max-rpm/
[10]: https://fedoraproject.org/wiki/Packaging:Scriptlets
[11]: https://discussion.fedoraproject.org
[12]: https://github.com/rpm-software-management/dnf
[13]: https://github.com/mmornati/docker-mock-rpmbuilder
[14]: https://alt.fedoraproject.org/cloud/
[15]: https://fedoraproject.org/wiki/Join_the_package_collection_maintainers#One-off_contributions
[16]: https://bugzilla.redhat.com/buglist.cgi?bug_status=ASSIGNED&bug_status=FAILS_QA&bug_status=MODIFIED&bug_status=NEEDINFO&bug_status=NEW&bug_status=ON_DEV&bug_status=ON_QA&bug_status=PASSES_QA&bug_status=POST&bug_status=RELEASE_PENDING&bug_status=VERIFIED&bugidtype=include&component=Package%20Review&field0-0-0=flagtypes.name&field0-1-0=bug_id&field0-2-0=bug_id&field0-3-0=bug_id&field0-4-0=bug_id&list_id=9069930&product=Fedora&query_format=advanced&query_format=advanced&type0-0-0=notsubstring&type0-1-0=notregexp&type0-2-0=notregexp&type0-3-0=notregexp&type0-4-0=notregexp&value0-0-0=fedora-review%2B&value0-1-0=%5E163776%24&value0-2-0=%5E163778%24&value0-3-0=%5E163779%24&value0-4-0=%5E177841%24
[17]: https://fedoraproject.org/wiki/Packaging:Python

# Getting Started

1. Get a Fedora machine setup for development.  Spinning up an EC2
instance with the latest Fedora is probably the easiest way [[14]].
Using Docker is another option but it is more complicated [[13]].

1. Build a Hello World RPM [[1]].

1. Upgrade to Rawhide.

1. Learn how to use the Koji build system [[3]].

1. Fix a bug in an existing package [[15], [16]].

# Command Quickref

## Setup a local build environment:

    $ rpmdev-setuptree
    (~/rpmbuild)

This will setup a hierarchy like the following:

    ~/rpmbuild/
      SPECS/
      SRPMS/
      SOURCES/
      RPMS/
      ...

Running a build (`rpmbuild -ba`) on a spec file under `SPECS/`,
assuming sources have been placed in `SOURCES/`, will produce
rpms in `RPMS/` and/or `SRPMS/`.

## Build a package locally:

    $ rpmbuild -ba hello.spec

## Build using a Koji build server:

    $ koji build --scratch f29 ~/rpmbuild/SRPMS/hello-2.10-2.fc28.src.rpm
    https://koji.fedoraproject.org/koji/userinfo?userID=4194

## How to clean the mock cache (`/var/cache/mock`):

    $ mock --scrub all

## Download sources for a spec file:

    $ rpmbuild --undefine=_disable_source_fetch -ba package.spec

    $ spectool -g -R package.spec

## Install dependencies needed for rpmbuild:

    $ dnf builddep package.spec
    $ dnf builddep package.src.rpm

# Packaging Tips

The shebang line for Python scripts in RPMs should be
`#!/usr/bin/python2` or `#!/usr/bin/python3` and not
`#!/usr/bin/env python` \[[17]\].  This is for two
reasons.  The python version should be explicitly
specified.  And env should be avoid to avoid picking
up a users non-system version of python.

# How to Build RPMs with a Docker Image

TODO \[[13]\]

# Docker Notes

    docker container ls
    docker container ls -a

How to copy to/from a container:

    # to a running container
    docker cp HELLO.txt 25322d67c71b:/

    # from a running container
    docker cp 25322d67c71b:/HELLO.txt .

Start a stopped container:

    docker start 25322d67c71b

Accessing a running container:

    docker run -it fedora:23 /bin/bash

    # exiting attach will stop the container
    docker attach 25322d67c71b

    # exiting from exec will not stop the container
    docker exec -it 25322d67c71b bash

# References

\[1\] [https://fedoraproject.org/wiki/How_to_create_a_GNU_Hello_RPM_package][1]

\[2\] [https://developer.fedoraproject.org/tools/docker/docker-images.html][2]

\[3\] [https://fedoraproject.org/wiki/Using_the_Koji_build_system][3]

\[4\] [https://koji.fedoraproject.org/koji/][4]

\[5\] [https://fedoraproject.org/wiki/Reproducible_Builds][5]

\[6\] [https://tests.reproducible-builds.org/rpms/fedora-23.html][6]

\[7\] [https://tests.reproducible-builds.org/rpms/fedora-23/x86_64/fail2ban/fail2ban-0.9.3-1.fc23.noarch.rpm.html][7]

\[8\] [https://fedoraproject.org/wiki/Join_the_package_collection_maintainers][8]

\[9\] [http://ftp.rpm.org/max-rpm/][9]

\[10\] [https://fedoraproject.org/wiki/Packaging:Scriptlets][10]

\[11\] [https://discussion.fedoraproject.org][11]

\[12\] [https://github.com/rpm-software-management/dnf][12]

\[13\] [https://github.com/mmornati/docker-mock-rpmbuilder][13]

\[14\] [https://alt.fedoraproject.org/cloud/][14]

\[15\] [https://fedoraproject.org/wiki/Join_the_package_collection_maintainers#One-off_contributions][15]

\[16\] [https://bugzilla.redhat.com/buglist.cgi?bug_status=ASSIGNED&bug_status=FAILS_QA&bug_status...][16]

\[17\]: [https://fedoraproject.org/wiki/Packaging:Python][17]
