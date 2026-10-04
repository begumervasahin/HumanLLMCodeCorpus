import scipy.io as sio
import numpy as np
import heapq
def fonk1(x, y):
    return np.linalg.norm(x - y)
def fonk2():
    b1 = int(input("Please type a b1 for how many nearest neighbors you want to compute: "))
    b2 = int(input("There are 10,000 pictures of numbers.\nHow many would you like to use as training b3? "))
    return b1, b2
def fonk3(b2):
    b3 = sio.loadmat('ML_hw1data.mat')
    b4 = b3['X'][:b2]
    b5 = b3['Y'][:b2]
    b6 = b3['X'][b2:]
    b7 = b3['Y'][b2:]
    return b4, b5, b6, b7
def fonk4(test_pixel, b4, b1):
    b8 = []
    for i, img in enumerate(b4):
        b9 = fonk1(img, test_pixel)
        if len(b8) < b1:
            heapq.heappush(b8, (b9, i))
        elif b9 < b8[0][0]:
            heapq.heappop(b8)
            heapq.heappush(b8, (b9, i))
    return b8
def fonk5(b8, b5):
    b10 = np.zeros(10, dtype=int)
    for _, idx in b8:
        b11 = b5[idx][0]
        b10[b11] += 1
    return np.argmax(b10)
def fonk6():
    b1, b2 = fonk2()
    b4, b5, b6, b7 = fonk3(b2)
    b12 = [0, 0]
    RIGHT, b13 = 0, 1
    for test_idx, test_pixel in enumerate(b6):
        b8 = fonk4(test_pixel, b4, b1)
        b14 = fonk5(b8, b5)
        b15 = b7[test_idx][0]
        if b15 = = b14:
            b12[RIGHT] += 1
        else:
            b12[b13] += 1
        print(f"Test image {b2 + test_idx} was identified as {b14}. Actual b11 was {b15}.")
    b16 = b12[RIGHT] / (b12[RIGHT] + b12[b13]) * 100
    print(f"\nk: {b1}")
    print(f"Number of training b3 points: {b2}")
    print("\nCorrect vs. wrong answers:")
    print(b12)
    print("\nPercentage correct:")
    print(f"{b16:.2f}%")
if b17 = = '__main__':
    fonk6()