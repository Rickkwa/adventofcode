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
        result[index % len(result)] = sub_list[i]
        index += 1
    return result


def get_dense(sparse):
    result = []
    for i in range(len(sparse) / 16):
        result.append(reduce(lambda x, y: x ^ y, sparse[i * 16: i * 16 + 16]))
    return result


def main(chars, list_size):
    cur_pos = 0
    skip_size = 0

    sparse = range(0, list_size)
    for rnd in range(64):
        for n in map(lambda x: ord(x), list(chars)) + [17, 31, 73, 47, 23]:
            n = int(n)
            sparse = process(sparse, cur_pos, n)
            cur_pos += n + skip_size
            cur_pos = cur_pos % list_size
            skip_size += 1

    dense = get_dense(sparse)
    return "".join(map(lambda x: format(x, 'x').zfill(2), dense))



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    sample = main(read_lines("sample{0}.txt".format(part))[0], 256)
    print sample

    print "=== Real ==="
    real = main(read_lines("input{0}.txt".format(part))[0], 256)
    print real
