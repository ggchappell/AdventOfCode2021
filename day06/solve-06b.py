#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def advance(counts):
    assert len(counts) == 9
    k = counts.pop(0)
    counts.append(k)
    counts[6] += k
    return counts


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

dataset = [ 0 for _ in range(9) ]
line = next(sys.stdin)
line = line.rstrip()
for nstr in line.split(","):
    n = int(nstr)
    dataset[n] += 1

# *** Do Computation ***

for _ in range(256):
    dataset = advance(dataset)
result = sum(dataset)

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

