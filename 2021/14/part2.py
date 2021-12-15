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


def turn(counter: Counter, overlap_counter: Counter, pair_insertions: list) -> str:
    pairs = list(map(lambda x: x[0], pair_insertions))
    insertions = list(map(lambda x: x[1], pair_insertions))
    counter_clone = counter.copy()
    for pair, insertion in pair_insertions:
        if counter_clone.get(pair, 0) <= 0:
            continue
        counter[pair] -= counter_clone[pair]
        counter[pair[0] + insertion] += counter_clone[pair]
        counter[insertion + pair[1]] += counter_clone[pair]
        overlap_counter[insertion] += counter_clone[pair]


if __name__ == "__main__":
    template, pair_insertions = read_input()
    pairs_counter = Counter()
    overlap_counter = Counter()

    for i in range(0, len(template) - 1):
        pairs_counter[template[i: i + 2]] += 1
        if i != len(template) - 2:
            overlap_counter[template[i + 1]] += 1

    for i in range(40):
        turn(pairs_counter, overlap_counter, pair_insertions)

    alphabet_counter = Counter()
    for pair, count in pairs_counter.items():
        alphabet_counter[pair[0]] += count
        alphabet_counter[pair[1]] += count
    alphabet_counter.subtract(overlap_counter)
    print(alphabet_counter.most_common()[0][1] - alphabet_counter.most_common()[-1][1])

