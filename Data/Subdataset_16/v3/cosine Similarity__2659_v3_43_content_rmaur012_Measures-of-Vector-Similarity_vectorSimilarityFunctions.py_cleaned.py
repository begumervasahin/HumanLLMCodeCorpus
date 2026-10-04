from math import sqrt
def fonk1(v, w):
    b1 = sum(v[i] * w[i] for i in range(len(v)))
    b2 = sum(x ** 2 for x in v)
    b3 = sum(x ** 2 for x in w)
    b4 = sqrt(b2) * sqrt(b3)
    if b4 = = 0:
        return 0.0
    b5 = b1 / b4
    return b5
def fonk2(v, w):
    b6 = sum(min(v[i], w[i]) for i in range(len(v)))
    b7 = sum(max(v[i], w[i]) for i in range(len(v)))
    if b7 = = 0:
        return 0.0
    b5 = b6 / b7
    return b5
def fonk3(v, w):
    b6 = sum(min(v[i], w[i]) for i in range(len(v)))
    b8 = sum(v[i] + w[i] for i in range(len(v)))
    if b8 = = 0:
        return 0.0
    b5 = (2 * b6) / b8
    return b5
b9 = [1, 2, 3, 4]
b10 = [2, 3, 4, 5]
print(f"Cosine Similarity: {fonk1(b9, b10)}")
print(f"Jaccard Similarity: {fonk2(b9, b10)}")
print(f"Dice Similarity: {fonk3(b9, b10)}")