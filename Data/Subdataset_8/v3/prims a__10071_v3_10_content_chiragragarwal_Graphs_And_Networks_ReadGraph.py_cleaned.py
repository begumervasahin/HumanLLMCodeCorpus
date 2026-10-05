import numpy as np
from pathlib import Path
class GraphReader:
    '''
    Reads a graph matrix from a text file and stores it as a numpy matrix.
    '''
    def __init__(self, file_path):
        '''
        Initializes the GraphReader with the provided file path.
        '''
        self.file_path = file_path
    def read_matrix(self):
        '''
        Reads the contents of the input file and converts it into a numpy matrix.
        '''
        with open(self.file_path, 'r') as file:
            graph_string = file.read()
        graph_matrix = np.matrix(graph_string)
        return graph_matrix
if __name__ == "__main__":
    input_file_path = Path("your_graph_file.txt")
    graph_reader = GraphReader(input_file_path)
    graph_matrix = graph_reader.read_matrix()
    print(graph_matrix)