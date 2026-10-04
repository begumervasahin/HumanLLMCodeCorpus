
import math
import numpy as np
def stft(source, winlen, slide):
    data = source
    topindex = 2**power2Near(len(source))
    if topindex-len(source)>0:
        data = data+[0]*(topindex-len(source))
    winNum = int((len(data)-winlen)/slide)+1
    Map = np.arange(winNum*winlen).reshape(winlen, winNum)
    for i in range(0, winNum):
        Map[:,i] = data[slide*i:slide*i+winlen]
    cMap = Map.astype(complex)
    for i in range(0,winNum):
        cMap[:,i] = np.fft.fft(Map[:,i])
    return cMap
def power2Near(k):
    assert(k>0),"Input must be bigger than 0"
    power = 0
    while(True):
        if k>1:
            k=math.ceil(k/2)
            power += 1
        elif k<=1:
            break
    return power