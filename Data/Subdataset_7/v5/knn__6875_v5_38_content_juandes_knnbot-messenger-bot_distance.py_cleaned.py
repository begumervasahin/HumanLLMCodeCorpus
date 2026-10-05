import math
def fonk1(data1, data2):
    b1 = [(a - b) ** 2 for a, b in zip(data1, data2)]
    b2 = math.sqrt(sum(b1))
    return b2