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
    count = 0
    for i in range(40000000):
        gen_a = generate(gen_a, 16807)
        # print "A", gen_a
        gen_b = generate(gen_b, 48271)
        # print "B", gen_b
        if gen_a % 2 != gen_b % 2:
            continue
        gen_a_bin = format(gen_a, 'b')
        gen_b_bin = format(gen_b, 'b')
        if gen_a_bin[-16:] == gen_b_bin[-16:]:
            # print gen_a_bin, gen_b_bin
            count += 1

    return count



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    print main(read_words("sample{0}.txt".format(part)))

    print "=== Real ==="
    print main(read_words("input.txt"))
