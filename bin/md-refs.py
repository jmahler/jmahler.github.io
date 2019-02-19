#!/usr/bin/python3

# Generate a #References section from a
# Markdown file that can be added at the end.
#
# $ cat file | md-refs.py
#
# (from in Vim)
# :r !cat % | md-refs.py
#

import sys
import re

# [1]: https://security.archlinux.org/advisory
is_ref = re.compile(r'\[(\d+)\]: (.*)')

refs = []
for line in sys.stdin:
    m = is_ref.match(line)
    if m:
        refs.append([m.group(1), m.group(2)])
        
print("")
print("# References")
print("")

for ref in refs:
    print("[[{0}]] {1}\n".format(ref[0], ref[1]))

