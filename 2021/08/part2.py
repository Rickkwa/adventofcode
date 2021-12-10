def read_input():
    result = []
    with open("input1.txt") as fp:
        for line in fp:
            signal_patterns = line.split("|")[0].strip().split(" ")
            digits = line.split("|")[1].strip().split(" ")
            result.append((signal_patterns, digits))
    return result


class Helper():
    MAPPING = {
        0: ['a', 'b', 'c', 'e', 'f', 'g'],
        1: ['c', 'f'],
        2: ['a', 'c', 'd', 'e', 'g'],
        3: ['a', 'c', 'd', 'f', 'g'],
        4: ['b', 'c', 'd', 'f'],
        5: ['a', 'b', 'd', 'f', 'g'],
        6: ['a', 'b', 'd', 'e', 'f', 'g'],
        7: ['a', 'c', 'f'],
        8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
        9: ['a', 'b', 'c', 'd', 'f', 'g']
    }

    def x_in_y(self, x: int, y: int) -> bool:
        """ Is the number x a subset of y in terms of a seven-segment display. Eg, 1 is a subset of 3 since the display for 3 includes the 2 vertical segments that make up the display for 1. """
        return len(set(self.MAPPING[x] + self.MAPPING[y])) == len(self.MAPPING[y])

    def num_of_segs(self, n: int):
        return len(self.MAPPING[n])

    def seg_x_in_y(self, x: str, y: str) -> bool:
        """ Are the segments of x a subset of the segments in y? Eg. is 'be' a subset of 'cefdb' """
        return len(set(x + y)) == len(y)

    def seg_eq(self, x: str, y: str) -> bool:
        return set(x) == set(y)


def calculate(signal_patterns, digits) -> int:
    """ Return the 4 digit number as a single int """

    def update_candidates():
        # Remove all known answers from all candidates
        for i in range(len(candidates)):
            for v in answers:
                try:
                    candidates[i].remove(v)
                except:
                    pass

    helper = Helper()
    answers = [None] * 10

    # Set a list of candidate answers for each unknown digit
    # Start with all 10 signal_patterns and eliminate all the ones whose length doesn't match the digit
    candidates = [list(filter(lambda x: len(x) == helper.num_of_segs(i), signal_patterns)) for i in range(10)]
    update_candidates()

    for _ in range(100):
        unknowns = [k for k, v in enumerate(answers) if v is None]
        knowns = [k for k, v in enumerate(answers) if v is not None]
        if len(unknowns) == 0:
            break
        # For every digit we still need to solve, compare it to the digits we already know the answers to
        # See if the unknown digit is a "subset" of the known digit(s), and if it is, then the segments should also be a subset.
        # Vice versa if the unknown digit is a "superset" of the known digit(s), then similarly the segments should be as well.
        for unknown_n in unknowns:
            for known_n in knowns:
                if helper.x_in_y(known_n, unknown_n):
                    # Then we expect segments in answers[known_n] to be a subset of segments in unknown_n
                    # Remove candidates from unknown_n where that isn't the case
                    candidates[unknown_n] = list(filter(lambda el: helper.seg_x_in_y(answers[known_n], el), candidates[unknown_n]))
                if helper.x_in_y(unknown_n, known_n):
                    # Then we expect candidates in unknown_n to be a subset of segments in answers[known_n]
                    # Remove candidates from unknown_n where that isn't the case
                    candidates[unknown_n] = list(filter(lambda el: helper.seg_x_in_y(el, answers[known_n]), candidates[unknown_n]))

            # If candidates for unknown_n is only one element, set the answer. If zero, then raise exception.
            if len(candidates[unknown_n]) == 0:
                raise Exception(f"There are no candidate answers for {unknown_n}")
            elif len(candidates[unknown_n]) == 1:
                answers[unknown_n] = candidates[unknown_n][0]
                update_candidates()

    answers = ["".join(sorted(x)) for x in answers]
    digits = ["".join(sorted(x)) for x in digits]

    return int(answers.index(digits[0])) * 1000 + \
           int(answers.index(digits[1])) * 100 + \
           int(answers.index(digits[2])) * 10 + \
           int(answers.index(digits[3]))


if __name__ == "__main__":
    entries = read_input()

    total = 0
    for signal_patterns, digits in entries:
        total += calculate(signal_patterns, digits)
    print(total)
