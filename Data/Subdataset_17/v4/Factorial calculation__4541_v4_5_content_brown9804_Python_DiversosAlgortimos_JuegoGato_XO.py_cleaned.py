def create_matrix(rows, cols):
    return [["-" for _ in range(cols)] for _ in range(rows)]
def is_cell_free(matrix, row, col):
    return matrix[row][col] == "-"
def is_cell_valid(row, col, size):
    return 0 <= row < size and 0 <= col < size
def display_matrix(matrix):
    for row in matrix:
        print("\t".join(row))
    print()
def assign_move(matrix, row, col, player):
    marker = "X" if player == 1 else "O"
    matrix[row][col] = marker
def check_rows(matrix, marker):
    return any(all(cell == marker for cell in row) for row in matrix)
def check_columns(matrix, marker):
    size = len(matrix)
    return any(all(matrix[row][col] == marker for row in range(size)) for col in range(size))
def check_diagonals(matrix, marker):
    size = len(matrix)
    diagonal1 = all(matrix[i][i] == marker for i in range(size))
    diagonal2 = all(matrix[i][size - 1 - i] == marker for i in range(size))
    return diagonal1 or diagonal2
def check_winner(matrix, player):
    marker = "X" if player == 1 else "O"
    return (check_rows(matrix, marker) or
            check_columns(matrix, marker) or
            check_diagonals(matrix, marker))
def get_move(matrix, player):
    while True:
        try:
            print(f"\nPlayer {player}'s turn")
            row = int(input("Enter the row index (0, 1, 2): "))
            col = int(input("Enter the column index (0, 1, 2): "))
            if is_cell_valid(row, col, len(matrix)) and is_cell_free(matrix, row, col):
                assign_move(matrix, row, col, player)
                return check_winner(matrix, player)
            else:
                print("Invalid or occupied cell, please try again.")
        except ValueError:
            print("Invalid input. Please enter integers for row and column.")
def main():
    size = 3
    matrix = create_matrix(size, size)
    total_moves = 0
    current_player = 1
    while total_moves < size * size:
        display_matrix(matrix)
        if get_move(matrix, current_player):
            display_matrix(matrix)
            print(f"Congratulations! Player {current_player} wins!")
            return
        total_moves += 1
        current_player = 2 if current_player == 1 else 1
    display_matrix(matrix)
    print("The game is a draw!")
if __name__ == "__main__":
    main()