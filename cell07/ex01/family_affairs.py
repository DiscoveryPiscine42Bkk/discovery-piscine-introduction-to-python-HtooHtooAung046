#!/usr/bin/env python3

def find_the_redheads(x1):
    return list(filter(lambda name: x1[name]=='red', x1.keys()))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))