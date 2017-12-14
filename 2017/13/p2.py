import sys
import os
import math
sys.path.append('../../lib')
from aoc import *


def get_scanner_pos(layers, picosecond):
    scanner_loop = range(layers) + range(layers - 2, 0, -1)
    return scanner_loop[picosecond % len(scanner_loop)]


def main(inp, picosecond=0):
    firewall = {}
    for line in inp:
        firewall[int(line[0].strip(":"))] = int(line[1])

    depth = -1
    while depth <= max(firewall.keys()):
        depth += 1
        if depth in firewall:
            scanner = get_scanner_pos(firewall[depth], picosecond)
            if scanner == 0:
                return False
        picosecond += 1
    return True



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    i = 0
    while True:
        escaped = main(read_words("sample{0}.txt".format(part)), i)
        if escaped:
            print i
            break
        i += 1

    print "=== Real ==="
    i = 0
    while True:
        escaped = main(read_words("input.txt"), i)
        if escaped:
            print i
            break
        i += 1


