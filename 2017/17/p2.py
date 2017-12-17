import sys
import os
import math
sys.path.append('../../lib')
from aoc import *


def main(steps):
    buf_len = 1
    pos = 0
    result = None
    for i in range(50000000):
        pos = (pos + steps) % buf_len
        if pos == 0:
            result = i + 1
        pos += 1
        buf_len += 1
    return result



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    # print "=== Test ==="
    # print main(3)

    print "=== Real ==="
    print main(363)
