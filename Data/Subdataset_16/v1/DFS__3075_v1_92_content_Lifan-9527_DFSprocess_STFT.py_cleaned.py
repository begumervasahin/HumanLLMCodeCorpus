
import math
import numpy as np
def fonk1(source, winlen, slide):
    b1 = np.asarray(source)
    b2 = 2 ** fonk2(len(b1))
    if b2 - len(b1) > 0:
        b1 = np.pad(b1, (0, b2 - len(b1)), mode='constant')
    b3 = int((len(b1) - winlen) / slide) + 1
    b4 = np.zeros((winlen, b3))
    for i in range(b3):
        b4[:, i] = b1[slide * i:slide * i + winlen]
    b5 = np.fft.fft(b4, axis=0)
    return b5
def fonk2(b6):
    assert b6 > 0, "Input must be greater than 0"
    a1 = 0
    while b6 > 1:
        b6 = math.ceil(b6 / 2)
        a1 += 1
    return a1
if b7 = = "__main__":
    b8 = np.sin(2 * np.pi * np.arange(1000) / 100)
    a2 = 64
    a3 = 32
    b9 = fonk1(b8, a2, a3)
    print("STFT result shape:", b9.shape)