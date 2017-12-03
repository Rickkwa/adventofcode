import sys
import os

def get_adjacent_sum(spiral, x, y):
    total = 0
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            if x_offset == 0 and y_offset == 0:
                continue
            if x + x_offset in spiral and y + y_offset in spiral[x + x_offset]:
                total += spiral[x + x_offset][y + y_offset]

    return total



def main(inp):
    spiral = { 0: {0: 1} } # (1, 1) is in Q4
    level = 0

    while True:

        # Fill out each ring of the spiral at a time.
        # Starting with bottom right (1 sq to the right of the bottom right item in previous ring) and going counter clockwise.
        level += 1
        x = level
        y = level - 1
        n = level * 2 + 1
        for i in range(1, level * 8 + 1):
            # Set spiral value for x, y
            spiral[x] = spiral.get(x, {})
            spiral[x][y] = get_adjacent_sum(spiral, x, y)
            if spiral[x][y] > inp:
                return spiral[x][y]

            # Get new x and y
            if i < n - 1:
                y -= 1
            elif i < 2 * (n - 1):
                x -= 1
            elif i < 3 * (n - 1):
                y += 1
            elif i < 4 * (n - 1):
                x += 1



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    print "=== Part {0} ===".format(part)
    print main(361527)
    # print main(25)
    # print main(300)
    # print main(140)
    # print main(10)
    # print main(15)
