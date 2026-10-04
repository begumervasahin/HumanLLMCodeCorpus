from math import sqrt
def fonk1(v, w):
    a1 = 0
    a2 = 0
    a3 = 0
    for index, value in enumerate(v):
        a1 += value * w[index]
        a2 += value * value
        a3 += w[index] * w[index]
    b1 = (sqrt(a2) * sqrt(a3))
    b2 = a1 / b1
    return b2
def fonk2(v, w):
    a4 = 0
    a5 = 0
    for index, value in enumerate(v):
        if value <= w[index]:
            a4 += value
        else:
            a4 += w[index]
        if value >= w[index]:
            a5 += value
        else:
            a5 += w[index]
    b2 = a4 / a5
    return b2
def fonk3(v, w):
    a4 = 0
    a6 = 0
    for index, value in enumerate(v):
        if value <= w[index]:
            a4 += value
        else:
            a4 += w[index]
        a6 += (value + w[index])
    b2 = (2 * a4) / a6
    return b2
b3 = [1, 2, 3, 4]
b4 = [2, 3, 4, 5]
print(f"Cosine Similarity: {fonk1(b3, b4)}")
print(f"Jaccard Similarity: {fonk2(b3, b4)}")
print(f"Dice Similarity: {fonk3(b3, b4)}")