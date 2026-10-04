import time
from math import sqrt
def fonk1(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
def fonk2(b10, b8, b9, k):
    b1 = [(fonk1(b10, point), label) for point, label in zip(b8, b9)]
    b1.sort(b2 = lambda x: x[0])
    b3 = [label for _, label in b1[:k]]
    b4 = {label: b3.count(label) for label in set(b3)}
    b5 = max(b4, b2=b4.get)
    return b5
if b6 = = "__main__":
    b7 = time.time()
    b8 = [
        [1.0, 1.1],
        [1.0, 1.0],
        [0.0, 0.0],
        [0.0, 0.1]
    ]
    b9 = ['A', 'A', 'B', 'B']
    b10 = [1.0, 1.1]
    b11 = fonk2(b10, b8, b9, 3)
    print(f"Result: {b11}")
    print(f"Time taken: {time.time() - b7:.6f} seconds")