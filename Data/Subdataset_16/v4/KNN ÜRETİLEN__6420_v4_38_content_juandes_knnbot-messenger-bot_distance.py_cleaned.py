import math
def fonk1(data1, data2):
    b1 = zip(data1, data2)
    b2 = [(a - b) ** 2 for a, b in b1]
    return math.sqrt(sum(b2))
b3 = [2, 3, 4]
b4 = [5, 6, 7]
print("Distance:", fonk1(b3, b4))