#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import re           # .search
import functools    # .reduce
import ast          # .literal_eval


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# ck_explode
# Given a snailfish number, determine whether an explode action can be
# applied. If so, apply it and return (True, n), where n is the new
# snailfish number. Otherwise, return (False, sfn).
def ck_explode(sfn):
    assert type(sfn) == str

    depth = 0
    for i, c in enumerate(sfn):
        if c == "[":
            depth += 1
            if depth >= 5:
                mo2 = re.search(r"^\[(\d+),(\d+)\]", sfn[i:])
                if mo2:
                    vv_a = mo2[1]
                    vv_b = mo2[2]
                    b2 = mo2.start(0) + i
                    assert b2 == i
                    ss2 = mo2[0]
                    e2 = mo2.end(0) + i
                    break
        elif c == "]":
            depth -= 1
    else:
        # No pair to explode
        assert depth == 0
        return False, sfn

    # Got pair to explode
    mo1 = re.search(r"\D(\d+)\D+$", sfn[:b2])
    if mo1:
        b1 = mo1.start(1)
        ss1 = mo1[1]
        e1 = mo1.end(1)
        before = sfn[:b1] + str(int(ss1)+int(vv_a)) + sfn[e1:b2]
    else:
        before = sfn[:b2]

    mo3 = re.search(r"^\D+(\d+)\D", sfn[e2:])
    if mo3:
        b3 = mo3.start(1) + e2
        ss3 = mo3[1]
        e3 = mo3.end(1) + e2
        after = sfn[e2:b3] + str(int(vv_b)+int(ss3)) + sfn[e3:]
    else:
        after = sfn[e2:]

    new_sfn = before + "0" + after
    return True, new_sfn


# ck_split
# Given a snailfish number, determine whether a split action can be
# applied. If so, apply it and return (True, n), where n is the new
# snailfish number. Otherwise, return (False, sfn).
def ck_split(sfn):
    assert type(sfn) == str

    mo = re.search(r"[^\d](\d*[1-9]\d)[^\d]", sfn)
    if not mo:
        # No number to split
        return False, sfn

    # Got number to split
    assert mo
    b = mo.start(1)
    ss = mo[1]
    e = mo.end(1)

    val = int(ss)
    new_sfn = (sfn[:b] +
               "[" + str(val//2) + "," + str((val+1)//2) + "]"
               + sfn[e:])
    return True, new_sfn


# ck_action
# Given a snailfish number, determine whether either kind of reduce
# action can be applied. If so, apply the proper kind of reduce action
# and return (True, n), where n is the new snailfish number. Otherwise,
# return (False, sfn).
def ck_action(sfn):
    assert type(sfn) == str
    changed, sfn = ck_explode(sfn)
    if changed:
        return True, sfn
    changed, sfn = ck_split(sfn)
    if changed:
        return True, sfn
    return False, sfn


# add
# Given two snailfish numbers, add them add them and return the reduced
# form of the result.
def add(sfn1, sfn2):
    assert type(sfn1) == str
    assert type(sfn2) == str
    new_sfn = "["+sfn1+","+sfn2+"]"
    while True:
        changed, new_sfn = ck_action(new_sfn)
        if not changed:
            break
    return new_sfn


# sum_list
# Given a list of snailfish numbers, add them and return the result. For
# each snailfish number, it is added to the total, and then the total is
# reduced before proceeding to the next snailfish number.
def sum_list(sfn_list):
    assert type(sfn_list) == list
    return functools.reduce(lambda s1, s2: add(s1, s2), sfn_list)


# magnitude
# Given a snailfish number, return is magnitude as an int.
def magnitude(sfn):
    def tree_mag(tree):
        if type(tree) == int:
            return tree
        assert type(tree) == list
        assert len(tree) == 2
        return 3*tree_mag(tree[0]) + 2*tree_mag(tree[1])

    assert type(sfn) == str
    tree = ast.literal_eval(sfn)
    return tree_mag(tree)


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***s

dataset = []
for line in sys.stdin:
    line = line.rstrip()
    dataset.append(line)

# *** Do Computation ***

new_sfn = sum_list(dataset)
result = magnitude(new_sfn)

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

