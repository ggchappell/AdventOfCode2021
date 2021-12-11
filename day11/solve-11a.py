#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import itertools    # .product


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def do_step(size, data, flash_count):
    to_inc = [ (x, y) for x in range(size) for y in range(size) ]

    def inc(x, y):
        nonlocal flash_count, to_inc, data, size
        data[y][x] += 1
        if data[y][x] == 10:
            flash_count += 1
            for i in (-1,0,1):
                for j in (-1,0,1):
                    if i == 0 and j == 0:
                        continue
                    if 0 <= x+i < size and 0 <= y+j < size:
                        to_inc.append((x+i, y+j))

    while len(to_inc):
        x, y = to_inc.pop()
        inc(x, y)

    for x, y in itertools.product(range(size), range(size)):
        if data[y][x] > 9:
            data[y][x] = 0

    return flash_count


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

# Optional command-line argument gives x & y size of input
# (default: 10).
size = 10
if len(sys.argv) > 1:
    size = int(sys.argv[1])

dataset = []
for line in sys.stdin:
    line = line.rstrip()
    row = [ int(c) for c in line ]
    assert len(row) == size
    dataset.append(row)
assert len(dataset) == size

# *** Do Computation ***

num_steps = 100

flash_count = 0
for _ in range(num_steps):
    flash_count = do_step(size, dataset, flash_count)

result = flash_count

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

