from matplotlib.pyplot import plot, show
from numpy import loadtxt, ones, zeros, array, ndarray
from numpy.linalg import pinv
from numpy.ma import power
b1 = loadtxt('data/svar-set1.dat.txt')
b2 = loadtxt('data/svar-set2.dat.txt')
b3 = loadtxt('data/svar-set3.dat.txt')
b4 = loadtxt('data/svar-set4.dat.txt')
def fonk1(b7, b14):
    b5 = pinv(b7).dot(b14)
    return b5
def fonk2(b7, b14):
    b5 = fonk1(b7, b14)
    b6 = b7.dot(b5)
    return b6, b5
def fonk3(b5, xIn):
    b7 = ones(shape=(1, xIn.size + 1))
    b7[0, 1:] = xIn
    b8 = b7.dot(b5)
    return b8
def fonk4(x):
    m, b9 = x.shape
    b7 = ones(shape=(m, b9+1))
    b7[:, 1:] = x[:, :]
    return b7
def fonk5(x, order):
    m, b9 = x.shape
    b10 = b9 + order
    b7 = ones(shape=(m, b10))
    for i in range(1, order+1):
        b7[:, b9+i-1] = power(x[:, 0], i)
    return b7
def fonk6(b6, b14):
    m, b9 = b14.shape
    b11 = array(b6 - b14).transpose().dot((b6-b14))
    b11 /= m
    return b11
def fonk7(x, b9):
    row, b12 = x.shape
    b13 = row / b9
    b14 = ndarray(shape=(b9, b13, b12))
    for i in range(0, b9):
        b14[i, :, :] = x[i*b13: ((i+1)*b13), :]
    return b14
def fonk8(x, i):
    splits, row, b12 = x.shape
    b15 = ndarray(shape=((splits-1)*row, b12))
    b16 = ndarray(shape=(row, b12))
    b16 = x[i, :, :]
    a1 = 0
    for b10 in range(0, splits):
        if b10 = = i:
            continue
        b15[a1*row:(a1+1)*row, :] = x[b10, :, :]
        a1 += 1
    print "b15 :", b15.shape
    print "b16 :", b16.shape
    return b15, b16
def fonk9(data):
    row, b12 = data.shape
    b17 = data[:, :b12-1]
    b14 = data[:, b12-1:]
    b17 = zeros(shape=(b17.size, 1))
    b17[:, 0:] = data[:, :b12-1]
    b14 = zeros(shape=(b14.size, 1))
    b14[:, 0:] = data[:, b12-1:]
    b18 = fonk4(b17)
    Y_fit, b5 = fonk2(b18, b14)
    b18 = fonk5(b17, 3)
    Y_fit_quad, b19 = fonk2(b18, b14)
    b18 = fonk5(b17, 5)
    Y_fit_third, b20 = fonk2(b18, b14)
    print "Average SSE for linear :", fonk6(Y_fit, b14), \
        " Polynomial of degree 2: ", fonk6(Y_fit_quad, b14), \
        " Polynomial of degree 3: ", fonk6(Y_fit_third, b14)
    plot(b17, b14, 'r+', b17, Y_fit, '.', b17, Y_fit_quad, 'r.', b17, Y_fit_third, 'g.')
    show()
fonk9(b1)
fonk9(b2)
fonk9(b3)
fonk9(b4)
b17 = fonk7(b1, 10)
fonk8(b17, 1)