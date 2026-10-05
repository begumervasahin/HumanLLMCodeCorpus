import numpy
from path import Path
class ReadGraph:
    '''
    This class reads a graph matrix from a text file and stores it in a numpy matrix.
    It then returns the same matrix.
    '''
    def __init__(self, inputFile):
        self.inputFile = inputFile
    def read(self):
        '''
        This method reads the contents of the file into a matrix.
        '''
        graphString = self.inputFile.text()
        graphMat = numpy.matrix(str(graphString))
        return graphMat