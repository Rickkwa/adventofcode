import sys
import os
import math
sys.path.append('../../lib')
from aoc import *


def main(inp):
    registers = {}
    sound_history = []
    i = 0
    while i < len(inp):
    # for i in range(len(inp)):
        line = inp[i]
        inst, reg = line[:2]
        registers[reg] = registers.get(reg, 0)
        if len(line) == 3:
            try:
                value = int(line[2])
            except:
                value = registers.get(line[2], 0)

        if inst == 'set':
            registers[reg] = value
        elif inst == 'snd':
            sound_history.append((reg, registers[reg]))
        elif inst == 'add':
            registers[reg] += value
        elif inst == 'mul':
            registers[reg] *= value
        elif inst == 'mod':
            registers[reg] %= value
        elif inst == 'rcv':
            if registers[reg] != 0:
                freq = sound_history.pop()
                return freq
        elif inst == 'jgz':
            if registers[reg] > 0:
                i += value
                i -= 1
        i += 1
        # print i, inst, registers
    # print registers
    return None





if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    print main(read_words("sample{0}.txt".format(part)))

    print "=== Real ==="
    print main(read_words("input.txt"))
