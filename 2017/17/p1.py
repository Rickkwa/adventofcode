import sys
import os
import math
sys.path.append('../../lib')
from aoc import *


def main(steps):
    buf = [0]
    pos = 0
    for i in range(2017):
        pos = (pos + steps) % len(buf) + 1
        buf.insert(pos, i + 1)
    # print buf
    return buf[buf.index(2017) + 1]



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    print main(3)

    print "=== Real ==="
    print main(363)
