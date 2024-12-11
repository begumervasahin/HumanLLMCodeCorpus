from IDAPICourseworkLibrary import *
from numpy import *
def fonk1(b11, root, noStates):
    b1 = zeros((noStates[root]), float )
    b2 = len(b11[:,0])
    for i in range(b2):
        b1[b11[i,root]]+=1
    b1/=b2
    return b1
def fonk2(b11, varC, varP, noStates):
    b2 = len(b11[:,0])
    b3 = zeros((noStates[varC], noStates[varP]), float )
    for row in range(b2):
        b3[b11[row,varC]][b11[row,varP]]+=1
    for i in range(noStates[varP]):
        b4 = (numpy.sum(b11[:,varP]==i))
        if b4!=0:
            b3[:,i]/=(numpy.sum(b11[:,varP]==i))
    return b3
def fonk3(b11, varRow, varCol, noStates):
    b5 = zeros((noStates[varRow], noStates[varCol]), float )
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
def fonk5(b12, b16):
    b6 = zeros((b16[0].shape[0]), float)
    for i in range(len(b6)):
        b6[i]=b16[0][i]
        for j in range(0,len(b12)):
            b6[i]*=b16[j+1][b12[j],i]
    if (numpy.sum(b6)!=0):
        b6*=1/(numpy.sum(b6))
    else:
        b6 = ones((b16[0].shape[0]), float)/b16[0].shape[0]
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
            if (jP[i][j] != 0 and b9[j] != 0 and b10 != 0):
                a1+= jP[i][j]*math.log(jP[i][j]/(b10*b9[j]),2)
    return a1
b11 = array([[1,1,1,1],[1,2,1,1],[2,1,2,2],[2,2,2,2],[2,2,1,1]])
b12 = array([0,1,1])
b1 = fonk1(b11, 0, [3,2,2,2])
print("Prior:", b1)
b13 = fonk2(b11, 1, 0, [3,2,2,2])
print("CPT:", b13)
b14 = fonk3(b11, 0, 1, [3,2,2,2])
print("JPT:", b14)
b15 = fonk4(b14)
print("CPT from JPT:", b15)
b16 = [b1, b15]
for i in range(len(b12)):
    print("Query result:", fonk5(b12, b16))
b17 = fonk6(b14)
print("Mutual Information:", b17)