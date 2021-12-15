#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import itertools    # .product
import heapq        # .heappop, .heappush


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# (NONE)


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

# Read input into 2-D array
dataset = []
for line in sys.stdin:
    line = line.rstrip()
    row = [ int(c) for c in line ]
    dataset.append(row)
height = len(dataset)
assert height > 0
width = len(dataset[0])
assert width > 0

# Make weights dict from array
weights = { (x,y):dataset[y][x]
            for y in range(height) for x in range(width) }

# *** Do Computation ***

# Find shortest path
# This is basically Dijkstra's Algorithm, except that, when a vertex's
# weight goes down, we do not change its weight in the priority queue.
# Rather, we insert a new item in the priority queue with the new
# weight. This will be just a bit slower, but it's signifiantly easier
# to implement. And it's fast enough for what we need it to do.

# When dealing with distances, INF represents infinity.
INF = 999999999  # Cheesy way to do it
start = (0, 0)
end = (width-1, height-1)

# Best distance so far for each vertex
dists = { (x,y):INF
            for x,y in itertools.product(range(width),range(height)) }
dists[start] = 0

# Set of vertices that are done
done = set()

# Set up our priority queue as a minheap
heap = [(0, start)]  # Entries: (priority, vertex)

# Main loop
while True:
    assert heap  # We would normally do "while heap:"

    # Get least-distance not-done vertex v
    _, v = heapq.heappop(heap)
    if v in done:
        continue
    dv = dists[v]

    # Update distances of neighbors
    for offset in [(-1,0), (0,-1), (1,0), (0,1)]:
        w = (v[0]+offset[0], v[1]+offset[1])
        if w[0] < 0 or w[0] >= width or w[1] < 0 or w[1] >= height:
            continue
        newdw = dv + weights[w]
        if newdw < dists[w]:
            dists[w] = newdw
            heapq.heappush(heap, (newdw, w))

    # Mark vertex v as done
    if v == end:
        break
    done.add(v)

result = dists[end]

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

