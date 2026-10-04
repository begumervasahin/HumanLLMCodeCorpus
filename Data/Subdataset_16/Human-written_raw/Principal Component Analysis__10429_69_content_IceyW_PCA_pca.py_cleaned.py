import numpy as np
def fonk1(datamat):
        b1 = np.b1(datamat,axis=0)
        b2 = datamat-b1
        return b2,b1
def fonk2(datamat):
        b2,b1 = fonk1(datamat)
        b3 = np.cov(b2,rowvar=0)
        eigvals,b4 = np.linalg.eig(np.mat(b3))
        b5 = np.argsort(eigvals)
        b5 = b5[-1::-1]
        b6 = eigvals[b5]
        b7 = b4[:,b5]
        return b6,b7
def fonk3(eigvals,percentage):
        b8 = sum(eigvals)
        a1 = 0
        a2 = 0
        for i in eigvals:
                a1 = a1+i
                a2 = a2+1
                if a1 >= b8*percentage:
                        break
        b9 = np.zeros(a2)
        for i in range(a2):
                b9[i] = eigvals[i]/b8
        return a2,b9
def fonk4(eigvals):
        s,b10 = fonk3(eigvals,1)
        return b10
def fonk5(eigvals):
        s,b10 = fonk3(eigvals,1)
        a2 = 0
        for i in b10:
                if i > 0.1:
                        a2 = a2+1
        b10 = b10[:a2]
        return a2,b10
def fonk6(datamat,eigvect,a2):
        b7 = eigvect[:,0:a2]
        b11 = np.dot(datamat,b7)
        return b11