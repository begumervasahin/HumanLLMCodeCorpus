'''
è®¡ç®è¿ç»­åº¦
'''
import scipy.io as sio
import numpy as np
import itertools
def fonk1(b14):
    if 0 in b14:
        b1 = max([len(list(a1)) for i, a1 in itertools.groupby(b14) if i == 0])
        b2 = b14.count(0)
        b3 = 1-b1/b2
    else:
        b3 = 0
    return b3
def fonk2(lyst):
    b4 = len(lyst)-1
    b5 = []
    for i  in range(b4):
        if lyst[i] + lyst[i+1]==0:
            b5.append(i)
            b5.append(i+1)
    b6 = np.array(b5)
    b6 = b6.reshape(-1,2)
    print(b6)
    b7 = []
    b8 = len(b6)-1
    a1 = 0
    b9 = lyst
    while a1 <= b8:
        h,b10 = b6[a1][0],b6[a1][1]
        b9[h],b9[b10] = 1,1
        b3 = fonk1(b9)
        b7.append(b3)
        b9[h], b9[b10] = 0,0
        a1+=1
    if len(b7)== 0:
       b11 = np.array([9, 9])
       a2 = 9
    else:
       a2 = min(b7)
       b12 = b7.index(min(b7))
       b11 = b6[b12]
    return b11,a2
if b13 = ='__main__':
    b14 = [0,1,0,0,0,0]
    print(fonk2(b14))