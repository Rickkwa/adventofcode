def read_input():
    result = []
    with open("input1.txt") as fp:
        for line in fp:
            result.append(line.strip())
    return result


if __name__ == "__main__":
    chunks = read_input()

    mapping = { '(': ')', '[': ']', '{': '}', '<': '>'}
    counter = { ')': 0, ']': 0, '}': 0, '>': 0}

    stack = []
    for line in chunks:
        for c in line:
            if c in ['(', '[', '{', '<']:
                stack.append(c)
            else:
                opening_bracket = stack.pop()
                if mapping[opening_bracket] != c:
                    counter[c] += 1
                    break


    score = counter[')'] * 3 + counter[']'] * 57 + counter['}'] * 1197 + counter['>'] * 25137
    print(score)
