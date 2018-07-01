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

# Getting Started

1. Get a Fedora machine setup for development.  Spinning up an EC2
instance with the latest Fedora is probably the easiest way [[14]].
Using Docker is another option but it is more complicated [[13]].

1. Build a Hello World RPM [[1]].

1. Upgrade to Rawhide.

1. Learn how to use the Koji build system [[3]].

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
