#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import itertools    # .product


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
    row = [ int(c) for c in line ]
    if not dataset:
        xsize = len(row)
    else:
        assert len(row) == xsize
    dataset.append(row)
ysize = len(dataset)
# Use "dataset[y][x]" for 0 <= x < xsize, 0 <= y < ysize.

# *** Do Computation ***

total = 0
for x, y in itertools.product(range(xsize), range(ysize)):
    v = dataset[y][x]
    if ((x == 0 or dataset[y][x-1] > v) and
        (x == xsize-1 or dataset[y][x+1] > v) and
        (y == 0 or dataset[y-1][x] > v) and
        (y == ysize-1 or dataset[y+1][x] > v)):
        # We have a low point
        risk = v+1
        total += risk
result = total

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

