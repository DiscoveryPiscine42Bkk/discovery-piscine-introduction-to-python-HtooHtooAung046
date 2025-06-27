#!/usr/bin/env python3
def array_of_names(names):
    arr_names = []
    for A, B in names.items():
        arr_names.append(f"{A.capitalize()}{B.capitalize()}")
    return arr_names
persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))