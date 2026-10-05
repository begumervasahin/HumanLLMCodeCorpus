
QUEEN = "\u265B"
N = 8
solution_count = 1
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
    global solution_count
    if col >= N:
        print("Solution", solution_count, ": ")
        for i in range(N):
            for j in range(N):
                print(board[i][j], end="  ")
            print()
        print()
        solution_count += 1
        return True
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = QUEEN
            if n_queen_solution(board, col + 1):
                return True
            board[i][col] = '_'
    return False
def n_queen():
    board = [['_' for _ in range(N)] for _ in range(N)]
    if not n_queen_solution(board, 0):
        print("No solution exists!")
if __name__ == '__main__':
    n_queen()