#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import collections  # .defaultdict


# ======================================================================
# NOTES
# ======================================================================


# An image is stored as a collections.defaultdict. Keya are pairs of
# int: (x, y). Associated values are 0 for pixel off and 1 for pixel on.
# Calling .default_factory() gets the background value.


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


# factories
# Two constant functions, for use as default factory for a defaultdict.
# For i = 0 or 1, factories[i] is a function returning i.
factories = [
    lambda: 0,
    lambda: 1,
]


def print_img(img):
    """Prints a portion of the given image. FOR TESTING ONLY.

    The rectangle printed is the smallest rectangle enclosing all
    non-default value.

    """
    assert len(img) > 0
    x, y = next(iter(img))
    xmin, xmax, ymin, ymax = x, x, y, y
    for x, y in img:
        if x < xmin:
            xmin = x
        if x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y
    for y in range(ymin, 1+ymax):
        for x in range(xmin, 1+xmax):
            print('.' if img[(x,y)] == 0 else "#", end="")
        print()


def process_image(alg, img_in):
    default_value_in = img_in.default_factory()
    if default_value_in == 0:
        default_value_out = alg[0]
    else:
        default_value_out = alg[511]
    img_out = collections.defaultdict(factories[default_value_out])

    todo = set()
    for x, y in img_in:
        for yo in range(-1, 2):
            for xo in range(-1, 2):
                todo.add((x+xo, y+yo))

    for x, y in todo:
        alg_index = 0
        for yo in range(-1, 2):
            for xo in range(-1, 2):
                alg_index = 2 * alg_index + img_in[(x+xo, y+yo)]
        img_out[(x, y)] = alg[alg_index]

    return img_out


def count_pixels_on(img):
    default_value_in = img.default_factory()
    assert default_value_in == 0

    count = 0
    for x, y in img:
        if img[(x, y)] == 1:
            count += 1
    return count



# ======================================================================
# MAIN PROGRAM
# ======================================================================


def main():
    # *** Process Input ***

    alg_raw = next(sys.stdin)
    alg_raw = alg_raw.rstrip()
    assert len(alg_raw) == 512
    assert all(( c == '.' or c == '#' for c in alg_raw ))

    alg = []
    for c in alg_raw:
        alg.append(1 if c == '#' else 0)

    line = next(sys.stdin)
    line = line.rstrip()
    assert line == ""

    img_raw = []
    width = None
    for line in sys.stdin:
        line = line.rstrip()
        if width is None:
            width = len(line)
        else:
            assert len(line) == width
        img_raw.append(line)

    img = collections.defaultdict(factories[0])
    for y, line in enumerate(img_raw):
        for x, c in enumerate(line):
            if c == "#":
                img[(x,y)] = 1

    # *** Do Computation ***

    num_enhance = 50

    for i in range(num_enhance):
        print(i)
        img = process_image(alg, img)
    result = count_pixels_on(img)

    # *** Print Answer ***

    #print("-" * 60)
    print(f"Answer: {result}")


if __name__ == "__main__":
    main()

