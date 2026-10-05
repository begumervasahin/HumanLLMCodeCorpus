import random
class Maze:
    def __init__(self, dim=0, p=0, maze_arr=None):
        self.arr = []
        self.dim = dim
        self.p = p
        if maze_arr is None:
            self.generate_random_maze()
        else:
            self.arr = [[cell if cell != ' ' else 'O' for cell in row] for row in maze_arr]
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
class SolverBase(Maze):
    def __init__(self, maze_obj):
        super().__init__(maze_obj.dim, maze_obj.p, maze_obj.arr)
        self.visited = set()
        self.parent = {}
        self.is_solvable = False
    def find_path(self, start_i, start_j, move_offsets):
        self.visited.add((start_i, start_j))
        queue = [(start_i, start_j)]
        while queue:
            cur_i, cur_j = queue.pop(0)
            for i_offset, j_offset in move_offsets:
                new_i, new_j = cur_i + i_offset, cur_j + j_offset
                if 0 <= new_i < self.dim and 0 <= new_j < self.dim and self.arr[new_i][new_j] != 'X' and \
                        (new_i, new_j) not in self.visited:
                    self.parent[(new_i, new_j)] = (cur_i, cur_j)
                    queue.append((new_i, new_j))
                    self.visited.add((new_i, new_j))
                    if self.arr[new_i][new_j] == 'G':
                        self.is_solvable = True
                        return
    def trace_path(self, goal_i, goal_j):
        i, j = goal_i, goal_j
        while (i, j) != (0, 0):
            self.arr[i][j] = ' '
            i, j = self.parent[(i, j)]
    def display_solution(self, move_offsets):
        self.find_path(0, 0, move_offsets)
        if self.is_solvable:
            print(f"Displaying solution with {self.__class__.__name__} -")
            self.trace_path(self.dim - 1, self.dim - 1)
            self.display()
        else:
            print("Maze is not solvable.")
class DFSSolver(SolverBase):
    def __init__(self, maze_obj):
        super().__init__(maze_obj)
    def solve(self):
        self.display_solution([(0, 1), (0, -1), (1, 0), (-1, 0)])
class BFSSolver(SolverBase):
    def __init__(self, maze_obj):
        super().__init__(maze_obj)
    def solve(self):
        self.display_solution([(1, 0), (-1, 0), (0, 1), (0, -1)])
if __name__ == '__main__':
    maze = Maze(10, 0.2)
    maze.display()
    bfs_solver = BFSSolver(maze)
    bfs_solver.solve()