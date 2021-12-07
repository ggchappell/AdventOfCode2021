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

dataset = []
for line in sys.stdin:
    line = line.rstrip()
    value = int(line)
    dataset.append(value)

# *** Do Computation ***

result = 0
for i in range(1, len(dataset)-2):
    if dataset[i+2] > dataset[i-1]:
      # No need to add all three in sliding window, since two of them
      # are duplicated
        result += 1

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

