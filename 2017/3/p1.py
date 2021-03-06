import sys
import os
import math

def main(inp):
    # Get which odd numbered squared is closest and <= to our input
    level = 0
    while (1 + level * 2) * (1 + level * 2) <= inp:
        level += 1
    level -= 1
    n = 1 + level * 2

    # Calculate the coordinate of the spiral where the odd numbered squared is
    coords = [level, level] # (1, 1) is in Q4

    # Traverse the ring counter clockwise to our input number
    for i in range(n * n + 1, inp + 1):
        if i == n * n + 1: # The next ring starts 1 square to the right of odd squared number
            coords[0] += 1
        elif i <= n * n + n + 1:
            coords[1] -= 1
        elif i <= n * n + 2 * (n + 1):
            coords[0] -= 1
        elif i <= n * n + 3 * (n + 1):
            coords[1] += 1
        elif i <= n * n + 4 * (n + 1):
            coords[0] += 1

    return abs(coords[0]) + abs(coords[1])



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    print "=== Part {0} ===".format(part)
    print main(361527)

    # print "== 25:", main(25)
    # print "== 26:", main(26)
    # print "== 27:", main(27)
    # print "== 28:", main(28)
    print "== 32:", main(32)
    print "== 35:", main(35)
