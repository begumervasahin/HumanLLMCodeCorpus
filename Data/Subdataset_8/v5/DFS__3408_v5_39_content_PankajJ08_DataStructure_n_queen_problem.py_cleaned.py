
QUEEN = "\u265B"
BOARD_SIZE = 8
solution_count = 1
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == QUEEN:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == QUEEN:
            return False
    for i, j in zip(range(row, BOARD_SIZE), range(col, -1, -1)):
        if board[i][j] == QUEEN:
            return False
    return True
def find_all_solutions(board, col):
    global solution_count
    if col >= BOARD_SIZE:
        print("Solution", solution_count, ": ")
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                print(board[i][j], end="  ")
            print()
        print()
        solution_count += 1
        return True
    for i in range(BOARD_SIZE):
        if is_safe(board, i, col):
            board[i][col] = QUEEN
            if find_all_solutions(board, col + 1):
                return True
            board[i][col] = '_'
    return False
def n_queen():
    board = [['_'] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    if not find_all_solutions(board, 0):
        print("No solution exists!")
if __name__ == '__main__':
    n_queen()