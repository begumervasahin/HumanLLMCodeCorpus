from IDAPICourseworkLibrary import *
from numpy import *
def fonk1(b11, root, b12):
    b1 = zeros((b12[root]), float )
    b2 = len(b11[:,0])
    for i in range(b2):
        b1[b11[i,root]]+=1
    b1/=b2
    return b1
def fonk2(b11, varC, varP, b12):
    b2 = len(b11[:,0])
    b3 = zeros((b12[varC], b12[varP]), float )
    for row in range(b2):
        b3[b11[row,varC]][b11[row,varP]]+=1
    for i in range(b12[varP]):
        b4 = (numpy.sum(b11[:,varP]==i))
        if b4!=0:
            b3[:,i]/=(numpy.sum(b11[:,varP]==i))
    return b3
def fonk3(b11, varRow, varCol, b12):
    b5 = zeros((b12[varRow], b12[varCol]), float )
    b2 = len(b11[:,0])
    for row in range(b2):
        b5[b11[row,varRow]][b11[row,varCol]]+=1
    b5/=b2
    return b5
def fonk4(aJPT):
    for i in range(len(aJPT[0,:])):
        b4 = (numpy.sum(aJPT[:,i]))
        if b4!=0:
            aJPT[:,i]*=1/b4
    return aJPT
def fonk5(b39, b38):
    b6 = zeros((b38[0].shape[0]), float)
    for i in range(len(b6)):
        b6[i]=b38[0][i]
        for j in range(0,len(b39)):
            b6[i]*=b38[j+1][b39[j],i]
    if (numpy.sum(b6)!=0):
        b6*=1/(numpy.sum(b6))
    else:
        b6 = ones((b38[0].shape[0]), float)/b38[0].shape[0]
    return b6
def fonk6(jP):
    a1 = 0.0
    b7 = len(jP[0,:])
    b8 = len(jP[:,0])
    b9 = zeros(b7, float)
    for j in range(b7):
        b9[j] = sum(jP[:,j])
    for i in range(b8):
        b10 = sum(jP[i,:])
        for j in range(b7):
            if (jP[i][j] != 0):
                a1+= jP[i][j]*log2(jP[i][j]/(b10*b9[j]))
    return a1
b11 = ImportData("IDAPICourseworkData.csv", ",")
b11 = Discretise(b11, [5, 5, 5, 5, 5, 5, 5], ["s", "s", "s", "s", "s", "s", "c"])
b12 = [5, 5, 5, 5, 5, 5, 5]
b13 = fonk1(b11, 0, b12)
b14 = fonk1(b11, 1, b12)
b15 = fonk1(b11, 2, b12)
b16 = fonk1(b11, 3, b12)
b17 = fonk1(b11, 4, b12)
b18 = fonk1(b11, 5, b12)
b19 = fonk1(b11, 6, b12)
b20 = fonk2(b11, 0, 1, b12)
b21 = fonk2(b11, 1, 2, b12)
b22 = fonk2(b11, 2, 3, b12)
b23 = fonk2(b11, 3, 4, b12)
b24 = fonk2(b11, 4, 5, b12)
b25 = fonk2(b11, 5, 6, b12)
b26 = fonk3(b11, 0, 1, b12)
b27 = fonk3(b11, 1, 2, b12)
b28 = fonk3(b11, 2, 3, b12)
b29 = fonk3(b11, 3, 4, b12)
b30 = fonk3(b11, 4, 5, b12)
b31 = fonk3(b11, 5, 6, b12)
b32 = fonk4(b26)
b33 = fonk4(b27)
b34 = fonk4(b28)
b35 = fonk4(b29)
b36 = fonk4(b30)
b37 = fonk4(b31)
b38 = [b13, b32, b33, b34, b35, b36, b37]
b39 = [1, 3, 2, 4, 2, 1]
b40 = fonk5(b39, b38)
print("Result of query:", b40)
b41 = fonk6(b26)
b42 = fonk6(b27)
b43 = fonk6(b28)
b44 = fonk6(b29)
b45 = fonk6(b30)
b46 = fonk6(b31)
print("Mutual Information between A and B:", b41)
print("Mutual Information between B and C:", b42)
print("Mutual Information between C and D:", b43)
print("Mutual Information between D and E:", b44)
print("Mutual Information between E and F:", b45)
print("Mutual Information between F and G:", b46)