#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import re           # .search


# ======================================================================
# NOTES
# ======================================================================


# Alternate solution to day 22 part 2, based on idea from David Maxwell.


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def clamp(v, lo, hi):
    """Return v clamped to range [lo, hi].

    >>> clamp(1, 2, 3)
    2
    >>> clamp(4, 0, 1)
    1
    >>> clamp(6, 5, 8)
    6

    """
    assert lo <= hi
    if v < lo:
        return lo
    elif v > hi:
        return hi
    else:
        return v


def nonempty_region(r):
    """Return True if given region is nonempty.

    >>> nonempty_region([1,2,3,4,5,6])
    True
    >>> nonempty_region([1,2,4,4,5,6])
    False

    """
    assert type(r) == list
    assert len(r) == 6
    return (r[0] != r[1] and
            r[2] != r[3] and
            r[4] != r[5])


def region_diff(ra, rb):
    """Yields disjoint regions whose union is ra - rb.

    >>> list(region_diff([1,3,1,3,1,3],[2,3,2,3,2,3]))
    [[1, 2, 1, 3, 1, 3], [2, 3, 1, 2, 1, 3], [2, 3, 2, 3, 1, 2]]

    """
    rrb = rb[:]

    rrb[0] = clamp(rrb[0], ra[0], ra[1])
    rrb[1] = clamp(rrb[1], ra[0], ra[1])
    rrb[2] = clamp(rrb[2], ra[2], ra[3])
    rrb[3] = clamp(rrb[3], ra[2], ra[3])
    rrb[4] = clamp(rrb[4], ra[4], ra[5])
    rrb[5] = clamp(rrb[5], ra[4], ra[5])

    r1 = [ra[0], rrb[0], ra[2], ra[3], ra[4], ra[5]]
    if nonempty_region(r1):
        yield r1
    r2 = [rrb[1], ra[1], ra[2], ra[3], ra[4], ra[5]]
    if nonempty_region(r2):
        yield r2
    r3 = [rrb[0], rrb[1], ra[2], rrb[2], ra[4], ra[5]]
    if nonempty_region(r3):
        yield r3
    r4 = [rrb[0], rrb[1], rrb[3], ra[3], ra[4], ra[5]]
    if nonempty_region(r4):
        yield r4
    r5 = [rrb[0], rrb[1], rrb[2], rrb[3], ra[4], rrb[4]]
    if nonempty_region(r5):
        yield r5
    r6 = [rrb[0], rrb[1], rrb[2], rrb[3], rrb[5], ra[5]]
    if nonempty_region(r6):
        yield r6


# ======================================================================
# MAIN PROGRAM
# ======================================================================


def main():
    # *** Process Input ***

    dataset = []
    for line in sys.stdin:
        line = line.rstrip()
        rngpat = r"(-?\d+)\.\.(-?\d+)"
        pat = f"^(on|off) x={rngpat},y={rngpat},z={rngpat}"
        mo = re.search(pat, line)
        assert mo
        onoff = (mo[1] == "on")
        limits = [int(mo[2]), int(mo[3])+1,
                  int(mo[4]), int(mo[5])+1,
                  int(mo[6]), int(mo[7])+1]
        for i in range(3):
            assert limits[2*i] < limits[2*i+1]
        dataset.append((onoff, limits))

    # *** Do Computation ***

    # Create list of regions
    regions = []
    line_count = 0
    for onoff, limits in dataset:
        line_count += 1
        print(f"Processing input line {line_count}/{len(dataset)}")
        new_regions = []
        for r in regions:
            # For speed; always doing "else" part gives correct results
            if (limits[1] <= r[0] or
                limits[0] >= r[1] or
                limits[3] <= r[2] or
                limits[2] >= r[3] or
                limits[5] <= r[4] or
                limits[4] >= r[5]):
                new_regions.append(r)
            else:
                for rr in region_diff(r, limits):
                    new_regions.append(rr)
        if onoff:
            new_regions.append(limits)
        regions = new_regions

    # Count actual "on" cubes
    print("Counting \"on\" cubes")
    num_on_cubes = 0
    for r in regions:
        num_on_cubes += (r[1]-r[0])*(r[3]-r[2])*(r[5]-r[4])

    result = num_on_cubes

    # *** Print Answer ***

    print("-" * 60)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()

