#!/usr/bin/env python3

import sys

x = sys.argv

if len(x) == 1:
    print("none")
else:
    print(f"parameters: {len(x[1:])}")
    for i in x[1:]:
        print(f"{i} : {len(i)}")