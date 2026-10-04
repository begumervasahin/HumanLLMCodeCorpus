import numpy
mat = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
graphMat = numpy.matrix(mat)
graphMat.shape
graphMat[0,1]
graphMat[2,3]
graphMat[0,1] = -8
graphMat[1]
graphMat[: , 1]