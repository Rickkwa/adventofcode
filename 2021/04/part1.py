class Board():
    def __init__(self, board_2dlist):
        self.board = board_2dlist
        self.marks = [[0] * len(row) for row in self.board]
        self.matching_numbers = []


    def is_winner(self):
        for row in self.marks:
            if sum(row) == len(row):
                return True
        for row in list(zip(*self.marks)):
            if sum(row) == len(row):
                return True
        return False

    def mark_number(self, n):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == n:
                    self.marks[i][j] = 1
                    self.matching_numbers.append(n)

    def __str__(self):
        result = ''
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                result += str(self.board[i][j])
                if self.marks[i][j] == 1:
                    result += "*"
                result += " "
            result += '\n'
        return result


    def sum_unmarked(self):
        result = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.marks[i][j] == 0:
                    result += self.board[i][j]
        return result

    def winning_number(self):
        return self.matching_numbers[-1]


def read_input():
    with open("input1.txt") as fp:
        # Read called out bingo numbers
        numbers = [int(x) for x in fp.readline().strip().split(",")]

        # Read bingo boards
        boards = []
        board = []
        for line in fp:
            if line.strip() == "":
                if board != []:
                    boards.append(Board(board))
                    board = []
                continue
            nums = [int(x) for x in line.strip().split()]
            board.append(nums)
        boards.append(Board(board))

    return numbers, boards


def get_winner(numbers, boards):
    for n in numbers:
        for board in boards:
            board.mark_number(n)
            if board.is_winner():
                return board
    return None



if __name__ == "__main__":
    call_numbers, bingo_boards = read_input()
    winning_board = get_winner(call_numbers, bingo_boards)
    print(winning_board)
    print(winning_board.winning_number())
    print(winning_board.sum_unmarked() * winning_board.winning_number())
