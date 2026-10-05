class ComputeTools:
    def __init__(self, adjacency_matrix, nodes, start_node):
        self.adjacency_matrix = adjacency_matrix
        self.make_diagonal_zero(self.adjacency_matrix)
        self.start_index = nodes.index(start_node)
        self.nodes = nodes
    def calculate_single_step(self, step):
        for i in range(len(self.adjacency_matrix)):
            for j in range(len(self.adjacency_matrix)):
                if self.adjacency_matrix[i][step] != -1 and self.adjacency_matrix[step][j] != -1:
                    if self.adjacency_matrix[i][j] == -1:
                        self.adjacency_matrix[i][j] = self.adjacency_matrix[step][j] + self.adjacency_matrix[i][step]
                    else:
                        self.adjacency_matrix[i][j] = min(self.adjacency_matrix[i][j],
                                                           self.adjacency_matrix[step][j] + self.adjacency_matrix[i][step])
    def make_diagonal_zero(self, adjacency_matrix):
        for i in range(len(adjacency_matrix)):
            adjacency_matrix[i][i] = 0
    def calculate_shortest_paths(self):
        for step in range(len(self.adjacency_matrix)):
            self.calculate_single_step(step)
    def print_shortest_paths(self):
        self.calculate_shortest_paths()
        for n in range(len(self.nodes)):
            print(f"   \u279c {self.nodes[n]}: {self.adjacency_matrix[self.start_index][n]}".replace("-1", "inf"))
adjacency_matrix = [
    [0, 3, -1, 7],
    [8, 0, 2, -1],
    [-1, 5, 0, 1],
    [4, -1, -1, 0]
]
nodes_list = ['A', 'B', 'C', 'D']
start_node = 'A'
compute_tool = ComputeTools(adjacency_matrix, nodes_list, start_node)
compute_tool.print_shortest_paths()