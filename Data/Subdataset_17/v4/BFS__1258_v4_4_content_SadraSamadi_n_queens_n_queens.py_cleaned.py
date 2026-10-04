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
                queen = (row, col)
                queens = solution.copy()
                queens.append(queen)
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
                queen = (row, col)
                queens = solution.copy()
                queens.append(queen)
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
    def print_board(self, queens):
        for i in range(self.size):
            print(' ---' * self.size)
            for j in range(self.size):
                p = 'Q' if (i, j) in queens else ' '
                print('| %s ' % p, end='')
            print('|')
        print(' ---' * self.size)
if __name__ == "__main__":
    n = 8
    nqueens = NQueens(n)
    solutions_dfs = nqueens.solve_dfs()
    solutions_bfs = nqueens.solve_bfs()
    print(f"Number of solutions using DFS: {len(solutions_dfs)}")
    print(f"Number of solutions using BFS: {len(solutions_bfs)}")
    if solutions_dfs:
        print("One of the solutions using DFS:")
        nqueens.print_board(solutions_dfs[0])
    if solutions_bfs:
        print("One of the solutions using BFS:")
        nqueens.print_board(solutions_bfs[0])