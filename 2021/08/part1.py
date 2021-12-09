def read_input():
    result = []
    with open("input1.txt") as fp:
        for line in fp:
            signal_patterns = line.split("|")[0].strip().split(" ")
            digits = line.split("|")[1].strip().split(" ")
            result.append((signal_patterns, digits))
    return result


if __name__ == "__main__":
    entries = read_input()
    count = 0
    for signal_patterns, digits in entries:
        digits_length = list(map(len, digits))

        # 1 = 2 segs, 4 = 4 segs, 7 = 3 segs, 8 = 7 segs
        count += digits_length.count(2) + digits_length.count(4) + digits_length.count(3) + digits_length.count(7)
    print(count)
