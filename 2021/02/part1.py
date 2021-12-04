depth = 0
hpos = 0

with open("input1.txt") as fp:
    for line in fp:
        cmd, dist = line.strip().split(" ")
        dist = int(dist)

        if cmd == "up":
            depth -= dist
        elif cmd == "down":
            depth += dist
        elif cmd == "forward":
            hpos += dist
        else:
            raise Exception()

print(depth, hpos)
print(depth * hpos)
