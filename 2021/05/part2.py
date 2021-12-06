def read_input():
    result = []
    with open("input1.txt") as fp:
        for line in fp:
            p1, p2 = line.split()[0], line.split()[-1]
            p1_coords = tuple(map(int, p1.split(",")))
            p2_coords = tuple(map(int, p2.split(",")))
            result.append((p1_coords, p2_coords))
    return result

if __name__ == "__main__":
    lines = read_input()
    max_x = 0
    max_y = 0
    for p1, p2 in lines:
        max_x = max(max_x, max(p1[0], p2[0]))
        max_y = max(max_y, max(p1[1], p2[1]))
    max_x += 1
    max_y += 1

    floor = [[0] * max_y for i in range(max_x)]

    for p1, p2 in lines:
        x1, y1 = p1
        x2, y2 = p2

        if y1 == y2:
            y_dir = 0
            x_dir = 1 if x2 > x1 else -1
            dist = max(x1, x2) - min(x1, x2)
        elif x1 == x2:
            x_dir = 0
            y_dir = 1 if y2 > y1 else -1
            dist = max(y1, y2) - min(y1, y2)
        else:
            x_dir = 1 if x2 > x1 else -1
            y_dir = 1 if y2 > y1 else -1
            dist = max(x1, x2) - min(x1, x2)  # either x or y yields same result for diag case

        x, y = x1, y1
        for i in range(dist + 1):
            floor[x][y] += 1
            x += x_dir
            y += y_dir

    # print("\n".join([" ".join(map(str, row)) for row in floor]))

    count = 0
    for i in range(max_x):
        for j in range(max_y):
            if floor[i][j] > 1:
                count += 1
    print(count)
