import sys
import os
import math
sys.path.append('../../lib')
from aoc import *

# Day 10 part 2 stuff
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


def do_hash(keystr, list_size=256):
    cur_pos = 0
    skip_size = 0

    sparse = range(0, list_size)
    for rnd in range(64):
        for n in map(lambda x: ord(x), list(keystr)) + [17, 31, 73, 47, 23]:
            n = int(n)
            sparse = process(sparse, cur_pos, n)
            cur_pos += n + skip_size
            cur_pos = cur_pos % list_size
            skip_size += 1

    dense = get_dense(sparse)
    return "".join(map(lambda x: format(x, 'x').zfill(2), dense))



def main(keystr):
    count_used = 0
    disk = []
    for i in range(128):
        key = keystr + "-" + str(i)
        keyhash = do_hash(key, 256)
        binary = list(bin(int(keyhash, 16))[2:].zfill(128))
        disk.append(binary)
        count_used += binary.count('1')
    return count_used



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    print main(read_lines("sample{0}.txt".format(part))[0])

    print "=== Real ==="
    print main(read_lines("input.txt")[0])
