def read_input():
    result = []
    with open("input1.txt") as fp:
        for line in fp:
            result.append(line.strip())
    return result


def discard_corrupted(chunks_list):
    result = []

    mapping = { '(': ')', '[': ']', '{': '}', '<': '>'}
    counter = { ')': 0, ']': 0, '}': 0, '>': 0}

    stack = []
    for line in chunks_list:
        corrupted = False
        for c in line:
            if c in ['(', '[', '{', '<']:
                stack.append(c)
            else:
                opening_bracket = stack.pop()
                if mapping[opening_bracket] != c:
                    corrupted = True
                    break
        if not corrupted:
            result.append(line)
    return result


def get_completion(chunks):
    result = ''

    mapping = { '(': ')', '[': ']', '{': '}', '<': '>'}

    while "()" in chunks or "[]" in chunks or "{}" in chunks or "<>" in chunks:
        chunks = chunks.replace("()", "")
        chunks = chunks.replace("[]", "")
        chunks = chunks.replace("{}", "")
        chunks = chunks.replace("<>", "")

    for c in chunks:
        result = mapping[c] + result
    # print(chunks, result)
    return result


if __name__ == "__main__":
    chunks_list = read_input()
    incomplete_chunks_list = discard_corrupted(chunks_list)

    score_value_mapping = {')': 1, ']': 2, '}': 3, '>': 4}
    scores_list = []
    for chunks in incomplete_chunks_list:
        completion = get_completion(chunks)
        score = 0
        for c in completion:
            score = score * 5
            score += score_value_mapping[c]
        scores_list.append(score)

    scores_list.sort()
    print(scores_list[len(scores_list) // 2])
