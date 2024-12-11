import sys
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import heapq
from PIL import Image
def fonk1(x, y):
    b1 = x - y
    return np.linalg.norm(b1)
b2 = int(input("please type a b2 for how many nearest neighbors you want to compute"))
b3 = int(input("There are 10,000 pictures of numbers.\n  How many would you like to use as training b4?"))
b4 = sio.loadmat('ML_hw1data.mat')
b5 = b4['X'][:b3]
b6 = b4['Y'][:b3]
b7 = b4['X'][b3:]
b8 = b4['Y'][b3:]
b9 = [0,0]
a1 = 0
a2 = 1
for test_idx in range(0, len(b7)):
    b10 = []
    for i in range(0, 100):
        b11 = b5[i]
        b12 = fonk1(b11, b7[test_idx])
        if (len(b10) < b2):
            heapq.heappush(b10, (b12, str(i)))
            heapq._heapify_max(b10)
        elif (b12 < b10[0][0]):
            heapq.heappop(b10)
            heapq.heappush(b10, (b12, str(i)))
            heapq._heapify_max(b10)
    b13 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for pair in b10:
        b14 = int(pair[1])
        b15 = b6[b14][0]
        b13[b15] += 1
    a3 = 0
    a4 = 0
    for i in range(0, 10):
        if (b13[i] > a4):
            a3 = i
    b16 = b8[test_idx][0]
    if (b16 = = a3):
        b9[a1] += 1
    else :
        b9[a2] += 1
    print("   test image ", b17 = '')
    print((b3 + test_idx), b17 = '')
    print(" was identified as ", b17 = '')
    print(a3)
    print("     actual b15 was ", b17 = '')
    print(b8[test_idx][0])
print("    b2 was ", b17 = '')
print(b2)
print("    and we used ", b17 = '')
print(b3, b17 = '')
print(" training b4 points")
print("\n\n\n\n   Correct vs. wrong answers:")
print(b9)
print("\n\n\n\n\n    Percentage correct:    ")
print(   (b9[0] +0.0)   /   b9[1])