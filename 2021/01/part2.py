def read_input():
    numbers = []
    with open("input.txt") as fp:
        for line in fp:
            numbers.append(int(line.strip()))
    return numbers


def create_three_measurement_sums(nums):
    result = []
    try:
        for i in range(len(nums)):
            a, b, c = nums[i], nums[i + 1], nums[i + 2]
            result.append(a + b + c)
    except IndexError:
        return result
    return result


if __name__ == "__main__":
    numbers = read_input()
    tmw_sums = create_three_measurement_sums(numbers)

    count = 0
    last_value = None

    for val in tmw_sums:
        if last_value is not None:
            if val > last_value:
                count += 1
        last_value = val
    print(count)
