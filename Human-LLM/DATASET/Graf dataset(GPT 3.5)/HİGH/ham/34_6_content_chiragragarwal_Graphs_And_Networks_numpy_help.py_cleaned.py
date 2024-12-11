import numpy
b1 = '1 2 3 4 ; 5 6 7 8 ; 0 1 2 3'
b2 = numpy.matrix(b1)
b2.shape
b2[0,1]
b2[2,3]
b2[0,1] = -8
b2[1]
b2[: , 1]