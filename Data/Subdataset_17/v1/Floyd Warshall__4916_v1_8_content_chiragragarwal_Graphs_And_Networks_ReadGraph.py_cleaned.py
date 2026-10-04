import numpy as np
class ReadGraph:
    def __init__(self, input_file):
        self.input_file = input_file
    def read(self):
        with open(self.input_file, 'r') as file:
            graph_string = file.read()
        graph_mat = np.matrix(graph_string)
        return graph_mat
if __name__ == '__main__':
    file_path = 'graph_matrix.txt'
    graph_reader = ReadGraph(file_path)
    graph_matrix = graph_reader.read()
    print("Graph matrix:\n", graph_matrix)