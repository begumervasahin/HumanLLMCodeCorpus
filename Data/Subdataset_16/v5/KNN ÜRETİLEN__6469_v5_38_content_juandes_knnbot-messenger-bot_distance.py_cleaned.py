import math
def fonk1(data1, data2):
    if len(data1) != len(data2):
        raise ValueError("Data points must have the same number of dimensions.")
    b1 = sum((a - b) ** 2 for a, b in zip(data1, data2))
    return math.sqrt(b1)
b2 = [2, 3, 4]
b3 = [5, 6, 7]
print("Distance:", fonk1(b2, b3))