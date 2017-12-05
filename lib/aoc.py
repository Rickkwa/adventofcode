def read_lines(filepath):
    # Read the file and return a list of stripped lines
    result = []
    with open(filepath, "r") as file:
        for line in file:
            result.append(line.strip())
    return result

def read_words(filepath, delim=None):
    # Read the file and return a list of lines split by the given character
    result = []
    with open(filepath, "r") as file:
        for line in file:
            result.append(line.strip().split(delim))
    return result

def read_ints(filepath):
    # Read the file and return a list of lines, split by space and casted to int
    result = []
    with open(filepath, "r") as file:
        for line in file:
            result.append(map(lambda x: int(x), line.strip().split()))
    return result
