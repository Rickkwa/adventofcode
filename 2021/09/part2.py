def read_input():
    result = []
    with open("input1.txt") as fp:
        for line in fp:
            result.append(list(map(int, list(line.strip()))))
    return result


def calculate_low_points(area):
    """ Return a 2D list of booleans corresponding to the `area` 2D list. True = low point. """
    result = [[False] * len(row) for row in area]
    for r in range(len(area)):
        for c in range(len(area[r])):
            low_point = True
            # Check up
            if r - 1 >= 0 and area[r - 1][c] <= area[r][c]:
                low_point = False
            # Check down
            if r + 1 < len(area) and area[r + 1][c] <= area[r][c]:
                low_point = False
            # Check right
            if c + 1 < len(area[r]) and area[r][c + 1] <= area[r][c]:
                low_point = False
            # Check left
            if c - 1 >= 0 and area[r][c - 1] <= area[r][c]:
                low_point = False
            if low_point:
                result[r][c] = True
    return result


def get_basin_size(area, visited, r, c):
    visited[(r, c)] = True
    total = 1
    # Check up
    if r - 1 >= 0 and area[r - 1][c] > area[r][c] and area[r - 1][c] < 9 and not visited.get((r - 1, c), False):
        val = get_basin_size(area, visited, r - 1, c)
        total += val
    # Check down
    if r + 1 < len(area) and area[r + 1][c] > area[r][c] and area[r + 1][c] < 9 and not visited.get((r + 1, c), False):
        val = get_basin_size(area, visited, r + 1, c)
        total += val
    # Check right
    if c + 1 < len(area[r]) and area[r][c + 1] > area[r][c] and area[r][c + 1] < 9 and not visited.get((r, c + 1), False):
        val = get_basin_size(area, visited, r, c + 1)
        total += val
    # Check left
    if c - 1 >= 0 and area[r][c - 1] > area[r][c] and area[r][c - 1] < 9 and not visited.get((r, c - 1), False):
        val = get_basin_size(area, visited, r, c - 1)
        total += val
    return total


if __name__ == "__main__":
    area = read_input()
    low_point_map = calculate_low_points(area)

    basin_sizes = []
    for r in range(len(area)):
        for c in range(len(area[r])):
            if low_point_map[r][c]:
                basin_sizes.append(get_basin_size(area, {}, r, c))
    print(basin_sizes)
    basin_sizes.sort(reverse=True)
    print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
