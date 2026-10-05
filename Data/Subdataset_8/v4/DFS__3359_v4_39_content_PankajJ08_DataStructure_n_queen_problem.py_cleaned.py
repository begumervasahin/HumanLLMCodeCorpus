
QUEEN = "\u265B"
N = 8
solution_number = 1
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == QUEEN:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == QUEEN:
            return False
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == QUEEN:
            return False
    return True
def find_all_solutions(board, col):
    global solution_number
    if col >= N:
        print("Solution", solution_number, ": ")
        for i in range(N):
            for j in range(N):
                print(board[i][j], end="  ")
            print()
        print()
        solution_number += 1
        return True
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = QUEEN
            if find_all_solutions(board, col + 1):
                return True
            board[i][col] = '_'
    return False
def n_queen():
    board = [['_' for _ in range(N)] for _ in range(N)]
    if not find_all_solutions(board, 0):
        print("No solution exists!")
if __name__ == '__main__':
    n_queen()