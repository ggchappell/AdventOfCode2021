#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import itertools    # .product


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# check: Check whether board wins with number sequence nums. Doing it
# this way is inefficient, but not so inefficient that we don't get a
# reasonably quick answer for the input we are actually given.
def check(board, nums):
    marked = [ [False]*5 for _ in range(5) ]
    for n in nums:
        for i,k in itertools.product(range(5), range(5)):
            if n == board[i][k]:
                assert not marked[i][k]
                marked[i][k] = True
                # If we have a winning row/col, then it must be the
                # row/col containing entry [i][k].
                if all(marked[i]) or all([ row[k] for row in marked ]):
                    total = 0
                    for a,b in itertools.product(range(5), range(5)):
                        if not marked[a][b]:
                            total += board[a][b]
                    return (True, n * total)
    return (False, 0)


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

line = next(sys.stdin)
line = line.rstrip()
nums = [ int(nstr) for nstr in line.split(",") ]

boards = []
for line in sys.stdin:
    line = line.rstrip()
    assert line == ""
    b = []
    for i in range(5):
        line = next(sys.stdin)
        line = line.rstrip()
        b.append([ int(nstr) for nstr in line.split() ])
    boards.append(b)

# *** Do Computation ***

best = [-1, -1, 0]  # Board winning last (so far), turn it wins, score
for bnum, b in enumerate(boards):
    for i in range(len(nums)):
        win, score = check(b, nums[:i+1])
        if win:
            if i > best[1]:
                best = [bnum, i, score]
            break
    else:
        assert False, f"Board #{bnum} does not win"
assert best[0] != -1
result = best[2]

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

