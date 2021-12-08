#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def advance(nums):
    new = []
    for i in range(len(nums)):
        if nums[i] > 0:
            nums[i] -= 1
        else:
            nums[i] = 6
            new.append(8)
    return nums + new


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

dataset = []
line = next(sys.stdin)
line = line.rstrip()
dataset = [ int(nstr) for nstr in line.split(",") ]

# *** Do Computation ***

for _ in range(80):
    dataset = advance(dataset)
result = len(dataset)

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

