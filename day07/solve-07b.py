#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def cost(pos, dataset):
    total = 0
    for n in dataset:
        d = abs(n-pos)
        c2 = ((d+1)*d) // 2
        total += c2
    return total


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

line = next(sys.stdin)
line = line.rstrip()
dataset = [ int(nstr) for nstr in line.split(",") ]

# *** Do Computation ***

# Find the nearest integer to the mean of the dataset
mean = sum(dataset) / len(dataset)
pos = int(mean + 0.5)

# Now creep up or down as long as this reduces the totsl cost
c = [cost(pos-1, dataset), cost(pos, dataset), cost(pos+1, dataset)]
while True:
    if c[0] >= c[1] and c[2] >= c[1]:
        thecost = c[1]
        break
    elif c[0] < c[1]:
        pos -= 1
        c = [cost(pos-1, dataset), c[0], c[1]]
    else:
        pos += 1
        c = [c[1], c[2], cost(pos+1)]
print(f"Position: {pos}")

result = thecost

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

