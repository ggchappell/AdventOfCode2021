#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import queue        # .LifoQueue


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def check_line(line):
    open_set = { "(", "[", "{", "<" }
    close_set = { ")", "]", "}", ">" }
    partner = { "(":")", "[":"]", "{":"}", "<":">" }
    assert type(line) == str
    stack = queue.LifoQueue()
    for i, c in enumerate(line):
        if c in open_set:
            stack.put(c)
            continue
        assert c in close_set
        assert not stack.empty()
        c2 = stack.get()
        c3 = partner[c2]
        if c == c3:
            continue
        return True, i  # Corrupted, first bad char @ index i
    assert not stack.empty()
    return False, -1  # Incomplete


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

dataset = []
for line in sys.stdin:
    line = line.rstrip()
    dataset.append(line)

# *** Do Computation ***

score = { ")":3, "]":57, "}":1197, ">":25137 }
total = 0
for line in dataset:
    corrupted, bad_index = check_line(line)
    if not corrupted:
        continue
    bad_char = line[bad_index]
    total += score[bad_char]
result = total

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

