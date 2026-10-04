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
            if self._has_conflict(solution):
                continue
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
                continue
            for col in range(self.size):
                queen = (row, col)
                stack.append(solution + [queen])
        return solutions
    def solve_bfs(self):
        if self.size < 1:
            return []
        solutions = []
        queue = Queue()
        queue.put([])
        while not queue.empty():
            solution = queue.get()
            if self._has_conflict(solution):
                continue
            row = len(solution)
            if row == self.size:
                solutions.append(solution)
                continue
            for col in range(self.size):
                queen = (row, col)
                queue.put(solution + [queen])
        return solutions
    def _has_conflict(self, queens):
        for i in range(len(queens)):
            for j in range(i):
                if self._is_conflict(queens[i], queens[j]):
                    return True
        return False
    def _is_conflict(self, queen1, queen2):
        row1, col1 = queen1
        row2, col2 = queen2
        return row1 == row2 or col1 == col2 or abs(row1 - row2) == abs(col1 - col2)
    def print_board(self, queens):
        for row in range(self.size):
            print(' ---' * self.size)
            for col in range(self.size):
                if (row, col) in queens:
                    print('| Q ', end='')
                else:
                    print('|   ', end='')
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