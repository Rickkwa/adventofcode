import sys
import os

def main(fp):
    for line in fp:
        line = line.strip()



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    with open("sample{0}.txt".format(part), "r") as file:
        main(file)

    print "=== Real ==="
    with open("input{0}.txt".format(part), "r") as file:
        main(file)
