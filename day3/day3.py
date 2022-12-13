#!/usr/bin/env python

from collections import defaultdict
from itertools import islice

# 1st star - this is just dicts
# This is really gross code, but works, I'll refactor with questions and stuff another time.
with open('input', 'r') as f:
    runsum = 0
    for line in f.readlines():
        d1 = defaultdict(int)
        l1 = line[0:int(len(line) / 2)]
        l2 = line[int(len(line) / 2):len(line)]
        for l in l1: # TODO: easier way to define this reduce operator?
            d1[l] += 1
        for l in l2:
            if d1[l] != 0:
                # print(f"found {l}")
                if 'a' <= l <= 'z':
                    runsum += ord(l) - 96
                else:
                    runsum += ord(l) - 38
                break
    print(runsum)

# 2nd star - this is also just dicts
with open('input', 'r') as f:
    runsum = 0
    while True:
        d1, d2 = defaultdict(int), defaultdict(int)
        lines = [line.strip() for line in list(islice(f, 3))]
        if not lines:
            break
        for l in lines[0]:
            d1[l] += 1
        for l in lines[1]:
            if d1[l]: # truthiness, right?
                d2[l] += 1
        for l in lines[2]:
            if d1[l] and d2[l]:
                print(f"found {l}")
                if 'a' <= l <= 'z':
                    runsum += ord(l) - 96
                else:
                    runsum += ord(l) - 38
                break
    print(runsum)