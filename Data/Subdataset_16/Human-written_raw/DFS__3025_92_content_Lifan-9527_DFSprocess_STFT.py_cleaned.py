
import math
import numpy as np
def fonk1(source, winlen, slide):
    b1 = source
    b2 = 2**fonk2(len(source))
    if b2-len(source)>0:
        b1 = b1+[0]*(b2-len(source))
    b3 = int((len(b1)-winlen)/slide)+1
    b4 = np.arange(b3*winlen).reshape(winlen, b3)
    for i in range(0, b3):
        b4[:,i] = b1[slide*i:slide*i+winlen]
    b5 = b4.astype(complex)
    for i in range(0,b3):
        b5[:,i] = np.fft.fft(b4[:,i])
    return b5
def fonk2(b6):
    assert(b6>0),"Input must be bigger than 0"
    a1 = 0
    while(True):
        if b6>1:
            b6 = math.ceil(b6/2)
            a1 += 1
        elif b6<=1:
            break
    return a1