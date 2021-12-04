def read_input():
    result = []
    with open("input1.txt") as fp:
        for line in fp:
            result.append(line.strip())
    return result


def most_common_bit(report, col_n):
    """ Return the most common bit in the nth column, or -1 if equal """
    count = 0
    for bin_n in report:
        if bin_n[col_n] == '1':
            count += 1
        else:
            count -= 1
    if count > 0:
        return 1
    elif count < 0:
        return 0
    return -1


def get_oxygen_generator_rating_bin(report, col):
    if len(report) == 1:
        return report[0]

    remaining_report = []

    popular_bit = most_common_bit(report, col)
    for bin_n in report:
        if bin_n[col] == str(popular_bit) or (popular_bit == -1 and bin_n[col] == '1'):
            remaining_report.append(bin_n)
    return get_oxygen_generator_rating_bin(remaining_report, col + 1)


def get_co2_generator_rating_bin(report, col):
    if len(report) == 1:
        return report[0]

    remaining_report = []

    popular_bit = most_common_bit(report, col)
    if popular_bit == -1:
        unpopular_bit = -1
    else:
        unpopular_bit = 1 - popular_bit
    for bin_n in report:
        if bin_n[col] == str(unpopular_bit) or (unpopular_bit == -1 and bin_n[col] == '0'):
            remaining_report.append(bin_n)
    return get_co2_generator_rating_bin(remaining_report, col + 1)


if __name__ == "__main__":
    diag_report = read_input()
    oxy_rating = int(get_oxygen_generator_rating_bin(diag_report, 0), 2)
    co2_rating = int(get_co2_generator_rating_bin(diag_report, 0), 2)
    print(oxy_rating, co2_rating)
    print(oxy_rating * co2_rating)
