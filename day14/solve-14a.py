#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import re           # .search
import collections  # .defaultdict


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def apply_rules(s_in, rules):
    s_out = s_in[0]
    for i in range(len(s_in)-1):
        for r in rules:
            if s_in[i] == r[0] and s_in[i+1] == r[1]:
                s_out += r[2]
                break
        s_out += s_in[i+1]
    return s_out


def least_most(ss):
    quants = collections.defaultdict(int)
    for c in ss:
        quants[c] += 1
    c1 = min(quants, key = (lambda c: quants[c]))
    c2 = max(quants, key = (lambda c: quants[c]))
    return c1, quants[c1], c2, quants[c2]


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

# The template is stored as a list of characters.
line = next(sys.stdin)
line = line.rstrip()
assert line
template = [ c for c in line ]

line = next(sys.stdin)
line = line.rstrip()
assert not line

# *rules* is the list of rules. Each rule is stored as a triple. For
# example, the rule "CH -> B" is stored as ("C", "H", "B").
rules = []
for line in sys.stdin:
    line = line.rstrip()
    mo = re.search(r"^([A-Z])([A-Z]) -\> ([A-Z])$", line)
    assert mo
    rules.append((mo[1], mo[2], mo[3]))

# *** Do Computation ***

num_steps = 10

ss = template
for _ in range(num_steps):
    ss = apply_rules(ss, rules)
c1, qc1, c2, qc2 = least_most(ss)
result = qc2 - qc1

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

