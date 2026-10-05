def create_board(rows, cols):
    board = [["-" for _ in range(cols)] for _ in range(rows)]
    return board
def is_free_cell(board, row, col):
    return board[row][col] == "-"
def is_valid_cell(row, col):
    return 0 <= row < 3 and 0 <= col < 3
def display_board(board):
    for row in board:
        print("   ".join(row))
        print()
def make_move(board, row, col, player):
    mark = "X" if player == 1 else "O"
    board[row][col] = mark
def check_rows(board, mark):
    for row in board:
        if all(cell == mark for cell in row):
            return True
    return False
def check_columns(board, mark):
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True
    return False
def check_diagonals(board, mark):
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False
def check_winner(board, player):
    mark = "X" if player == 1 else "O"
    return check_rows(board, mark) or check_columns(board, mark) or check_diagonals(board, mark)
def read_move(board, player):
    while True:
        print(f"\nPlayer {player}'s turn")
        row = int(input("Enter the row (0, 1, 2): "))
        col = int(input("Enter the column (0, 1, 2): "))
        if is_valid_cell(row, col) and is_free_cell(board, row, col):
            return row, col
        else:
            print("Invalid move! Please try again.")
def play_game():
    board = create_board(3, 3)
    display_board(board)
    current_player = 1
    for _ in range(9):
        row, col = read_move(board, current_player)
        make_move(board, row, col, current_player)
        display_board(board)
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            return
        current_player = 2 if current_player == 1 else 1
    print("It's a draw!")
if __name__ == "__main__":
    play_game()