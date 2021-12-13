def read_input():
    result = {}
    with open("input1.txt") as fp:
        for line in fp:
            left = line.strip().split("-")[0]
            right = line.strip().split("-")[1]
            if right not in result.get(left, []):
                result[left] = result.get(left, []) + [right]
            if left not in result.get(right, []):
                result[right] = result.get(right, []) + [left]
    return result


def count_paths_start_to_end(current_node, cave_map, visited=[]):
    if current_node == "end":
        return 1

    count = 0
    for neighbour in cave_map[current_node]:
        if neighbour == "start":
            continue
        if neighbour == neighbour.lower() and neighbour not in visited or neighbour == neighbour.upper():
            count += count_paths_start_to_end(neighbour, cave_map, visited + [neighbour])

    visited.append(current_node)
    return count


if __name__ == "__main__":
    cave_map = read_input()
    print(count_paths_start_to_end("start", cave_map))
