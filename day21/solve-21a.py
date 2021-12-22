#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import re           # .search


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


num_die_rolls = 0
last_die_roll = 100


def roll_die():
    global num_die_rolls, last_die_roll
    num_die_rolls += 1
    last_die_roll += 1
    if last_die_roll == 101:
        last_die_roll = 1
    return last_die_roll


def roll_die_3():
    ddd = roll_die() + roll_die() + roll_die()
    return ddd


# ======================================================================
# MAIN PROGRAM
# ======================================================================


def main():
    # *** Process Input ***

    line = next(sys.stdin)
    line = line.rstrip()
    mo = re.search(r"Player 1 starting position: (1?\d)$", line)
    assert mo
    start1 = int(mo[1])
    assert 1 <= start1 <= 10

    line = next(sys.stdin)
    line = line.rstrip()
    mo = re.search(r"Player 2 starting position: (1?\d)$", line)
    assert mo
    start2 = int(mo[1])
    assert 1 <= start2 <= 10

    # *** Do Computation ***

    score_to_win = 1000

    score1, score2 = 0, 0
    pos1, pos2 = start1, start2
    while True:
        d = roll_die_3()
        pos1 += d
        pos1 = (pos1-1) % 10 + 1
        score1 += pos1
        if score1 >= score_to_win:
            break

        d = roll_die_3()
        pos2 += d
        pos2 = (pos2-1) % 10 + 1
        score2 += pos2
        if score2 >= score_to_win:
            break

    result = min(score1, score2) * num_die_rolls

    # *** Print Answer ***

    #print("-" * 60)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()

