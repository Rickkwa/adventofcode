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


def knot_hash(input_str, list_size=256):
    def process(lst, start_index, length):
        tmp_lst = lst[:] * ((length + start_index) / len(lst) + 1)
        sub_list = tmp_lst[start_index:start_index + length]
        sub_list.reverse()

        result = lst[:]
        index = start_index
        for i in range(length):
            result[index % len(result)] = sub_list[i]
            index += 1
        return result


    def get_dense(sparse):
        result = []
        for i in range(len(sparse) / 16):
            result.append(reduce(lambda x, y: x ^ y, sparse[i * 16: i * 16 + 16]))
        return result

    cur_pos = 0
    skip_size = 0
    sparse = range(0, list_size)
    for rnd in range(64):
        for n in map(lambda x: ord(x), list(input_str)) + [17, 31, 73, 47, 23]:
            n = int(n)
            sparse = process(sparse, cur_pos, n)
            cur_pos += n + skip_size
            cur_pos = cur_pos % list_size
            skip_size += 1

    dense = get_dense(sparse)
    return "".join(map(lambda x: format(x, 'x').zfill(2), dense))


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
