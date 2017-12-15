import sys
import os
import math
sys.path.append('../../lib')
from aoc import *

def generate(value, factor):
    return (value * factor) % 2147483647

def main(inp):
    gen_a = int(inp[0][-1])
    gen_b = int(inp[1][-1])

    slot_a = None
    slot_b = None
    count = 0
    pairs = 0
    while pairs < 5000000:
        if slot_a is None:
            gen_a = generate(gen_a, 16807)
            if gen_a % 4 == 0:
                slot_a = gen_a

        if slot_b is None:
            gen_b = generate(gen_b, 48271)
            if gen_b % 8 == 0:
                slot_b = gen_b

        if slot_a is not None and slot_b is not None:
            gen_a_bin = format(slot_a, 'b')
            gen_b_bin = format(slot_b, 'b')
            pairs += 1
            # print gen_a_bin, gen_b_bin

            if slot_a % 2 == slot_b % 2:
                if gen_a_bin[-16:] == gen_b_bin[-16:]:
                    count += 1
            slot_a = None
            slot_b = None

    return count



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    print main(read_words("sample{0}.txt".format(part)))

    print "=== Real ==="
    print main(read_words("input.txt"))
