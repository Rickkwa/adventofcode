import sys
import os
import math
sys.path.append('../../lib')
from aoc import *


def main(inp):
    candidate = {}
    for line in inp:
        parent = line[0]
        candidate[parent] = candidate.get(parent, 0)
        if "->" in line:
            children = map(lambda x: x.strip(","), line[line.index("->") + 1:])
            for c in children:
                candidate[c] = candidate.get(c, 0) + 1
    for key, value in candidate.iteritems():
        if value == 0:
            return key



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    print main(read_words("sample{0}.txt".format(part)))

    print "=== Real ==="
    print main(read_words("input{0}.txt".format(part)))
