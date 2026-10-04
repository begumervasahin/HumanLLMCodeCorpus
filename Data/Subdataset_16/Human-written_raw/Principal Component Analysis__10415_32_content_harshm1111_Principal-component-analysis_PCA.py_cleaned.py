import numpy as np
from scipy.spatial import distance
from sklearn.decomposition import PCA
b1 = int(raw_input())
b2 = int(raw_input())
b3 = int(raw_input())
b4 = int(raw_input())
b5 = [int(each) for each in raw_input().split()]
b6 = []
for i in range(b2):
    b6.append([int(each) for each in raw_input().split()])
def fonk1(b3, a, b):
    if b3 = = 1:
        return distance.minkowski(a, b, b7 = 1)
    elif b3 = = 2:
        return distance.minkowski(a, b, b7 = 2)
    elif b3 = = 3:
        return distance.minkowski(a, b, b7 = float('inf'))
    else:
        return distance.cosine(a, b)
def fonk2(number_components, b5, b6):
    b8 = np.array([b5] + b6)
    b9 = PCA(n_components=number_components)
    b9.fit(b8)
    b5 = b9.transform([b5])
    b10 = []
    for each in b6:
        b10.append(list(list(b9.transform([each]))[0]))
    return b5, b10, b9.explained_variance_
def fonk3(b5, b6):
    b11 = []
    if b4 != -1:
        b5, b6, b12 = fonk2(b4, b5, b6)
    for i in range(0, len(b6)):
        b11.append((i, fonk1(b3, b5, b6[i])))
    b11 = sorted(b11, key=lambda x: x[1])[0:5]
    for each in b11:
        print each[0]+1
    if b4!=-1:
        print sum(b12)
fonk3(b5, b6)