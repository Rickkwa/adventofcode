import sys
import os
import math
sys.path.append('../../lib')
from aoc import *


def main(inp):
    registers = {}
    for words in inp:
        registers[words[0]] = 0

    for words in inp:
        if eval("{0} {1} {2}".format(str(registers.get(words[4], 0)), words[5], words[6])):
            if words[1] == "inc":
                registers[words[0]] += int(words[2])
            elif words[1] == "dec":
                registers[words[0]] -= int(words[2])

    print registers
    return max(registers.values())



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    ops = []
    for words in read_words("input{0}.txt".format(part)):
        ops.append(words[5])
    print set(ops)

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    print main(read_words("sample{0}.txt".format(part)))

    print "=== Real ==="
    print main(read_words("input{0}.txt".format(part)))
