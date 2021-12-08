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

result = 0
for entry in dataset:
    # Find digit representations
    dig2set = {}
    for s in entry[0]:
        if len(s) == 2:
            dig2set[1] = s
        elif len(s) == 3:
            dig2set[7] = s
        elif len(s) == 4:
            dig2set[4] = s
        elif len(s) == 7:
            dig2set[8] = s
    for s in entry[0]:
        if len(s) == 5:
            if dig2set[1] < s:
                dig2set[3] = s
            elif len(s & dig2set[4]) == 2:
                dig2set[2] = s
            else:
                dig2set[5] = s
        elif len(s) == 6:
            if dig2set[4] < s:
                dig2set[9] = s
            elif dig2set[1] < s:
                dig2set[0] = s
            else:
                dig2set[6] = s
    set2dig = {}
    for dig in dig2set:
        set2dig[frozenset(dig2set[dig])] = dig

    # Compute value
    value = 0
    for s in entry[1]:
        dig = set2dig[frozenset(s)]
        value = 10*value + dig
    result += value

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

