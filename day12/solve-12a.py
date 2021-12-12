#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import re           # .search
import collections  # .defaultdict


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def is_small(cave):
    assert type(cave) == str
    assert len(cave) > 0
    return "a" <= cave[0] <= "z"


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

# Make adjacency lists. Each vertex is identified by the given string.
# adj[s] is a set of the neighbors of s.
adj = collections.defaultdict(set)
for line in sys.stdin:
    line = line.rstrip()
    mo = re.search(r"^(\w+)-(\w+)$", line)
    assert mo
    adj[mo[1]].add(mo[2])
    adj[mo[2]].add(mo[1])
assert "start" in adj
assert "end" in adj

# *** Do Computation ***

# Find all paths using DFS.
# Assume no two large caves are adjacent; otherwise infinite loop.
path_count = 0
s = []  # Use as stack: push = .append(item), pop = .pop()
visited = { cave:False for cave in adj if is_small(cave) }
curr = "start"
assert is_small(curr)
visited[curr] = True
curr_path = [curr]
s.append(0)  # "Pop" marker
for v in adj[curr]:
    s.append(v)
while True:
    assert s
    nxt = s.pop()

    if nxt == 0:  # "Pop" marker?
        if is_small(curr):
            visited[curr] = False
        assert curr_path[-1] == curr
        curr_path.pop()
        if len(curr_path) == 0:
            assert curr == "start"
            assert s == []
            break
        curr = curr_path[-1]
        continue

    if is_small(nxt) and visited[nxt]:
        continue

    curr = nxt
    if is_small(curr):
        visited[curr] = True
    curr_path.append(curr)

    s.append(0)
    if curr == "end":
        path_count += 1
    else:
        for v in adj[curr]:
            s.append(v)

result = path_count

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

