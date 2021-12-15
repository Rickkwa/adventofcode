from collections import Counter

def read_input():
    pair_insertions = []
    with open("input1.txt") as fp:
        template = fp.readline().strip()
        for line in fp:
            if line.strip() == "":
                continue
            pair, _, insertion = line.strip().split(" ")
            pair_insertions.append((pair, insertion))
    return template, pair_insertions


def turn(template: str, pair_insertions: list) -> str:
    result = ''
    pairs = list(map(lambda x: x[0], pair_insertions))
    insertions = list(map(lambda x: x[1], pair_insertions))
    for i in range(0, len(template) - 1):
        try:
            index = pairs.index(template[i: i + 2])
            result += template[i] + insertions[index]
        except:
            result += template[i]
    result += template[-1]
    return result


if __name__ == "__main__":
    template, pair_insertions = read_input()
    for _ in range(10):
        template = turn(template, pair_insertions)

    counter = Counter(template)
    print(counter.most_common())
    print(counter.most_common()[0][1] - counter.most_common()[-1][1])
