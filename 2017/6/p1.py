import sys
import os
import math
sys.path.append('../../lib')
from aoc import *



def redistribute(nums):
    max_index = nums.index(max(nums))
    n = nums[max_index]
    nums[max_index] = 0
    index = max_index + 1
    while n > 0:
        nums[index % len(nums)] += 1
        index += 1
        n -= 1
    return nums


def main(inp):
    count = 0
    seen = []
    while True:
        # inp = redistribute(inp)
        inp = redistribute(inp)
        count += 1
        if ",".join(map(lambda x: str(x), inp)) in seen:
            break
        seen.append(",".join(map(lambda x: str(x), inp)))
    return count



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    print main(read_ints("sample{0}.txt".format(part))[0])

    print "=== Real ==="
    print main(read_ints("input{0}.txt".format(part))[0])
