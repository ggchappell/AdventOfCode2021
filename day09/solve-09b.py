#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import itertools    # .product
import queue        # .SimpleQueue


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

# Find all low points
lowpts = set()
for x, y in itertools.product(range(xsize), range(ysize)):
    v = dataset[y][x]
    if ((x == 0 or dataset[y][x-1] > v) and
        (x == xsize-1 or dataset[y][x+1] > v) and
        (y == 0 or dataset[y-1][x] > v) and
        (y == ysize-1 or dataset[y+1][x] > v)):
        # We have a low point
        lowpts.add((x, y))
assert len(lowpts) >= 3

# Find all basin sizes
basin_sizes = []
for x, y in lowpts:
    # Find size of basin for this low point by doing a BFS.
    this_size = 0
    done = [ [ False for _ in range(xsize) ] for _ in range(ysize) ]
    q = queue.SimpleQueue()
    q.put((x, y))
    while not q.empty():
        x, y = q.get()
        if done[y][x]:
            continue

        done[y][x] = True
        this_size += 1

        v = dataset[y][x]
        if x > 0 and dataset[y][x-1] > v and dataset[y][x-1] != 9:
            q.put((x-1, y))
        if x < xsize-1 and dataset[y][x+1] > v and dataset[y][x+1] != 9:
            q.put((x+1, y))
        if y > 0 and dataset[y-1][x] > v and dataset[y-1][x] != 9:
            q.put((x, y-1))
        if y < ysize-1 and dataset[y+1][x] > v and dataset[y+1][x] != 9:
            q.put((x, y+1))
    basin_sizes.append(this_size)
assert len(basin_sizes) == len(lowpts)

# Compute result
basin_sizes.sort()
result = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

