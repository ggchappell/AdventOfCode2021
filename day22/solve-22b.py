#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import re           # .search


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


def ix_range(bd, lo, hi):
    """List of boundaries, numbers -> yields indices in boundary list.

    >>> bd = [2, 6, 9, 15, 17, 20, 30]
    >>> list(ix_range(bd, 9, 19))
    [2, 3, 4]
    >>> bd = [1, 2, 3, 4, 5, 6]
    >>> list(ix_range(bd, 2, 3))
    [1, 2]

    """
    for ix in range(len(bd)):
        if lo <= bd[ix] <= hi:
            yield ix


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
        limits = [int(mo[2]), int(mo[3]),
                  int(mo[4]), int(mo[5]),
                  int(mo[6]), int(mo[7])]
        for i in range(3):
            assert limits[2*i] <= limits[2*i+1]
        dataset.append((onoff, limits))

    # *** Do Computation ***

    # Figure out boundaries of x, y, z ranges
    xbd_set = set()
    ybd_set = set()
    zbd_set = set()
    for _, limits in dataset:
        xbd_set.add(limits[0])
        xbd_set.add(limits[1]+1)
        ybd_set.add(limits[2])
        ybd_set.add(limits[3]+1)
        zbd_set.add(limits[4])
        zbd_set.add(limits[5]+1)
    xbd = list(xbd_set)
    xbd.sort()
    assert xbd
    ybd = list(ybd_set)
    ybd.sort()
    assert ybd
    zbd = list(zbd_set)
    zbd.sort()
    assert zbd

    # Make array indicating all "on" cube ranges
    print("Creating 3-D array")
    cube_ranges = [ [ [ False for zi in range(len(zbd)) ]
                              for yi in range(len(ybd)) ]
                              for xi in range(len(xbd)) ]
    line_count = 0
    for onoff, limits in dataset:
        line_count += 1
        print(f"Processing input line {line_count}/{len(dataset)}")
        for xi in ix_range(xbd, limits[0], limits[1]):
            for yi in ix_range(ybd, limits[2], limits[3]):
                for zi in ix_range(zbd, limits[4], limits[5]):
                    if onoff:
                        cube_ranges[xi][yi][zi] = True
                    else:
                        cube_ranges[xi][yi][zi] = False

    # Count actual "on" cubes
    print("Counting \"on\" cubes")
    num_on_cubes = 0
    for xi in range(len(xbd)):
        for yi in range(len(ybd)):
            for zi in range(len(zbd)):
                if cube_ranges[xi][yi][zi]:
                    num_on_cubes += ((xbd[xi+1]-xbd[xi]) *
                                     (ybd[yi+1]-ybd[yi]) *
                                     (zbd[zi+1]-zbd[zi]))

    result = num_on_cubes

    # *** Print Answer ***

    print("-" * 60)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()

