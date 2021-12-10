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
    ss = ""
    while not stack.empty():
        c = stack.get()
        ss += partner[c]
    return False, ss  # Incomplete, sequence of chars to finish


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

dataset = []
for line in sys.stdin:
    line = line.rstrip()
    dataset.append(line)

# *** Do Computation ***

score = { ")":1, "]":2, "}":3, ">":4 }
line_score_list = []
for line in dataset:
    corrupted, ss = check_line(line)
    if corrupted:
        continue
    line_score = 0
    for c in ss:
        line_score = 5*line_score + score[c]
    line_score_list.append(line_score)

line_score_list.sort()
result = line_score_list[len(line_score_list)//2]

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

