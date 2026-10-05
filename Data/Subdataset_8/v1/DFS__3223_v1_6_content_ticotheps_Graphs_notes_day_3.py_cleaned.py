class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)
def get_neighbors(v, matrix):
    col = v[0]
    row = v[1]
    neighbors = []
    if row > 0 and matrix[row - 1][col] == 1:
        neighbors.append((col, row - 1))
    if row < len(matrix) - 1 and matrix[row + 1][col] == 1:
        neighbors.append((col, row + 1))
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] == 1:
        neighbors.append((col + 1, row))
    if col > 0 and matrix[row][col - 1] == 1:
        neighbors.append((col - 1, row))
    return neighbors
def island_counter(matrix):
    visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
    island_count = 0
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if not visited[row][col] and matrix[row][col] == 1:
                visited = dft(col, row, matrix, visited)
                island_count += 1
    return island_count
def dft(col, row, matrix, visited):
    s = Stack()
    s.push((col, row))
    while s.size() > 0:
        v = s.pop()
        col = v[0]
        row = v[1]
        if not visited[row][col]:
            visited[row][col] = True
            for neighbor in get_neighbors(v, matrix):
                s.push(neighbor)
    return visited
islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]
print(island_counter(islands))