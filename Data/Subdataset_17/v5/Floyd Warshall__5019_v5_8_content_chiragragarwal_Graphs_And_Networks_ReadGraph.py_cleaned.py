import numpy as np
class ReadGraph:
    def __init__(self, input_file: str):
        self.input_file = input_file
    def read(self) -> np.matrix:
        try:
            with open(self.input_file, 'r') as file:
                graph_string = file.read()
            graph_matrix = np.matrix(graph_string)
            return graph_matrix
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{self.input_file}' does not exist.")
        except ValueError:
            raise ValueError("The file content could not be converted to a NumPy matrix.")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {e}")
if __name__ == '__main__':
    file_path = 'graph_matrix.txt'
    graph_reader = ReadGraph(file_path)
    try:
        graph_matrix = graph_reader.read()
        print("Graph matrix:\n", graph_matrix)
    except Exception as e:
        print(f"Error: {e}")