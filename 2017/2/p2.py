input_file = "input2.txt"

with open(input_file, "r") as file:
    result = 0
    for line in file:
        line = line.strip()
        row = map(lambda x: int(x), line.split())
        for i in row:
            for j in row:
                if i % j == 0 and i != j:
                    result += i / j
    print result
