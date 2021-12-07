class Fish():
    def __init__(self, timer=8):
        self.timer = timer

    def next_day(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            return Fish(8)
        return None

    def __str__(self):
        return str(self.timer)


def read_input():
    result = []
    with open("input1.txt") as fp:
        nums = list(map(int, fp.readlines()[0].split(",")))
    for n in nums:
        result.append(Fish(n))
    return result


if __name__ == "__main__":
    fishes = read_input()

    for day in range(80):
        for fish in fishes.copy():
            new_fish = fish.next_day()
            if new_fish is not None:
                fishes.append(new_fish)
    print(len(fishes))
