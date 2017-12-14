import sys
import os
import math
sys.path.append('../../lib')
from aoc import *

# Day 10 part 2 stuff
# def process(lst, start_index, length):
#     tmp_lst = lst[:] * ((length + start_index) / len(lst) + 1)
#     sub_list = tmp_lst[start_index:start_index + length]
#     sub_list.reverse()

#     result = lst[:]
#     index = start_index
#     for i in range(length):
#         result[index % len(result)] = sub_list[i]
#         index += 1
#     return result


# def get_dense(sparse):
#     result = []
#     for i in range(len(sparse) / 16):
#         result.append(reduce(lambda x, y: x ^ y, sparse[i * 16: i * 16 + 16]))
#     return result


# def do_hash(keystr, list_size=256):
#     cur_pos = 0
#     skip_size = 0

#     sparse = range(0, list_size)
#     for rnd in range(64):
#         for n in map(lambda x: ord(x), list(keystr)) + [17, 31, 73, 47, 23]:
#             n = int(n)
#             sparse = process(sparse, cur_pos, n)
#             cur_pos += n + skip_size
#             cur_pos = cur_pos % list_size
#             skip_size += 1

#     dense = get_dense(sparse)
#     return "".join(map(lambda x: format(x, 'x').zfill(2), dense))


def convert_adjacent_free(disk, row, col):
    queue = [(row, col)]

    while len(queue) > 0:
        r, c = queue.pop()
        disk[r][c] = '0'
        # print r, c
        if r - 1 >= 0 and disk[r - 1][c] == '1':
            queue.append((r - 1, c))
        if c + 1 < 128 and disk[r][c + 1] == '1':
            queue.append((r, c + 1))
        if r + 1 < 128 and disk[r + 1][c] == '1':
            queue.append((r + 1, c))
        if c - 1 >= 0 and disk[r][c - 1] == '1':
            queue.append((r, c - 1))

def find_used(disk):
    for r in range(len(disk)):
        row = disk[r]
        if '1' in row:
            c = row.index('1')
            return (r, c)
    return None

def count_regions(disk):
    count = 0
    # find a used square and convert all to free
    while True:
        coords = find_used(disk)
        if coords is None:
            break
        r, c = coords
        convert_adjacent_free(disk, r, c)
        count += 1
    return count


def main(keystr):
    # count_used = 0
    disk = []
    for i in range(128):
        key = keystr + "-" + str(i)
        # keyhash = do_hash(key, 256)
        keyhash = knot_hash(key)
        binary = list(bin(int(keyhash, 16))[2:].zfill(128))
        disk.append(binary)
        # print len(keyhash)
        # count_used += binary.count('1')
    return count_regions(disk)



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    print main(read_lines("sample{0}.txt".format(part))[0])

    print "=== Real ==="
    print main(read_lines("input.txt")[0])
