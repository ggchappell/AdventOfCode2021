#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import re           # .search
import collections  # .defaultdict


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# (NONE)


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

    score_to_win = 21

    # state: dict of (pos1, pos2, score1, score2):num_universes
    state = collections.defaultdict(int)
    state[(start1, start2, 0, 0)] = 1

    # die: list of (total, num_universes)
    die = [
        (3, 1),  # 1,1,1
        (4, 3),  # 1,1,2
        (5, 6),  # 1,1,3; 1,2,2
        (6, 7),  # 1,2,3; 2,2,2
        (7, 6),  # 2,2,3; 1,3,3
        (8, 3),  # 2,3,3
        (9, 1),  # 3,3,3
    ]

    while True:
        # All games done?
        for p1, p2, s1, s2 in state:
            if s1 < score_to_win and s2 < score_to_win:
                break
        else:
            break

        # Player 1 moves
        new_state = collections.defaultdict(int)
        for p1, p2, s1, s2 in state:
            num_univ_prev = state[(p1, p2, s1, s2)]
            if s1 >= score_to_win or s2 >= score_to_win:
                new_state[(p1,p2,s1,s2)] += num_univ_prev
                continue
            for val, num_univ_die in die:
                p1n = p1 + val
                p1n = (p1n-1) % 10 + 1
                s1n = s1 + p1n
                new_state[(p1n,p2,s1n,s2)] += num_univ_prev*num_univ_die
        state = new_state

        # All games done?
        for p1, p2, s1, s2 in state:
            if s1 < score_to_win and s2 < score_to_win:
                break
        else:
            break

        # Player 2 moves
        new_state = collections.defaultdict(int)
        for p1, p2, s1, s2 in state:
            num_univ_prev = state[(p1, p2, s1, s2)]
            if s1 >= score_to_win or s2 >= score_to_win:
                new_state[(p1,p2,s1,s2)] += num_univ_prev
                continue
            num_univ_prev = state[(p1, p2, s1, s2)]
            for val, num_univ_die in die:
                p2n = p2 + val
                p2n = (p2n-1) % 10 + 1
                s2n = s2 + p2n
                new_state[(p1,p2n,s1,s2n)] += num_univ_prev*num_univ_die
        state = new_state

    # Count universes in which each player wins
    num_univ_p1win = 0
    num_univ_p2win = 0
    for p1, p2, s1, s2 in state:
        num_univ = state[(p1, p2, s1, s2)]
        assert s1 != s2
        if s1 > s2:
            num_univ_p1win += num_univ
        else:
            num_univ_p2win += num_univ

    result = max(num_univ_p1win, num_univ_p2win)

    # *** Print Answer ***

    #print("-" * 60)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()

