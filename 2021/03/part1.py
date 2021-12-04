report = []

with open("input1.txt") as fp:
    for line in fp:
        report.append(line.strip())

gamma_rate = ''
epsilon_rate = ''

for col_n in range(len(report[0])):
    count_ones = 0
    count_zeroes = 0
    for bin_num in report:
        if bin_num[col_n] == '1':
            count_ones += 1
        else:
            count_zeroes += 1
    if count_ones > count_zeroes:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

print(gamma_rate, epsilon_rate)
print(int(gamma_rate, 2) * int(epsilon_rate, 2))
