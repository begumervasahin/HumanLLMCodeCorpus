from queue import Queue
class NQueens:
    def __init__(self, size):
        self.size = size
    def solve_dfs(self):
        if self.size < 1:
            return []
        solutions = []
        stack = [[]]
        while stack:
            solution = stack.pop()
            if self.has_conflict(solution):
                continue
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
            else:
                for col in range(self.size):
                    new_solution = solution.copy()
                    new_solution.append((row, col))
                    stack.append(new_solution)
        return solutions
    def solve_bfs(self):
        if self.size < 1:
            return []
        solutions = []
        queue = Queue()
        queue.put([])
        while not queue.empty():
            solution = queue.get()
            if self.has_conflict(solution):
                continue
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
            else:
                for col in range(self.size):
                    new_solution = solution.copy()
                    new_solution.append((row, col))
                    queue.put(new_solution)
        return solutions
    def has_conflict(self, queens):
        for i in range(len(queens)):
            for j in range(i):
                (row1, col1) = queens[i]
                (row2, col2) = queens[j]
                if col1 == col2 or abs(row1 - row2) == abs(col1 - col2):
                    return True
        return False
    def print_solution(self, queens):
        board = [[" " for _ in range(self.size)] for _ in range(self.size)]
        for (row, col) in queens:
            board[row][col] = "Q"
        for row in board:
            print(" ---" * self.size)
            print("| " + " | ".join(row) + " |")
        print(" ---" * self.size)
if __name__ == "__main__":
    n = 8
    n_queens = NQueens(n)
    print("Solving N-Queens using DFS:")
    solutions_dfs = n_queens.solve_dfs()
    print(f"Number of solutions found: {len(solutions_dfs)}")
    for solution in solutions_dfs:
        n_queens.print_solution(solution)
        print()
    print("Solving N-Queens using BFS:")
    solutions_bfs = n_queens.solve_bfs()
    print(f"Number of solutions found: {len(solutions_bfs)}")
    for solution in solutions_bfs:
        n_queens.print_solution(solution)
        print()