#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin, .argv


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def filter_it(thelist, bitpos, mostflag):
    stats = [0, 0]
    for binstr in thelist:
        c = binstr[bitpos]
        assert c == "0" or c == "1"
        if c == "0":
            stats[0] += 1
        else:
            stats[1] += 1
    if stats[0] > stats[1]:
        thebit = "0" if mostflag else "1"
    else:
        thebit = "1" if mostflag else "0"
    newlist = [ s for s in thelist if s[bitpos] == thebit ]
    return newlist


def bin2dec(binstr):
    assert type(binstr) == str
    value = 0
    for c in binstr:
        assert c == "0" or c == "1"
        value *= 2
        if c == "1":
            value += 1
    return value


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

dataset = []
for line in sys.stdin:
    line = line.rstrip()
    dataset.append(line)

# *** Do Computation ***

for mostflag in [True, False]:
    thelist = dataset[:]
    for i in range(len(dataset[0])):
        assert len(thelist) != 0
        if len(thelist) == 1:
            break
        thelist = filter_it(thelist, i, mostflag)
    if mostflag:
        og_rating = bin2dec(thelist[0])
    else:
        cs_rating = bin2dec(thelist[0])

# *** Print Answer ***

print(f"Oxygen generator rating: {og_rating}", end="")
print(f"; CO2 scrubber rating: {cs_rating}")
result = og_rating * cs_rating
print(f"Answer: {result}")

