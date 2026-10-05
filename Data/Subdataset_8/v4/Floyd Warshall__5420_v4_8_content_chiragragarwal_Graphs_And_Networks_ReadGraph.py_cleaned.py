import numpy as np
from path import Path
class GraphReader:
    def __init__(self, file_path):
        self.file_path = file_path
    def read(self):
        with open(self.file_path, 'r') as file:
            graph_string = file.read()
            graph_matrix = np.matrix(graph_string)
        return graph_matrix
if __name__ == "__main__":
    input_file_path = "your_graph_file.txt"
    graph_reader = GraphReader(input_file_path)
    graph_matrix = graph_reader.read()
    print("Graph Matrix:")
    print(graph_matrix)