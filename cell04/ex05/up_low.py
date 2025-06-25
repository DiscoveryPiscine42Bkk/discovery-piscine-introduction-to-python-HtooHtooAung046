#!/usr/bin/env python3
x = input("Give a word: ")
for i in x:
    if i.isupper():
        print(i.lower(),end="")
    else:
        print(i.upper(),end="")