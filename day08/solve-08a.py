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
    strs = line.split()
    entry1 = [ set(ss) for ss in strs[:10] ]
    assert strs[10] == "|"
    entry2 = [ set(ss) for ss in strs[11:] ]
    dataset.append([entry1, entry2])

# *** Do Computation ***

count = 0
for entry in dataset:
    for s in entry[1]:
        if len(s) in {2, 3, 4, 7}:
            count += 1

result = count

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

