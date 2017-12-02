import sys
input_file = "input1.txt"
if len(sys.argv) > 1 and sys.argv[1].lower() in ["t", "--t", "test", "--test", "--check", "check"]:
    input_file = "sample1.txt"


with open(input_file, "r") as file:
    for line in file:
        line = line.strip()


