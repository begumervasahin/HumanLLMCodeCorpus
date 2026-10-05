import numpy
from pathlib import Path
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
        with open(self.b1, 'r') as file:
            b2 = file.fonk2()
        b3 = numpy.matrix(b2)
        return b3
if b4 = = "__main__":
    b5 = Path("your_graph_file.txt")
    b6 = class1(b5)
    b7 = b6.fonk2()
    print(b7)