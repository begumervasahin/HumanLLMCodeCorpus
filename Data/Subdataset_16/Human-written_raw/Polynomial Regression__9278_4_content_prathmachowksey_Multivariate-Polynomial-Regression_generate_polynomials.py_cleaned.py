import numpy as np
import pandas as pd
from itertools import combinations_with_replacement
def fonk1(degree):
    b1 = [0,1]
    b2 = []
    for i in range(1,degree+1):
        b2.append([x for x in combinations_with_replacement(b1,i)])
    b3 = []
    for sublist in b2:
        for x in sublist:
            b3.append(x)
    return b3
def fonk2(b6,b2):
    b4 = np.ones((b6.shape[0],len(b2)))
    for n in range(b6.shape[0]):
        for i in range(len(b2)):
            for j in b2[i]:
                b4[n][i]=b4[n][i]*b6[n][j]
    return b4
b5 = pd.read_csv('3D_spatial_network.txt',names=["id","latitude","longitude","altitude"])
print(b5.head())
b5 = b5.drop("id",axis=1)
print(b5.head())
b5 = (b5-b5.mean())/b5.std()
print(b5.head())
b6 = b5.iloc[:,0:2]
b6 = b6.values
b7 = b5.iloc[:,2:3]
b7 = b7.values
b8 = fonk1(1)
b9 = fonk1(2)
b10 = fonk1(3)
b11 = fonk1(4)
b12 = fonk1(5)
b13 = fonk1(6)
b14 = fonk2(b6,b8)
b15 = fonk2(b6,b9)
b16 = fonk2(b6,b10)
b17 = fonk2(b6,b11)
b18 = fonk2(b6,b12)
b19 = fonk2(b6,b13)
print(b10)
print(b6[:3])
print(b16[:3])
b7 = (b7-b7.mean())/b7.std()
b14 = (b14-b14.mean())/b14.std()
b15 = (b15-b15.mean())/b15.std()
b16 = (b16-b16.mean())/b16.std()
b17 = (b17-b17.mean())/b17.std()
b18 = (b18-b18.mean())/b18.std()
b19 = (b19-b19.mean())/b19.std()
np.save('b14.npy',b14)
np.save('b15.npy',b15)
np.save('b16.npy',b16)
np.save('b17.npy',b17)
np.save('b18.npy',b18)
np.save('b19.npy',b19)
np.save('b7.npy',b7)