input_file = "input1.txt"

with open(input_file, "r") as file:
    checksum = 0
    for line in file:
        line = line.strip()
        row = line.split()
        largest = int(row[0])
        smallest = int(row[0])
        for n in row:
            n = int(n)
            if n > largest:
                largest = n
            if n < smallest:
                smallest = n
        #print largest, smallest
        checksum += largest - smallest
    print checksum

