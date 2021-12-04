depth = 0
hpos = 0
aim = 0

with open("input1.txt") as fp:
    for line in fp:
        cmd, dist = line.strip().split(" ")
        dist = int(dist)

        if cmd == "up":
            aim -= dist
        elif cmd == "down":
            aim += dist
        elif cmd == "forward":
            hpos += dist
            depth += aim * dist
        else:
            raise Exception()

print(depth, hpos, aim)
print(depth * hpos)
