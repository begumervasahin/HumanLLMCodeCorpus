import math
def fonk1(b3, b4):
    b1 = zip(b3, b4)
    b2 = [pow(a - b, 2) for (a, b) in b1]
    return math.sqrt(sum(b2))
b3 = [1, 2, 3]
b4 = [4, 5, 6]
print(fonk1(b3, b4))
