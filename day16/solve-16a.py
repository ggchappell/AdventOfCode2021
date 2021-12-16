#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


version_total = 0  # For sum of version numbers


# STREAM FUNCTIONS
# Each returns an iterator.


# next_bit: generator. Given hex string, yield ints: 0 or 1 bits as long
# as hex string lasts, and -1 thereafter.
def next_bit(hex_str):
    assert type(hex_str) == str
    for c in hex_str:
        if '0' <= c <= '9':
            hex_val = int(c)
        elif 'A' <= c <= 'F':
            hex_val = ord(c) - ord('A') + 10
        else:
            assert False, "next_bit: hex_str contains non-hex char"
        bits = []
        for _ in range(4):
            bits.insert(0, hex_val % 2)
            hex_val //= 2
        yield from bits
    while True:
        yield -1


def truncate_stream(stream, length):
    assert type(length) == int
    assert length >= 0
    for _ in range(length):
        val = next(stream)
        yield val
    while True:
        yield -1


# UTILITY "GET" FUNCTIONS
# Each returns a pair: (bool, int). The bool is True on a correct parse,
# False otherwise. If the bool is True, then the int is the requested
# value.


def get_bit(stream):
    b = next(stream)
    assert type(b) == int
    ok = (b == 0 or b == 1)
    return ok, b


def get_num(stream, num_digs):
    assert type(num_digs) == int
    assert num_digs > 0
    val = 0
    for _ in range(num_digs):
        ok, b = get_bit(stream)
        if not ok: return False, -1
        val = 2 * val + b
    return True, val


# PARSING FUNCTIONS (recursive-descent parser)
# Each returns True on a correct parse, False otherwise.


def parse_packet(stream):
    ok, version = get_num(stream, 3)
    if not ok: return False
    global version_total      # JUST FOR THIS PROBLEM!!!
    version_total += version  # JUST FOR THIS PROBLEM!!!
    ok, type_id = get_num(stream, 3)
    if not ok: return False

    if type_id == 4:
        # Packet is literal value
        ok = parse_literal_packet_contents(stream)
        if not ok: return False
        return True

    # Packet is operator
    ok, length_type_id = get_num(stream, 1)
    if not ok: return False
    if length_type_id == 0:
        ok, total_length = get_num(stream, 15)
        if not ok: return False
        tstream = truncate_stream(stream, total_length)
        while True:
            ok = parse_packet(tstream)
            if not ok: break
        return True
    else:  # length_type_id == 1
        ok, num_subpackets = get_num(stream, 11)
        if not ok: return False
        for _ in range(num_subpackets):
            ok = parse_packet(stream)
            if not ok: return False
        return True


def parse_literal_packet_contents(stream):
    while True:
        ok, b = get_num(stream, 1)
        if not ok: return False
        ok, n = get_num(stream, 4)
        if not ok: return False
        if b == 0:
            break
    return True


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

dataset = next(sys.stdin)

# *** Do Computation ***

stream = next_bit(dataset)
version_total = 0
ok = parse_packet(stream)
assert ok

result = version_total

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

