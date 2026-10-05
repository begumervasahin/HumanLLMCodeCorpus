import math
def fonk1(b2, b3):
    b1 = [(a - b) ** 2 for a, b in zip(b2, b3)]
    return math.sqrt(sum(b1))
b2 = [1, 2, 3]
b3 = [4, 5, 6]
print(fonk1(b2, b3))
