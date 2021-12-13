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

# Read points
points = []
for line in sys.stdin:
    line = line.rstrip()
    if line == "":
        break
    mo = re.search(r"^(\d+),(\d+)$", line)
    assert mo
    x, y = int(mo[1]), int(mo[2])
    points.append((x, y))
assert points

# Read folds
folds = []
for line in sys.stdin:
    line = line.rstrip()
    mo = re.search(r"^fold along ([xy])=(\d+)$", line)
    assert mo
    axis, value = mo[1], int(mo[2])
    folds.append((axis, value))
assert folds

# *** Do Computation ***

# Do folds
ptset = set(points)
for axis, value in folds:
    # Do the fold
    ptset2 = set()
    for pt in ptset:
        if axis == "x" and pt[0] > value:
            pt2 = (2*value - pt[0], pt[1])
        elif axis == "y" and pt[1] > value:
            pt2 = (pt[0], 2*value - pt[1])
        else:
            pt2 = pt
        ptset2.add(pt2)
    ptset = ptset2

# Make the final array
maxx = max(( x for x, y in ptset ))
maxy = max(( y for x, y in ptset ))
array = [ [ "." for _ in range(1+maxx) ] for _ in range(1+maxy) ]
for x, y in ptset:
    array[y][x] = "#"

# *** Print Answer ***

#print("-" * 60)
print(f"Answer:")
for row in array:
    for c in row:
        assert type(c) == str
        print(c, end="")
    print()

