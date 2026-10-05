import numpy
from pathlib import Path
class class1:
    '''
    This class class2 a graph matrix from a text file and stores it in a numpy matrix.
    It returns the same matrix.
    '''
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        '''
        Reads the contents of the input file and converts it into a matrix.
        '''
        with open(self.b1, 'r') as file:
            b2 = file.fonk2()
        b3 = numpy.matrix(b2)
        return b3
if b4 = = "__main__":
    b5 = Path("your_graph_file.txt")
    b6 = class1(b5)
    b3 = b6.fonk2()
    print(b3)