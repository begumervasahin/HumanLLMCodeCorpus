import random
import sys
class Maze:
    def __init__(self, dim=0, p=0, maze_arr=[]):
        self.arr = []
        self.dim = dim
        self.p = p
        if dim != 0:
            self.generate_random_maze()
        else:
            self.arr = [[cell if cell != ' ' else 'O' for cell in row] for row in maze_arr]
            self.dim = len(maze_arr)
    def generate_random_maze(self):
        for i in range(self.dim):
            row = []
            for j in range(self.dim):
                cell = 'X' if random.random() < self.p else 'O'
                row.append(cell)
            self.arr.append(row)
        self.arr[0][0] = 'S'
        self.arr[self.dim - 1][self.dim - 1] = 'G'
    def display(self):
        for row in self.arr:
            print(*row, sep=' ')
class DFSSolver(Maze):
    path = []
    dfs_stack = []
    def __init__(self, maze_obj):
        super().__init__(0, 0, maze_obj.arr)
        self.visited = set()
        self.parent = dict()
        self.is_solvable = False
    def find_path(self, cur_i, cur_j):
        self.visited.add((cur_i, cur_j))
        self.dfs_stack.append((cur_i, cur_j))
        while self.dfs_stack:
            cur_i, cur_j = self.dfs_stack.pop()
            for i in range(cur_i - 1, cur_i + 2):
                for j in range(cur_j - 1, cur_j + 2):
                    if 0 <= i < self.dim and 0 <= j < self.dim and abs(i - cur_i) + abs(j - cur_j) == 1 \
                            and self.arr[i][j] != 'X' and (i, j) not in self.visited:
                        self.parent[(i, j)] = (cur_i, cur_j)
                        self.dfs_stack.append((i, j))
                        self.visited.add((i, j))
                        if self.arr[i][j] == 'G':
                            self.is_solvable = True
                            return
    def trace_path(self, goal_i, goal_j):
        i, j = goal_i, goal_j
        while (i, j) != (0, 0):
            self.path.append((i, j))
            i, j = self.parent[(i, j)]
        self.path.pop(0)
        for i, j in self.path:
            self.arr[i][j] = ' '
    def display_solution(self):
        self.find_path(0, 0)
        if self.is_solvable:
            print("Displaying solution with DFS -")
            self.trace_path(self.dim - 1, self.dim - 1)
            for row in self.arr:
                print(*row, sep=' ')
        else:
            print("Maze is not solvable.")
class BFSSolver(Maze):
    path = []
    def __init__(self, maze_obj):
        super().__init__(0, 0, maze_obj.arr)
        self.visited = set()
        self.parent = dict()
        self.queue = []
        self.is_solvable = False
    def find_path(self, cur_i, cur_j):
        self.queue.append((cur_i, cur_j))
        self.visited.add((cur_i, cur_j))
        while self.queue:
            cur_i, cur_j = self.queue.pop(0)
            for i in range(cur_i - 1, cur_i + 2):
                for j in range(cur_j - 1, cur_j + 2):
                    if 0 <= i < self.dim and 0 <= j < self.dim and abs(i - cur_i) + abs(j - cur_j) == 1 \
                            and self.arr[i][j] != 'X' and (i, j) not in self.visited:
                        self.parent[(i, j)] = (cur_i, cur_j)
                        self.visited.add((i, j))
                        self.queue.append((i, j))
                        if self.arr[i][j] == 'G':
                            self.is_solvable = True
                            return
    def trace_path(self, goal_i, goal_j):
        i, j = goal_i, goal_j
        while (i, j) != (0, 0):
            self.arr[i][j] = ' '
            i, j = self.parent[(i, j)]
    def display_solution(self):
        self.find_path(0, 0)
        if self.is_solvable:
            print("Displaying solution with BFS -")
            self.trace_path(self.dim - 1, self.dim - 1)
            for row in self.arr:
                print(*row, sep=' ')
        else:
            print("Maze is not solvable.")
if __name__ == '__main__':
    M = Maze(4000, 0.1)
    B = BFSSolver(M)
    print("Successful")