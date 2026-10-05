import scipy.io as sio
import numpy as np
import heapq
def fonk1(x, y):
    return np.linalg.norm(x - y)
b1 = int(input("Please enter the number of nearest neighbors (b1): "))
b2 = int(input("Enter the number of pictures to use as training b3 (up to 10,000): "))
b3 = sio.loadmat('ML_hw1data.mat')
b4 = b3['X'][:b2]
b5 = b3['Y'][:b2]
b6 = b3['X'][b2:]
b7 = b3['Y'][b2:]
a1 = 0
a2 = 0
for test_idx, test_img in enumerate(b6):
    b8 = []
    for i in range(b2):
        b9 = b4[i]
        b10 = fonk1(b9, test_img)
        if len(b8) < b1:
            heapq.heappush(b8, (b10, str(i)))
            heapq._heapify_max(b8)
        elif b10 < b8[0][0]:
            heapq.heappop(b8)
            heapq.heappush(b8, (b10, str(i)))
            heapq._heapify_max(b8)
    b11 = [0] * 10
    for pair in b8:
        b12 = int(pair[1])
        b13 = b5[b12][0]
        b11[b13] += 1
    b14 = b11.index(max(b11))
    b15 = b7[test_idx][0]
    if b15 = = b14:
        a1 += 1
    else:
        a2 += 1
    print(f"Test image {b2 + test_idx} was identified as {b14}")
    print(f"Actual b13 was {b15}")
b16 = a1 + a2
b17 = (a1 / b16) * 100
print(f"K was {b1} and we used {b2} training b3 points")
print("\nCorrect vs. wrong answers:")
print(f"Correct: {a1}, Wrong: {a2}")
print("\nPercentage correct:")
print(b17)