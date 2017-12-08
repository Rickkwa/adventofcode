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


class Node(object):
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []

    def __getitem__(self, index):
        return self.children[index]

    def __iter__(self):
        for child in self.children:
            yield child

    def __str__(self):
        return str(self.name)

    def __contains__(self, node):
        return node in self.children

    def contains_name(self, name):
        return name in map(lambda n: n.name, self.children)

    def children(self):
        return self.children

    def parent(self):
        return self.parent

    def add(self, node):
        self.children.append(node)
        node.parent = self

    def append(self, node):
        self.add(node)

    def is_leaf(self):
        return len(self.children) == 0

    def nested_str(self):
        result = ""
        q = [(self, 0)]
        while len(q) > 0:
            node, level = q.pop()
            result += "\n{0}{1}".format("-" * (level * 2), str(node))
            for child in node:
                q.append((child, level + 1))
        return result.strip()
