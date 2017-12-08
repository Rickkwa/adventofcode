import sys
import os
import math
sys.path.append('../../lib')
from aoc import *

def get_tree(inp):
    tree = {}
    for line in inp:
        if "->" in line:
            parent = line[0]
            children = map(lambda x: x.strip(","), line[line.index("->") + 1:])
            tree[parent] = children
    return tree

def get_weights(words):
    result = {}
    for word in words:
        weight = int(word[1].strip("()"))
        result[word[0]] = weight
    return result

def get_bottom(inp):
    candidate = {}
    for line in inp:
        if "->" in line:
            parent = line[0].split()[0]
            candidate[parent] = candidate.get(parent, 0)
            children = map(lambda x: x.strip(","), line[line.index("->") + 1:])
            for c in children:
                candidate[c] = candidate.get(c, 0) + 1
    for key, value in candidate.iteritems():
        if value == 0:
            return key

def calc_weight(tree, node, weights, dp):
    # Return weight of itself + all it's children

    if node in dp:
        return dp[node]

    if node not in tree:
        dp[node] = weights[node]
        return weights[node]

    result = weights[node]
    for child in tree[node]:
        weight = calc_weight(tree, child, weights, dp)
        if child not in dp:
            dp[child] = weight
        result += weight
    return result

def find_imbalanced_child(tree, node, final_weights):
    # Find the child with a different weight
    answers = {}
    for child in tree[node]:
        weight = final_weights[child]
        answers[weight] = answers.get(weight, [])
        answers[weight].append(child)
    for key, value in answers.iteritems():
        if len(value) == 1:
            return value[0]
    return None


def main(inp):
    weights_dp = {}
    weights = get_weights(inp[:])
    tree = get_tree(inp[:])
    bottom = get_bottom(inp[:])

    calculated_weights = {}
    for node in weights.keys():
        calculated_weights[node] = calc_weight(tree, node, weights, weights_dp)

    diff = []
    for child in tree[bottom]:
        print child, calculated_weights[child]
        diff.append(calculated_weights[child])
    diff = max(diff) - min(diff)

    # print "===S"
    # for child in tree["fabacam"]:
    #     print child, calculated_weights[child]
    # print "===E"

    node = bottom
    while find_imbalanced_child(tree, node, calculated_weights) != None:
        node = find_imbalanced_child(tree, node, calculated_weights)
    print "Imbalance:", node, weights[node], weights[node] - diff

    return weights[node] - diff



if __name__ == "__main__":
    part = '1' if os.path.basename(__file__).endswith("1.py") else '2'

    # read_lines, read_words, read_ints, read_int_list

    print "=== Part {0} ===".format(part)
    print "=== Test ==="
    print main(read_words("sample{0}.txt".format(part)))

    print "=== Real ==="
    print main(read_words("input{0}.txt".format(part)))
