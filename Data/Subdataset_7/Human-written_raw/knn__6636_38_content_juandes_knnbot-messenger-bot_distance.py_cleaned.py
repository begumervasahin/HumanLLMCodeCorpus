import math
def fonk1(data1, data2):
    b1 = zip(data1, data2)
    b2 = [pow(a - b, 2) for (a, b) in b1]
    return math.sqrt(sum(b2))