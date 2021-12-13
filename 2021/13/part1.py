def read_input():
    dots, instructions = [], []
    with open("input1.txt") as fp:
        parsing_part1 = True
        for line in fp:
            if line.strip() == "":
                parsing_part1 = False
                continue
            if parsing_part1:
                x, y = line.strip().split(",")
                x, y = int(x), int(y)
                dots.append((x, y))
            else:
                plane, value = line.strip().split()[-1].split("=")
                instructions.append((plane, int(value)))
    return dots, instructions


def foldup(dots, lineno):
    result = []

    for x, y in dots:
        if y < lineno:
            result.append((x, y))
        else:
            result.append((x, lineno - (y - lineno)))
    return result


def foldleft(dots, lineno):
    result = []

    for x, y in dots:
        if x < lineno:
            result.append((x, y))
        else:
            result.append((lineno - (x - lineno), y))
    return result


def print_dots(dots):
    max_x = max(dots, key=lambda item: item[0])[0]
    max_y = max(dots, key=lambda item: item[1])[1]
    output = ""
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in dots:
                output += "#"
            else:
                output += "."
        output += "\n"
    print(output)


if __name__ == "__main__":
    dots, instructions = read_input()


    direction, lineno = instructions[0]
    if direction == "x":
        dots = foldleft(dots, lineno)
    else:
        dots = foldup(dots, lineno)
    print(len(set(dots)))
