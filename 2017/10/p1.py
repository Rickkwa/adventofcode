import sys
import os
import math
sys.path.append('../../lib')
from aoc import *


def process(lst, start_index, length):
    tmp_lst = lst[:] * ((length + start_index) / len(lst) + 1)
    sub_list = tmp_lst[start_index:start_index + length]
    sub_list.reverse()

    result = lst[:]
    index = start_index
    for i in range(length):
        if i < len(sub_list):
            result[index % len(result)] = sub_list[i]
        index += 1
    return result


def main(nums, list_size):
    cur_pos = 0
    skip_size = 0

    result = range(0, list_size)
    for n in nums:
        n = int(n)
        result = process(result, cur_pos, n)
        cur_pos += n + skip_size
        cur_pos = cur_pos % list_size
        skip_size += 1

    return result



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    sample = main(read_words("sample{0}.txt".format(part), ",")[0], 5)
    print sample
    print sample[0] * sample[1]

    print "=== Real ==="
    real = main(read_words("input{0}.txt".format(part), ",")[0], 256)
    print real[:5]
    print real[0] * real[1]
