def read_input():
    return list(map(int, open("input1.txt").read().split(",")))

if __name__ == "__main__":
    crabs = read_input()

    min_fuel_cost = None
    min_fuel_pos = None
    for i in range(max(crabs) + 1):
        fuel_cost = 0
        for crab in crabs:
            n = abs(i - crab)
            fuel_cost += (n**2 + n) // 2
        if min_fuel_cost is None:
            min_fuel_cost = fuel_cost
            min_fuel_pos = i
        elif fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
            min_fuel_pos = i
    print(min_fuel_pos)
    print(min_fuel_cost)
