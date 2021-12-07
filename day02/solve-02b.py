#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin, .argv


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# (NONE)


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

convert = {
    "forward":1,
    "down":2,
    "up":3,
    }

dataset = []
for line in sys.stdin:
    line = line.rstrip()
    words = line.split()
    assert len(words) == 2
    tup = (convert[words[0]], int(words[1]))
    dataset.append(tup)

# *** Do Computation ***

horiz = 0
depth = 0
aim = 0
for (a, b) in dataset:
    if a == 1:
        horiz += b
        depth += aim * b
    elif a == 2:
        aim += b
    elif a == 3:
        aim -= b

# *** Print Answer ***

#print("-" * 60)
print(f"Horizontal position: {horiz}; depth: {depth}")
result = horiz * depth
print(f"Answer: {result}")

