#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import re           # .search
import collections  # .defaultdict


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def list2pairs(t):
    assert type(t) == list
    pairs = collections.defaultdict(int)
    for i in range(len(t)-1):
        cc = t[i] + t[i+1]
        assert type(cc) == str
        assert len(cc) == 2
        pairs[cc] += 1
    return pairs

def apply_rules(pp_in, rules):
    pp_out = collections.defaultdict(int)
    for cc in pp_in:
        assert type(cc) == str
        assert len(cc) == 2
        if cc in rules:
            cc1 = cc[0] + rules[cc]
            cc2 = rules[cc] + cc[1]
            pp_out[cc1] += pp_in[cc]
            pp_out[cc2] += pp_in[cc]
        else:
            pp_out[cc] += pp_in[cc]
    return pp_out

def least_most(pp):
    # The number of times a letter appears is the number of times a pair
    # holding it appears, plus 1 if the letter is the first or last in
    # the template, divided by 2. This should be the same as the number
    # of times a pait containing it appears, rounded up to the nearest
    # even integer, divided by 2.
    quants = collections.defaultdict(int)
    for cc in pp:
        quants[cc[0]] += pp[cc]
        quants[cc[1]] += pp[cc]
    for cc in quants:
        q = quants[cc]
        if q % 2 == 1:
            q += 1
        quants[cc] = q // 2
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

# *rules* is the list of rules. Each rule is stored as a pair. For
# example, the rule "CH -> B" is stored as ("CH", "B").
rules = {}
for line in sys.stdin:
    line = line.rstrip()
    mo = re.search(r"^([A-Z][A-Z]) -\> ([A-Z])$", line)
    assert mo
    rules[mo[1]] = mo[2]

# *** Do Computation ***

num_steps = 40

# The current string is stored as a dict. Each key is a string of length
# 2. The associated value tells how often this pair of characters
# appears as an adjacent pair in the string. For example, the string
# "ABBBAB" would be stored as { "AB":2, "BA":1, "BB":2 }.
pp = list2pairs(template)
for step in range(num_steps):
    pp = apply_rules(pp, rules)
c1, qc1, c2, qc2 = least_most(pp)
result = qc2 - qc1

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

