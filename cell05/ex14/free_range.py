#!/usr/bin/env python3

import sys

x = sys.argv

if len(x) < 3:
    print("none")

else:
    num1 = int(x[1])
    num2 = int(x[2])
    nums = []
    for i in range(num1, num2 + 1):
        nums.append(i)
    print(nums)