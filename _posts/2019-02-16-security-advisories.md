---
layout: post
title: "Survey of Security Advisory Systems"
date: 2019-02-16 1:00
category: Linux
tags: [Linux, Packaging, Security]
---

[1]: https://security.archlinux.org/advisory

[2]: https://wiki.archlinux.org/index.php/Arch_Security_Team

[3]: https://github.com/archlinux/arch-security-tracker

[4]: https://usn.ubuntu.com/

[5]: https://www.debian.org/security/2019/

[6]: https://launchpad.net/ubuntu-cve-tracker

[7]: https://git.launchpad.net/ubuntu-cve-tracker/tree/active/CVE-2012-1096

[8]: https://security-tracker.debian.org/tracker/

[9]: https://salsa.debian.org/security-tracker-team/security-tracker/tree/master/data

[10]: https://alas.aws.amazon.com/

# Introduction

Every major Linux distribution tracks security advisories and
CVEs [[1], [4], [5], [8], [10]].  And the systems they use are
largely the same.  This is a survey of those systems.

| Distro      | Source?       | Store   | Server | Lang         | Other |
|-------------|---------------|---------|--------|--------------|-------|
| ArchLinux   | yes [[2]]     | db      | uswgi  | Python Flask |       |
| AmazonLinux | no            | ???     | s3     | ???          |       |
| Debian      | yes [[9]]     | git     | ???    | ???          |       |
| Fedora      | ???           | ???     | ???    | ???          |       |
| Ubuntu      | yes  [[6]]    | git [7] | ???    | ???          |       |

# References

[[1]] https://security.archlinux.org/advisory

[[2]] https://wiki.archlinux.org/index.php/Arch_Security_Team

[[3]] https://github.com/archlinux/arch-security-tracker

[[4]] https://usn.ubuntu.com/

[[5]] https://www.debian.org/security/2019/

[[6]] https://launchpad.net/ubuntu-cve-tracker

[[7]] https://git.launchpad.net/ubuntu-cve-tracker/tree/active/CVE-2012-1096

[[8]] https://security-tracker.debian.org/tracker/

[[9]] https://salsa.debian.org/security-tracker-team/security-tracker/tree/master/data

[[10]] https://alas.aws.amazon.com/
