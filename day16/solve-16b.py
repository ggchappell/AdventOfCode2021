#!/usr/bin/env python3
# Advent of Code 2021
# Glenn G. Chappell

import sys          # .stdin
import functools    # .reduce


# ======================================================================
# HELPER FUNCTIONS
# ======================================================================


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
# Each returns a pair: (bool, int). The bool is True on a correct parse,
# False otherwise. If the bool is True, then the int is the result of
# evaluating the expression the packet represents.


def parse_packet(stream):
    ok, version = get_num(stream, 3)
    if not ok: return False, -1
    ok, type_id = get_num(stream, 3)
    if not ok: return False, -1

    if type_id == 4:
        # Packet is literal value
        ok, val = parse_literal_packet_contents(stream)
        if not ok: return False, -1
        return True, val

    # Packet is operator
    ok, length_type_id = get_num(stream, 1)
    if not ok: return False, -1
    values = []
    if length_type_id == 0:
        ok, total_length = get_num(stream, 15)
        if not ok: return False, -1
        tstream = truncate_stream(stream, total_length)
        while True:
            ok, val = parse_packet(tstream)
            if not ok: break
            values.append(val)
    else:  # length_type_id == 1
        ok, num_subpackets = get_num(stream, 11)
        if not ok: return False, -1
        for _ in range(num_subpackets):
            ok, val = parse_packet(stream)
            if not ok: return False, -1
            values.append(val)

    if type_id == 0:    # Sum
        assert len(values) >= 1
        val = sum(values)
        return True, val
    elif type_id == 1:  # Product
        assert len(values) >= 1
        val = functools.reduce(lambda x, y: x*y, values)
        return True, val
    elif type_id == 2:  # Minimum
        assert len(values) >= 1
        val = min(values)
        return True, val
    elif type_id == 3:  # Maximum
        assert len(values) >= 1
        val = max(values)
        return True, val
    elif type_id == 5:  # Greater than
        assert len(values) == 2
        val = 1 if values[0] > values[1] else 0
        return True, val
    elif type_id == 6:  # Less than
        assert len(values) == 2
        val = 1 if values[0] < values[1] else 0
        return True, val
    elif type_id == 7:  # Equal
        assert len(values) == 2
        val = 1 if values[0] == values[1] else 0
        return True, val
    else:
        assert False, "parse_packet: bad type id"


def parse_literal_packet_contents(stream):
    val = 0
    while True:
        ok, b = get_num(stream, 1)
        if not ok: return False, -1
        ok, n = get_num(stream, 4)
        if not ok: return False, -1
        val = 16 * val + n
        if b == 0:
            break
    return True, val


# ======================================================================
# MAIN PROGRAM
# ======================================================================


# *** Process Input ***

dataset = next(sys.stdin)

# *** Do Computation ***

stream = next_bit(dataset)
version_total = 0
ok, result = parse_packet(stream)
assert ok

# *** Print Answer ***

#print("-" * 60)
print(f"Answer: {result}")

