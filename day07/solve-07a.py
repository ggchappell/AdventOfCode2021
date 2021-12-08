#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# (NONE)


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

line = next(sys.stdin)
line = line.rstrip()
dataset = [ int(nstr) for nstr in line.split(",") ]

# *** Do Computation ***

# Find a median of the dataset
dataset.sort()
median = dataset[len(dataset) // 2]
print(f"Position: {median}")

result = sum([ abs(k-median) for k in dataset ])

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

