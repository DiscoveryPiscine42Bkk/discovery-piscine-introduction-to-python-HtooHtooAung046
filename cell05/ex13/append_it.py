#!/usr/bin/env python3

import sys

x = sys.argv

if len(x) < 2:
    print("none")

else:
    for i in x[1:]:
        if i.endswith("ism"):
            continue
        print(i+"ism")
