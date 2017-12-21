import sys
import os
import math
sys.path.append('../../lib')
from aoc import *


def get_value(value, registers):
    # if value is a number, return the number. Else if it is a register, return value of register (default 0 if register isn't in dict)

    try:
        result = int(value)
    except:
        result = registers.get(value, 0)
    return result


def send_val(pid, programs, value):
    if pid == 0:
        programs[1]['in_queue'].append(value)
    elif pid == 1:
        programs[0]['in_queue'].append(value)


def process(pid, programs, instructions):
    # Return if 1 if program sends to other program; else 0
    registers = programs[pid]['registers']
    instruction = instructions[programs[pid]['offset']]
    op, a1 = instruction[0], instruction[1]
    if len(instruction) == 3:
        a2 = get_value(instruction[2], registers)
    else:
        a2 = None
    # print pid, programs[pid], op, a1, a2

    result = 0
    if op == 'set':
        registers[a1] = a2
    elif op == 'snd':
        send_val(pid, programs, get_value(a1, registers))
        result = 1
    elif op == 'add':
        registers[a1] += a2
    elif op == 'mul':
        registers[a1] *= a2
    elif op == 'mod':
        registers[a1] %= a2
    elif op == 'rcv':
        if len(programs[pid]['in_queue']) > 0:
            registers[a1] = programs[pid]['in_queue'].pop(0)
            programs[pid]['dl'] = 0
        else:
            programs[pid]['dl'] += 1
            programs[pid]['offset'] -= 1
    elif op == 'jgz':
        if get_value(a1, registers) > 0:
            programs[pid]['offset'] += a2
            programs[pid]['offset'] -= 1

    programs[pid]['offset'] += 1
    return result


def main(inp):
    programs = {
        0: {
            'registers': {'p': 0},
            'in_queue': [],
            'offset': 0,
            'dl': 0
        },
        1: {
            'registers': {'p': 1},
            'in_queue': [],
            'offset': 0,
            'dl': 0
        }
    }

    result = 0
    while programs[0]['offset'] < len(inp) or programs[1]['offset'] < len(inp):
        process(0, programs, inp)
        result += process(1, programs, inp)

        # Check for deadlock and exit if there is
        if programs[0]['dl'] >= 4 and programs[1]['dl'] >= 4:
            print "DL"
            print programs
            return result
    print "Normal"
    print programs
    return result


if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    print main(read_words("sample{0}.txt".format(part)))

    print "=== Real ==="
    print main(read_words("input.txt"))
