import sys
import os
import math
sys.path.append('../../lib')
from aoc import *

def apply_ignore(stream):
    parse_ignore_str = ""
    while len(stream) > 0:
        if stream[0] == "!":
            stream = stream[2:]
        else:
            parse_ignore_str += stream[0]
            stream = stream[1:]
    return parse_ignore_str

def count_garbage(stream):
    result = 0
    garbage_on = False
    while len(stream) > 0:
        if stream[0] == "<" and not garbage_on:
            garbage_on = True
        elif stream[0] == ">":
            garbage_on = False
        else:
            if garbage_on:
                result += 1
        stream = stream[1:]
    return result

def get_score(stream):
    return count_garbage(apply_ignore(stream))

def main(inp):
    for line in inp:
        print get_score(line)


if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    main(read_lines("sample{0}.txt".format(part)))

    print "=== Real ==="
    main(read_lines("input{0}.txt".format(part)))
