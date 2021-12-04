count = 0
last_value = None

with open("input.txt") as fp:
    for line in fp:
        if last_value is not None:
            if int(line) > last_value:
                count += 1
        last_value = int(line)

print(count)
