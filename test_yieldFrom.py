#!/usr/bin/python

from collections import Iterable

def flattern(items, ignore_type=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_type):
            yield from flattern(x)
        else:
            yield x

items = [1, 2, [3, 4,[5, 6], 7], 8]
itemsiStr = ['Dave', 'Paula', ['Thomas', 'Lewis']]
print(list(flattern(items)))
print(list(flattern(itemsiStr)))
