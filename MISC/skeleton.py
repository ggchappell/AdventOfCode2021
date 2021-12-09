#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin, .argv
import re           # .search
import itertools    # .count, .chain, .product,
                    #  .combinations, .permutations
import copy         # .deepcopy
import collections  # .defaultdict
import os           # .system
import time         # .sleep
import functools    # .reduce
import queue        # .SimpleQueue


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
    # ...
    dataset.append(42)

# *** Do Computation ***

result = 42

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

