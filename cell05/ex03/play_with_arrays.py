#!/usr/bin/env python3
org_arr = [2,8,9,48,8,22,-12,2]
print(org_arr)
new_arr = set()
for i in org_arr:
    if i > 5 :
        new_arr.add(i+2)
print(new_arr)