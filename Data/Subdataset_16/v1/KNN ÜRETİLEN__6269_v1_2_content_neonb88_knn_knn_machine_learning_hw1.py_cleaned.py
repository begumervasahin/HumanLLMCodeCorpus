import scipy.io as sio
import numpy as np
import heapq
def fonk1(x, y):
    return np.linalg.norm(x - y)
def fonk2():
    b1 = int(input("Please type a b1 for how many nearest neighbors you want to compute: "))
    b2 = int(input("There are 10,000 pictures of numbers.\nHow many would you like to use as training b3? "))
    b3 = sio.loadmat('ML_hw1data.mat')
    b4 = b3['X'][:b2]
    b5 = b3['Y'][:b2]
    b6 = b3['X'][b2:]
    b7 = b3['Y'][b2:]
    b8 = [0, 0]
    RIGHT, b9 = 0, 1
    for test_idx in range(len(b6)):
        b10 = []
        for i in range(len(b4)):
            b11 = fonk1(b4[i], b6[test_idx])
            if len(b10) < b1:
                heapq.heappush(b10, (b11, i))
                heapq._heapify_max(b10)
            elif b11 < b10[0][0]:
                heapq.heappop(b10)
                heapq.heappush(b10, (b11, i))
                heapq._heapify_max(b10)
        b12 = [0] * 10
        for _, idx in b10:
            b13 = b5[idx][0]
            b12[b13] += 1
        b14 = np.argmax(b12)
        b15 = b7[test_idx][0]
        if b15 = = b14:
            b8[RIGHT] += 1
        else:
            b8[b9] += 1
        print(f"Test image {b2 + test_idx} was identified as {b14}")
        print(f"Actual b13 was {b7[test_idx][0]}")
    print(f"b1 was {b1}")
    print(f"and we used {b2} training b3 points")
    print("\nCorrect vs. wrong answers:")
    print(b8)
    print("\nPercentage correct:")
    print((b8[RIGHT] / sum(b8)) * 100)
if b16 = = '__main__':
    fonk2()