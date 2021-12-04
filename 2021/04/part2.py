class Board():
    def __init__(self, board_2dlist):
        self.board = board_2dlist
        self.marks = [[0] * len(row) for row in self.board]


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


def get_worst_winner(numbers, boards):
    winners = []
    winners_n = []
    for n in numbers:
        for board in boards:
            if board in winners:
                continue
            board.mark_number(n)
            if board.is_winner():
                winners.append(board)
                winners_n.append(n)
    return winners_n[-1], winners[-1]



if __name__ == "__main__":
    call_numbers, bingo_boards = read_input()
    winning_number, worst_board = get_worst_winner(call_numbers, bingo_boards)
    print(winning_number)
    print(worst_board)
    print(winning_number * worst_board.sum_unmarked())
