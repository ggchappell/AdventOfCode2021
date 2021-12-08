#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import re           # .search


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# (NONE)


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

dataset = []
for line in sys.stdin:
    line = line.rstrip()
    mo = re.search(r"(\d+),(\d+) -\> (\d+),(\d+)", line)
    if not mo:
        print(line)
        assert False, "Line not properly formatted"
    x1 = int(mo[1])
    y1 = int(mo[2])
    x2 = int(mo[3])
    y2 = int(mo[4])
    if x1 != x2 and y1 != y2:
        continue
    dataset.append((x1, y1, x2, y2))

# *** Do Computation ***

coverage = {}
for x1, y1, x2, y2 in dataset:
    if x1 == x2:
        diry = 1 if (y2 > y1) else -1
        for y in range(y1, y2+diry, diry):
            pt = (x1, y)
            coverage[pt] = 1 + coverage.get(pt, 0)
    else:  # y1 == y2
        dirx = 1 if (x2 > x1) else -1
        for x in range(x1, x2+dirx, dirx):
            pt = (x, y1)
            coverage[pt] = 1 + coverage.get(pt, 0)

result = 0
for x, y in coverage:
    if coverage[(x,y)] > 1:
        result += 1

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

