import scipy.io as sio
import numpy as np
import heapq
def fonk1(x, y):
    b1 = x - y
    return np.linalg.norm(b1)
b2 = int(input("Please type a b2 for how many nearest neighbors you want to compute: "))
b3 = int(input("There are 10,000 pictures of numbers. How many would you like to use as training b4? "))
b4 = sio.loadmat('ML_hw1data.mat')
b5 = b4['X'][:b3]
b6 = b4['Y'][:b3]
b7 = b4['X'][b3:]
b8 = b4['Y'][b3:]
b9 = [0, 0]
a1 = 0
a2 = 1
for test_idx in range(len(b7)):
    b10 = []
    for i in range(100):
        b11 = b5[i]
        b12 = fonk1(b11, b7[test_idx])
        if len(b10) < b2:
            heapq.heappush(b10, (b12, str(i)))
            heapq._heapify_max(b10)
        elif b12 < b10[0][0]:
            heapq.heappop(b10)
            heapq.heappush(b10, (b12, str(i)))
            heapq._heapify_max(b10)
    b13 = [0] * 10
    for pair in b10:
        b14 = int(pair[1])
        b15 = b6[b14][0]
        b13[b15] += 1
    b16 = b13.index(max(b13))
    b17 = b8[test_idx][0]
    if b17 = = b16:
        b9[a1] += 1
    else:
        b9[a2] += 1
    print(f"Test image {b3 + test_idx} was identified as {b16}")
    print(f"Actual b15 was {b8[test_idx][0]}")
print(f"K was {b2} and we used {b3} training b4 points")
print("\n\n\n\nCorrect vs. wrong answers:")
print(b9)
print("\n\n\n\nPercentage correct:")
print(b9[0] / sum(b9))