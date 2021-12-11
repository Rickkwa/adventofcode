from typing import List

class Octopus():
    def __init__(self, initial_energy):
        if not(0 <= initial_energy <= 9):
            raise Exception("Invalid initial energy. Should be in range [0, 9].")
        self.energy = initial_energy
        self.flash = False

    def step(self):
        if not self.flash:
            self.energy += 1
            if self.energy > 9:
                self.flash = True
                self.energy = 0

    def is_flashing(self):
        return self.flash

    def resolve_step(self):
        if self.flash:
            self.flash = False
            self.energy = 0

    def __str__(self):
        result = str(self.energy)
        if self.flash:
            result += "*"
        else:
            result += " "
        return result

    def __repr__(self):
        return f"Octopus({self.energy})"


class Cavern():
    def __init__(self, cavern_raw: List[List[int]]):
        self.cavern = []
        self.collen = 10
        self.rowlen = 10
        for row in cavern_raw:
            self.cavern.append([])
            for col in row:
                self.cavern[-1].append(Octopus(col))

    def start_step(self):
        """ Apply a step to every octopus in the cavern """
        queue = []

        # Put all 100 octo coords into queue
        for row in range(self.rowlen):
            for col in range(self.collen):
                queue.append((row, col))

        while len(queue) > 0:
            r, c = queue.pop(0)
            octo = self.cavern[r][c]
            if octo.is_flashing():
                continue
            octo.step()
            if octo.is_flashing():
                # Add neighbours to queue
                if r - 1 >= 0:  # up
                    queue.append((r - 1, c))
                if r + 1 < self.rowlen:  # down
                    queue.append((r + 1, c))
                if c - 1 >= 0:  # left
                    queue.append((r, c - 1))
                if c + 1 < self.collen:  # right
                    queue.append((r, c + 1))
                if r - 1 >= 0 and c - 1 >= 0:  # up-left
                    queue.append((r - 1, c - 1))
                if r - 1 >= 0 and c + 1 < self.collen:  # up-right
                    queue.append((r - 1, c + 1))
                if r + 1 < self.rowlen and c - 1 >= 0:  # down-left
                    queue.append((r + 1, c - 1))
                if r + 1 < self.rowlen and c + 1 < self.collen:  # down-right
                    queue.append((r + 1, c + 1))

    def end_step(self):
        for row in self.cavern:
            for col in row:
                col.resolve_step()

    def num_flashing(self) -> int:
        return sum([sum(list(map(lambda x: x.is_flashing(), row))) for row in self.cavern])

    def __str__(self) -> str:
        result = ""
        for row in self.cavern:
            result += " ".join(map(str, row))
            result += "\n"
        return result


def read_input() -> Cavern:
    result = []
    with open("input1.txt") as fp:
        for line in fp:
            result.append(list(map(int, list(line.strip()))))
    return Cavern(result)



if __name__ == "__main__":
    cavern_map = read_input()
    # print(str(cavern_map))

    turn = 1
    while True:
        cavern_map.start_step()
        if cavern_map.num_flashing() == 100:
            print(turn)
            break
        # print(f"Turn {turn}")
        # print(str(cavern_map))
        # print("")
        cavern_map.end_step()
        turn += 1
