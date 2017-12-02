
with open("input2.txt", "r") as file:
    for line in file:
        line = line.strip()
        total = 0
        for i in range(len(line)):
            cur_n = int(line[i])
            next_n = int(line[(len(line)/2 + i) % len(line)])
            if cur_n == next_n:
                total += cur_n
        print "Answer ", total


