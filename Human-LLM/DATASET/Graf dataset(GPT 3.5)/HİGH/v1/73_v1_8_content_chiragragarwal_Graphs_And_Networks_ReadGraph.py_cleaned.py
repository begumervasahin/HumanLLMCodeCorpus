import numpy as np
from path import Path
class class1:
    '''
    Read the graph matrix from a text file and store it in a numpy matrix.
    Returns the same matrix
    '''
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        '''
        Read the file contents into a matrix
        '''
        b2 = self.b1.text()
        b3 = np.matrix(str(b2))
        return b3
if b4 = = "__main__":
    b1 = Path("your_graph_file.txt")
    b5 = class1(b1)
    b6 = b5.fonk2()
    print("Graph Matrix:")
    print(b6)