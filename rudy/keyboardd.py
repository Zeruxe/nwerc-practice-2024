#!/usr/bin/env python
#
# Solution to https://open.kattis.com/problems/keyboardd
#
# Problem K of NWERC 2020
#
# 2024 Rudy Matela
#
# Kinda-sorta a golfy port of my Haskell solution to Python
# The algorithm is a bit different... but is the same "in spirit".

from collections import Counter
a = Counter(input())
b = Counter(input())
print(''.join([k for k in a.keys() if b[k] > a[k]]))
