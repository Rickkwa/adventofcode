import sys
import os
import math
sys.path.append('../../lib')
from aoc import *


def main(inp):

    nums = []
    for line in inp:
        nums.append(int(line))

    count = 0
    index = 0
    while True:
        old_index = index
        index += nums[index]
        count += 1
        if index < 0 or index >= len(nums):
            break
        if nums[old_index] >= 3:
            nums[old_index] -= 1
        else:
            nums[old_index] += 1
    return count




if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    print main(read_lines("sample{0}.txt".format(part)))

    print "=== Real ==="
    print main(read_lines("input{0}.txt".format(part)))
