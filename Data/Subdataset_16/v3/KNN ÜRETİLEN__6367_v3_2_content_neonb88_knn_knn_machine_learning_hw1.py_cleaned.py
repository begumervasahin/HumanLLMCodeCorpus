import scipy.io as sio
import numpy as np
import heapq
def fonk1(x, y):
    return np.linalg.norm(x - y)
def fonk2(b9, b10, b12, b13, b14, b15):
    b1 = [0, 0]
    RIGHT, b2 = 0, 1
    for test_idx in range(len(b14)):
        b3 = []
        for i in range(len(b12)):
            b4 = fonk1(b12[i], b14[test_idx])
            if len(b3) < b9:
                heapq.heappush(b3, (b4, i))
                heapq._heapify_max(b3)
            elif b4 < b3[0][0]:
                heapq.heappop(b3)
                heapq.heappush(b3, (b4, i))
                heapq._heapify_max(b3)
        b5 = [0] * 10
        for _, idx in b3:
            b6 = b13[idx][0]
            b5[b6] += 1
        b7 = np.argmax(b5)
        b8 = b15[test_idx][0]
        if b8 = = b7:
            b1[RIGHT] += 1
        else:
            b1[b2] += 1
        print(f"Test image {b10 + test_idx} was identified as {b7}")
        print(f"Actual b6 was {b8}")
    return b1
def fonk3():
    b9 = int(input("Please type a b9 for how many nearest neighbors you want to compute: "))
    b10 = int(input("There are 10,000 pictures of numbers.\nHow many would you like to use as training b11? "))
    b11 = sio.loadmat('ML_hw1data.mat')
    b12 = b11['X'][:b10]
    b13 = b11['Y'][:b10]
    b14 = b11['X'][b10:]
    b15 = b11['Y'][b10:]
    b1 = fonk2(b9, b10, b12, b13, b14, b15)
    print(f"\nk was {b9}")
    print(f"We used {b10} training b11 points")
    print("\nCorrect vs. wrong answers:")
    print(b1)
    print("\nPercentage correct:")
    b16 = (b1[0] / sum(b1)) * 100
    print(f"{b16:.2f}%")
if b17 = = '__main__':
    fonk3()