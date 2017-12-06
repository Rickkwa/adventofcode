import sys
import os
import math
sys.path.append('../../lib')
from aoc import *


def main(inp):
    for line in inp:
        pass



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    print main(read_lines("sample{0}.txt".format(part)))

    print "=== Real ==="
    print main(read_lines("input{0}.txt".format(part)))
