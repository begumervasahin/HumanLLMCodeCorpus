from utils import grid_values, search, display
def solve_sudoku(puzzle: str):
    values = grid_values(puzzle)
    solution = search(values)
    display(solution)
def main():
    puzzle = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
    solve_sudoku(puzzle)
if __name__ == "__main__":
    main()