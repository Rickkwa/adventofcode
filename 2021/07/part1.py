def read_input():
    return list(map(int, open("input1.txt").read().split(",")))

if __name__ == "__main__":
    crabs = read_input()

    # Find the median to be the horizontal position?
    median = sorted(crabs)[len(crabs) // 2]
    print("Median", median)

    fuel_cost = 0
    for crab in crabs:
        fuel_cost += abs(crab - median)
    print(fuel_cost)
