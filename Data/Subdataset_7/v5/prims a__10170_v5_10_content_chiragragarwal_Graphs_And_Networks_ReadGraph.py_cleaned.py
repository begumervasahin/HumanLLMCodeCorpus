import numpy
from path import Path
class class1:
    '''
    This class class2 a graph matrix from a text file and stores it in a numpy matrix.
    It then returns the same matrix.
    '''
    def fonk1(self, b1):
        '''
        Initialize the class1 object with the input file path.
        '''
        self.b1 = b1
    def fonk2(self):
        '''
        Read the contents of the file and convert it into a numpy matrix.
        '''
        b2 = self.fonk3()
        b3 = numpy.matrix(b2)
        return b3
    def fonk3(self):
        '''
        Helper method to read the contents of the file.
        '''
        with open(self.b1, 'r') as file:
            b2 = file.read()
        return b2