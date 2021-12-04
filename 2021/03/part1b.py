report = []

with open("input1.txt") as fp:
    for line in fp:
        report.append(list(line.strip()))
transpose_report = list(zip(*report))

gamma_rate = "".join([('1' if x.count('1') > x.count('0') else '0') for x in transpose_report])
epsilon_rate = "".join([('0' if x.count('1') > x.count('0') else '1') for x in transpose_report])

print(gamma_rate, epsilon_rate)
print(int(gamma_rate, 2) * int(epsilon_rate, 2))
