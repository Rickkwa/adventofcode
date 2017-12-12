import sys
import os
import math
sys.path.append('../../lib')
from aoc import *

def get_max_distance(steps):
    max_distance = 0
    x = 0
    y = 0
    for step in steps:
        if "n" in step:
            y += 1
        elif "s" in step:
            y -= 1
        if "e" in step:
            x += 1
        elif "w" in step:
            x -= 1
        max_distance = max(max_distance, calc_distance(x, y))
    return max_distance


def calc_distance(x, y):
    count = 0
    while x != 0 and y != 0:
        if y < 0:
            y += 1
        else:
            y -= 1
        if x < 0:
            x += 1
        else:
            x -= 1
        count += 1
    return count + max(abs(x), abs(y))


def main(inp):
    for steps in inp:
        coords = get_max_distance(steps)
        print coords


if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    print main(read_words("sample{0}.txt".format(part), ","))

    print "=== Real ==="
    print main(read_words("input.txt", ","))
