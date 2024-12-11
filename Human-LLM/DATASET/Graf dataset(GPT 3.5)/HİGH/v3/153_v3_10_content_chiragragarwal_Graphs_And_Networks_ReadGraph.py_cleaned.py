import numpy as np
from pathlib import Path
class class1:
    '''
    Reads a graph matrix from a text file and stores it as a numpy matrix.
    '''
    def fonk1(self, b1):
        '''
        Initializes the class1 with the provided file path.
        '''
        self.b1 = b1
    def fonk2(self):
        '''
        Reads the contents of the input file and converts it into a numpy matrix.
        '''
        with open(self.b1, 'r') as file:
            b2 = file.read()
        b3 = np.matrix(b2)
        return b3
if b4 = = "__main__":
    b5 = Path("your_graph_file.txt")
    b6 = class1(b5)
    b3 = b6.fonk2()
    print(b3)