import sys
import os
import math
sys.path.append('../../lib')
from aoc import *


def spin(dancers, n):
    for i in range(n):
        item = dancers.pop()
        dancers.insert(0, item)


def exchange(dancers, posa, posb):
    dancers[posa], dancers[posb] = dancers[posb], dancers[posa]


def partner(dancers, namea, nameb):
    posa = int(dancers.index(namea))
    posb = int(dancers.index(nameb))
    exchange(dancers, posa, posb)


def do_dance(instructions, init_dancers='abcdefghijklmnop'):
    dancers = list(init_dancers)
    for ins in instructions:
        # print ins
        if ins[0] == 's':
            spin(dancers, int(ins[1:]))
        elif ins[0] == 'x':
            exchange(dancers, int(ins[1:].split("/")[0]), int(ins[1:].split("/")[1]))
        elif ins[0] == 'p':
            partner(dancers, ins[1:].split("/")[0], ins[1:].split("/")[1])
    return dancers


def main(instructions):
    iterations = 1000000000
    dance_order = list('abcdefghijklmnop')
    i = 0
    seen = []
    while i < iterations:
        dance_order = do_dance(instructions, "".join(dance_order))
        if "".join(dance_order) in seen:
            return "".join(seen[iterations % len(seen) - 1])
        seen.append("".join(dance_order))
        i += 1
    return "".join(dance_order)



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    # print main(read_lines("sample{0}.txt".format(part)))

    print "=== Real ==="
    print main(read_words("input.txt", ",")[0])
