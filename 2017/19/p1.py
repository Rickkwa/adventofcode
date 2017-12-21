import sys
import os
import math
sys.path.append('../../lib')
from aoc import *


def valid_coords(grid, coords):
    # Return true iff the coord exists and is not empty space
    row, col = coords
    if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0:
        return False
    return grid[row][col] != " "


def get_coords(current_coords, new_direction):
    row, col = current_coords
    if new_direction == "N":
        row -= 1
    elif new_direction == "S":
        row += 1
    elif new_direction == "E":
        col += 1
    elif new_direction == "W":
        col -= 1
    return (row, col)


def main(inp):
    compass = "NESW"
    grid = []
    for line in inp:
        grid.append(list(line))

    coords = (0, grid[0].index('|'))
    direction = "S"

    result = ""
    while True:
        if grid[coords[0]][coords[1]].isalpha():
            result += grid[coords[0]][coords[1]]

        index = compass.index(direction)

        # Priority of directions relative to current coord to check
        q = [compass[index], compass[(index + 1) % 4], compass[(index + 3) % 4]]

        # Get next coords
        while len(q) > 0:
            new_dir = q.pop(0)
            new_coords = get_coords(coords, new_dir)
            if valid_coords(grid, new_coords):
                direction = new_dir
                coords = new_coords
                break

        # If no next direction coord, we've reached the end
        if coords != new_coords:
            return result


if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    with open("sample{0}.txt".format(part), "r") as file:
        print main(file.readlines())

    print "=== Real ==="
    with open("input.txt", "r") as file:
        print main(file.readlines())
