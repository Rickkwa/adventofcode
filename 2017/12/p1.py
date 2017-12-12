import sys
import os
import math
sys.path.append('../../lib')
from aoc import *


def main(inp):
    count = 0
    mapping = {}
    for words in inp:
        words = map(lambda x: x.strip(","), words)
        mapping[words[0]] = words[2:]

    # print mapping

    queue = []
    seen = []
    queue.append('0')
    while len(queue) > 0:
        pid = queue.pop()
        # print seen
        for p in mapping[pid]:
            if p not in seen:
                queue.append(p)
                count += 1
                seen.append(p)
    return count



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    print main(read_words("sample{0}.txt".format(part)))

    print "=== Real ==="
    print main(read_words("input.txt"))
