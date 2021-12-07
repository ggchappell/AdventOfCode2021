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

dataset = []
for line in sys.stdin:
    line = line.rstrip()
    if dataset == []:
        dataset = [ [0,0] for i in range(len(line)) ]
           # Counts: [# of 0s, # of 1s] for each bit position
    for i, c in enumerate(line):
        assert c == "0" or c == "1"
        if c == "0":
            dataset[i][0] += 1
        else:
            dataset[i][1] += 1

# *** Do Computation ***

gamrate = 0
epsrate = 0
for [a, b] in dataset:
    # a: # of 0s in this bit position, b: # of 1s in this bit position
    assert a != b  # Cannot have same # of 0s, 1s in a bit position
    if a > b:      # More 0s than 1s in this bit position
        gamrate = 2 * gamrate
        epsrate = 2 * epsrate + 1
    else:          # More 1s than 0s in this bit position
        gamrate = 2 * gamrate + 1
        epsrate = 2 * epsrate
        

# *** Print Answer ***

print(f"Gamma rate: {gamrate}; epsilon rate: {epsrate}")
result = gamrate * epsrate
print(f"Answer: {result}")

