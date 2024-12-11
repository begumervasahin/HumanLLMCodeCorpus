import scipy.io as sio
import numpy as np
import heapq
def fonk1(b8):
    b1 = sio.loadmat(b8)
    return b1['X'], b1['Y']
def fonk2(x, y):
    return np.linalg.norm(x - y)
def fonk3(test_pixels, training_pixels, b11, b9):
    a1 = 0
    for test_idx, test_pixel in enumerate(test_pixels):
        b2 = []
        for i, train_pixel in enumerate(training_pixels):
            b3 = fonk2(train_pixel, test_pixel)
            if len(b2) < b9:
                heapq.heappush(b2, (b3, i))
            elif b3 < b2[0][0]:
                heapq.heappop(b2)
                heapq.heappush(b2, (b3, i))
        b4 = [0] * 10
        for _, idx in b2:
            b5 = b11[idx][0]
            b4[b5] += 1
        b6 = max(range(10), key=lambda x: b4[x])
        b7 = b12[test_idx][0]
        if b7 = = b6:
            a1 += 1
        print(f"Test image {len(training_pixels) + test_idx} was identified as {b6}")
        print(f"Actual b5 was {b7}")
    return a1
def fonk4():
    b8 = 'ML_hw1data.mat'
    b9 = int(input("Please enter the value of b9 for b9-nearest neighbors: "))
    b10 = int(input("How many images would you like to use as training b1? (There are 10,000 images in total): "))
    training_pixels, b11 = fonk1(b8)
    test_pixels, b12 = training_pixels[b10:], b11[b10:]
    a1 = fonk3(test_pixels, training_pixels[:b10], b11[:b10], b9)
    print(f"b9 was {b9} and we used {b10} training b1 points")
    print("\nCorrect vs. wrong answers:")
    print([a1, len(test_pixels) - a1])
    print("\nPercentage a1:")
    print(a1 / len(test_pixels))
if b13 = = "__main__":
    fonk4()