#!/usr/bin/env python3

import sys

x = sys.argv

if len(x) != 2 or ('z' not in x[1]):
    print("none")
else:
    for i in x[1]:
        if i == 'z':
            print('z', end='')
    print()