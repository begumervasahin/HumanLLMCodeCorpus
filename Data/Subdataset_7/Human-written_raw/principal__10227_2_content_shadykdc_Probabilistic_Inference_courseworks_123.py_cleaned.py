from IDAPICourseworkLibrary import *
from numpy import *
def fonk1(b39, root, noStates):
    b1 = zeros((noStates[root]), float )
    b2 = len(b39[:,0])
    for i in range(b2):
        b1[b39[i,root]]+=1
    b1/=b2
    return b1
def fonk2(b39, varC, varP, noStates):
    b2 = len(b39[:,0])
    b3 = zeros((noStates[varC], noStates[varP]), float )
    for row in range(b2):
        b3[b39[row,varC]][b39[row,varP]]+=1
    for i in range(noStates[varP]):
        b4 = (numpy.sum(b39[:,varP]==i))
        if b4!=0:
            b3[:,i]/=(numpy.sum(b39[:,varP]==i))
    return b3
def fonk3(b39, varRow, varCol, noStates):
    b5 = zeros((noStates[varRow], noStates[varCol]), float )
    b2 = len(b39[:,0])
    for row in range(b2):
        b5[b39[row,varRow]][b39[row,varCol]]+=1
    b5/=b2
    return b5
def fonk4(aJPT):
    for i in range(len(aJPT[0,:])):
        b4 = (numpy.sum(aJPT[:,i]))
        if b4!=0:
            aJPT[:,i]*=1/b4
    return aJPT
def fonk5(theQuery, naiveBayes):
    b6 = zeros((naiveBayes[0].shape[0]), float)
    for i in range(len(b6)):
        b6[i]=naiveBayes[0][i]
        for j in range(0,len(theQuery)):
            b6[i]*=naiveBayes[j+1][theQuery[j],i]
    if (numpy.sum(b6)!=0):
        b6*=1/(numpy.sum(b6))
    else:
        b6 = ones((naiveBayes[0].shape[0]), float)/naiveBayes[0].shape[0]
    return b6
def fonk6(b12):
    a1 = 0.0
    b7 = len(b12[0,:])
    b8 = len(b12[:,0])
    b9 = zeros(b7, float)
    for j in range(b7):
        b9[j] = sum(b12[:,j])
    for i in range(b8):
        b10 = sum(b12[i,:])
        for j in range(b7):
            if (b12[i][j] != 0):
                a1 += (b12[i][j] * log2(b12[i][j]/(b10*b9[j])))
    return a1
def fonk7(b39, noVariables, noStates):
    b11 = zeros((noVariables, noVariables))
    for i in range(noVariables):
        for j in range(i+1):
            b12 = fonk3(b39, i, j, noStates)
            b11[i][j] = fonk6(b12)
            b11[j][i] = b11[i][j]
    return b11
def fonk8(depMatrix):
    b13 = []
    b8 = len(depMatrix[:,0])
    for i in range(b8):
        for j in range(i):
            b13.append([depMatrix[i][j], i, j])
    b14 = sorted(b13, reverse=True)
    return array(b14)
def fonk9(vec,root1,root2):
    for i in range(len(vec)):
      if (vec[i]==root2):
	vec[i]=root1
def fonk10(b13, noVariables):
    b15 = []
    b16 = numpy.arange(noVariables)
    b17 = [[item[1],item[2]] for item in b13]
    for i in range(len(b17)):
      b18 = b17[i][0]
      b19 = b17[i][1]
      if (b16[b18]!=b16[b19]):
	fonk9(b16,b16[b18],b16[b19])
	b15.append(b17[i])
    return array(b15)
def fonk11(b39, child, parent1, parent2, noStates):
    b3 = zeros([noStates[child],noStates[parent1],noStates[parent2]], float )
    for i in range(len(b39)):
        b3[b39[i, child]][b39[i, parent1]][b39[i, parent2]]+=1
    for i in range(noStates[parent1]):
        for j in range(noStates[parent2]):
            b4 = sum(b3[:,i,j])
            if b4!=0:
                b3[:,i,j]/=b4
    return b3
def fonk12(b39, noStates):
    b20 = [[0],[1],[2,0],[3,2,1],[4,3],[5,3]]
    b21 = fonk1(b39, 0, noStates)
    b22 = fonk1(b39, 1, noStates)
    b23 = fonk2(b39, 2, 0, noStates)
    b24 = fonk11(b39, 3, 2, 1, noStates)
    b25 = fonk2(b39, 4, 3, noStates)
    b26 = fonk2(b39, 5, 3, noStates)
    b27 = [b21, b22, b23, b24, b25, b26]
    return b20, b27
def fonk13(b39, noStates):
    b20 = [[0],[1],[2,0],[3,4],[4,1],[5,4],[6,1],[7,0,1],[8,7]]
    b21 = fonk1(b39, 0, noStates)
    b22 = fonk1(b39, 1, noStates)
    b23 = fonk2(b39, 2, 0, noStates)
    b24 = fonk2(b39, 3, 4, noStates)
    b25 = fonk2(b39, 4, 1, noStates)
    b26 = fonk2(b39, 5, 4, noStates)
    b28 = fonk2(b39, 6, 1, noStates)
    b29 = fonk11(b39, 7, 0, 1, noStates)
    b30 = fonk2(b39, 8, 7, noStates)
    b27 = [b21, b22, b23, b24, b25, b26, b28, b29, b30]
    return b20, b27
def fonk14(b39, noStates):
    b20 = [[0],[1,0],[2,0],[3,1]]
    b21 = fonk1(b39, 0, noStates)
    b22 = fonk1(b39, 1, noStates)
    b23 = fonk2(b39, 2, 0, noStates)
    b24 = fonk2(b39, 3, 1, noStates)
    b27 = [b21, b22, b23, b24]
    return b20, b27
def fonk15(b20, b27, noDataPoints, noStates):
    a2 = 0.0
    a3 = 0
    for aList in b20:
        b31 = noStates[aList[0]]-1
        for i in xrange(1,len(aList)):
            b31 *= noStates[aList[i]]
        a3 += b31
    a2 = a3*log2(noDataPoints)/2
    return a2
def fonk16(dataPoint, b20, b27):
    b12 = 1.0
    for i in range(len(dataPoint)):
        if len(b20[i])==1:
            b12*=b27[i][dataPoint[i]]
        elif len(b20[i])==2:
            b12*=(b27[i])[dataPoint[i]][dataPoint[b20[i][1]]]
        else:
            b12*=(b27[i])[dataPoint[i]][dataPoint[b20[i][1]]][dataPoint[b20[i][2]]]
    return b12
def fonk17(b39, b20, b27):
    a4 = 0
    for i in range(len(b39)):
        a4+=log2(fonk16(b39[i],b20,b27))
    return a4
def fonk18(b39, b20, b27,noStates):
    b32 = fonk15(b20, b27,len(b39),noStates)
    b33 = fonk17(b39, b20, b27)
    b34 = b32-b33
    return b34
def fonk19(b39,b20,b27,noStates):
    b35 = []
    for aList in b20:
        if len(aList)==2:
            b36 = numpy.copy(b27[aList[0]])
            b37 = aList[1]
            b27[aList[0]]=fonk1(b39,aList[0],noStates)
            aList.remove(b37)
            b35.append(fonk18(b39, b20, b27,noStates))
            b27[aList[0]]=numpy.copy(b36)
            aList.append(b37)
        if len(aList)==3:
            for i in range(1,2):
                b36 = numpy.copy(b27[aList[0]])
                b37 = aList[2] if i==1 else aList[1]
                b27[aList[0]]=fonk2(b39,aList[0],aList[i],noStates)
                aList.remove(b37)
                b35.append(fonk18(b39, b20, b27,noStates))
                b27[aList[0]]=numpy.copy(b36)
                aList.append(b37)
    print(min(b35))
    return min(b35)
noVariables, noRoots, noStates, noDataPoints, b38 = ReadFile("HepatitisC.txt")
b39 = array(b38)
AppendString("results.txt","Coursework Three Results by Kathryn Shea & Pierre Thary")
AppendString("results.txt","")
AppendString("results.txt","The MDLSize of our network for Hepatitis C data set")
AppendString("results.txt","")
[arclist,cptlist]=fonk13(b39, noStates)
b40 = fonk15(arclist,cptlist,len(b39),noStates)
b41 = fonk17(b39,arclist,cptlist)
fonk19(b39,arclist,cptlist,noStates)