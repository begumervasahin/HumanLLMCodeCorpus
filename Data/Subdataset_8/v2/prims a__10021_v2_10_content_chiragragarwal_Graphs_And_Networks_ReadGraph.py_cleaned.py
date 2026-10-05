import numpy
from pathlib import Path
class ReadGraph:
    '''
    This class reads a graph matrix from a text file and stores it in a numpy matrix.
    It returns the same matrix.
    '''
    def __init__(self, input_file):
        self.input_file = input_file
    def read(self):
        '''
        Reads the contents of the input file and converts it into a matrix.
        '''
        with open(self.input_file, 'r') as file:
            graph_string = file.read()
        graph_matrix = numpy.matrix(graph_string)
        return graph_matrix
if __name__ == "__main__":
    input_file_path = Path("your_graph_file.txt")
    graph_reader = ReadGraph(input_file_path)
    graph_matrix = graph_reader.read()
    print(graph_matrix)