def read_lines(filepath):
    # Read the file and return a list of stripped lines
    with open(filepath, "r") as file:
        return map(lambda s: s.strip(), file.readlines())


def read_words(filepath, delim=None):
    # Read the file and return a list of lines split by the given character
    with open(filepath, "r") as file:
        return map(lambda s: s.strip().split(delim), file.readlines())


def read_ints(filepath):
    # Read the file and return a list of lines, split by space and casted to int
    with open(filepath, "r") as file:
        return map(lambda s: map(lambda x: int(x), list(s.split())), file.readlines())


def read_int_list(filepath):
    # The input file should contain a single int on each line. Return a list of ints.
    with open(filepath, "r") as file:
        return map(lambda s: int(s.strip()), file.readlines())

