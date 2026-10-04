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
            if self.conflict(solution):
                continue
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
                continue
            for col in range(self.size):
                queens = solution.copy()
                queens.append((row, col))
                stack.append(queens)
        return solutions
    def solve_bfs(self):
        if self.size < 1:
            return []
        solutions = []
        queue = Queue()
        queue.put([])
        while not queue.empty():
            solution = queue.get()
            if self.conflict(solution):
                continue
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
                continue
            for col in range(self.size):
                queens = solution.copy()
                queens.append((row, col))
                queue.put(queens)
        return solutions
    def conflict(self, queens):
        for i in range(1, len(queens)):
            for j in range(i):
                a, b = queens[i]
                c, d = queens[j]
                if a == c or b == d or abs(a - c) == abs(b - d):
                    return True
        return False
    def print_solution(self, queens):
        for i in range(self.size):
            print(' ---' * self.size)
            for j in range(self.size):
                cell = 'Q' if (i, j) in queens else ' '
                print(f'| {cell} ', end='')
            print('|')
        print(' ---' * self.size)
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