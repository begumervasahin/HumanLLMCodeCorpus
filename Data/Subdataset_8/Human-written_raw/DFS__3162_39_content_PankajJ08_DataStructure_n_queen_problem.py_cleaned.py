
QUEEN = "\u265B"
N = 8
x = 1
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == QUEEN:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == QUEEN:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == QUEEN:
            return False
    return True
def n_queen_solution(board, col):
    res = False
    global x
    if col >= N:
        print(x, ": ")
        for i in range(N):
            for j in range(N):
                print(board[i][j], end="  ")
            print()
        print()
        x += 1
        return True
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = QUEEN
            res = n_queen_solution(board, col + 1) or res
            board[i][col] = '_'
    return res
def n_queen():
    board = [['_' for _ in range(N)] for _ in range(N)]
    y = n_queen_solution(board, 0)
    if not y:
        print("No solution exist!")
if __name__ == '__main__':
    n_queen()