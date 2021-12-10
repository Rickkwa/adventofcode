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


if __name__ == "__main__":
    area = read_input()
    low_point_map = calculate_low_points(area)

    risk_level_sum = 0
    for r in range(len(area)):
        for c in range(len(area[r])):
            if low_point_map[r][c]:
                risk_level_sum += area[r][c] + 1
    print(risk_level_sum)
