#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import re           # .search


# ======================================================================
# NOTES
# ======================================================================


# We assume that the target lies entirely to the right of the y-axis and
# entirely below the x-axis.


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# shoot
# Given description of the target and initial velocity, returns pair
# (bool, int). The bool indicates whether the target was hit. The int
# gives the maximum y position.
def shoot(target, xv, yv):
    assert 0 < target[0] < target[1]
    assert target[2] < target[3] < 0

    xp, yp = 0, 0
    max_yp = yp
    while True:
        if (target[0] <= xp <= target[1] and
            target[2] <= yp <= target[3]):
            return True, max_yp
        if xp > target[1] or yp < target[2]:
            return False, max_yp

        xp += xv
        yp += yv
        if xv > 0:
            xv -= 1
        elif xv < 0:
            xv += 1
        yv -= 1

        if yp > max_yp:
            max_yp = yp


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

line = next(sys.stdin)
line = line.rstrip()
mo = re.search(r"^target area: " +
                 r"x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)$",
               line)
assert mo, "Input line not formatted properly"
target = [int(mo[1]), int(mo[2]), int(mo[3]), int(mo[4])]
assert 0 < target[0] < target[1]
assert target[2] < target[3] < 0

# *** Do Computation ***

max_yp = None
best_xv = None
best_yv = None

# The probe is going right. To hit the target, the initial x-velocity
# must be positive and no greater than target[1] (max x-coord of the
# target). Also, regardless, of whether the probe is initially going up
# or down, it will eventually be at y = 0 with its y-velocity being
# -abs(initial_y_vel). Therefore, the absolute value of the initial
# y-velocity must be at most abs(target[2]), (where target[2] is the min
# y-coord of the target).
hit_count = 0
for xv in range(1, 1+target[1]):
    for yv in range(target[2], -target[2]):
        hit, myp = shoot(target, xv, yv)
        if hit:
            hit_count += 1
            if max_yp is None or myp > max_yp:
                max_yp = myp
                best_xv = xv
                best_yv = yv

result = (f"# hits = {hit_count}\n" +
          f" Max y = {max_yp}, start velocity = ({best_xv}, {best_yv})")

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

