def read_input():
    with open("input1.txt") as fp:
        nums = list(map(int, fp.readlines()[0].split(",")))
    return nums


if __name__ == "__main__":
    fish_timers = read_input()

    fish_counter = [0] * 9  # Split into buckets based on timers
    for fish in fish_timers:
        fish_counter[fish] += 1

    DAYS = 256

    for day in range(DAYS):
        fish_counter_orig = fish_counter.copy()
        fish_counter[0] = fish_counter_orig[1]
        fish_counter[1] = fish_counter_orig[2]
        fish_counter[2] = fish_counter_orig[3]
        fish_counter[3] = fish_counter_orig[4]
        fish_counter[4] = fish_counter_orig[5]
        fish_counter[5] = fish_counter_orig[6]
        fish_counter[6] = fish_counter_orig[7] + fish_counter_orig[0]
        fish_counter[7] = fish_counter_orig[8]
        fish_counter[8] = fish_counter_orig[0]
        # print(fish_counter)

    print(sum(fish_counter))
