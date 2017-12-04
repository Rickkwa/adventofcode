import sys
import os

def check_anagram(passphrase):
    # Return true iff all words cannot be rearranged to form another word in the list
    words = passphrase[:]
    words_sorted = []
    for word in words:
        letters = list(word)
        letters.sort()
        words_sorted.append("".join(letters))
    return len(words_sorted) == len(set(words_sorted))


def main(fp):
    passphrases = []
    for line in fp:
        line = line.strip()
        passphrases.append(line.split())

    count = 0
    for phrase in passphrases:
        if len(phrase) == len(set(phrase)):
            if check_anagram(phrase):
                count += 1
    return count


if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    with open("sample{0}.txt".format(part), "r") as file:
        print main(file)

    print "=== Real ==="
    with open("input{0}.txt".format(part), "r") as file:
        print main(file)
