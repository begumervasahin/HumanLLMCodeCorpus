import scipy.io as sio
import numpy as np
import heapq
def fonk1(x, y):
    b1 = x - y
    return np.linalg.norm(b1)
b2 = int(input("Please enter the number of nearest neighbors (b2): "))
b3 = int(input("Enter the number of pictures to use as training b4 (up to 10,000): "))
b4 = sio.loadmat('ML_hw1data.mat')
b5 = b4['X'][:b3]
b6 = b4['Y'][:b3]
b7 = b4['X'][b3:]
b8 = b4['Y'][b3:]
a1 = 0
a2 = 0
for test_idx, test_img in enumerate(b7):
    b9 = []
    for i in range(100):
        b10 = b5[i]
        b11 = fonk1(b10, test_img)
        if len(b9) < b2:
            heapq.heappush(b9, (b11, str(i)))
            heapq._heapify_max(b9)
        elif b11 < b9[0][0]:
            heapq.heappop(b9)
            heapq.heappush(b9, (b11, str(i)))
            heapq._heapify_max(b9)
    b12 = [0] * 10
    for pair in b9:
        b13 = int(pair[1])
        b14 = b6[b13][0]
        b12[b14] += 1
    b15 = b12.index(max(b12))
    b16 = b8[test_idx][0]
    if b16 = = b15:
        a1 += 1
    else:
        a2 += 1
    print(f"Test image {b3 + test_idx} was identified as {b15}")
    print(f"Actual b14 was {b16}")
b17 = a1 + a2
b18 = (a1 / b17) * 100
print(f"K was {b2} and we used {b3} training b4 points")
print("\nCorrect vs. wrong answers:")
print(f"Correct: {a1}, Wrong: {a2}")
print("\nPercentage correct:")
print(b18)