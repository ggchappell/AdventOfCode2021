#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import re           # .search


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# (NONE)


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

    lo = -50
    hi = 50

    # Restrict dataset to lo .. hi in each coordinate
    restricted_dataset = []
    for onoff, limits in dataset:
        if (limits[0] > hi or limits[1] < lo or
            limits[2] > hi or limits[3] < lo or
            limits[4] > hi or limits[5] < lo):
            continue
        limits = limits[:]
        for i in range(3):
            if limits[2*i] < lo:
                limits[2*i] = lo
            if limits[2*i+1] > hi:
                limits[2*i+1] = hi
        restricted_dataset.append((onoff, limits))

    # Make set of all "on" cubes
    cube_set = set()
    for onoff, limits in restricted_dataset:
        for x in range(limits[0], 1+limits[1]):
            for y in range(limits[2], 1+limits[3]):
                for z in range(limits[4], 1+limits[5]):
                    if onoff:
                        cube_set.add((x, y, z))
                    else:
                        cube_set.discard((x, y, z))

    result = len(cube_set)

    # *** Print Answer ***

    #print("-" * 60)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()

