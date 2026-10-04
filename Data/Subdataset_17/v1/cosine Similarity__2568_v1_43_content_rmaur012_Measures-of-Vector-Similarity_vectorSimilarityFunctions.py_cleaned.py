from math import sqrt
def simCosine(v, w):
    numeratorSum = 0
    vVectorSum = 0
    wVectorSum = 0
    for index, value in enumerate(v):
        numeratorSum += value * w[index]
        vVectorSum += value * value
        wVectorSum += w[index] * w[index]
    denominatorTotal = (sqrt(vVectorSum) * sqrt(wVectorSum))
    similarity = numeratorSum / denominatorTotal
    return similarity
def simJaccard(v, w):
    numeratorMinSum = 0
    denominatorMaxSum = 0
    for index, value in enumerate(v):
        if value <= w[index]:
            numeratorMinSum += value
        else:
            numeratorMinSum += w[index]
        if value >= w[index]:
            denominatorMaxSum += value
        else:
            denominatorMaxSum += w[index]
    similarity = numeratorMinSum / denominatorMaxSum
    return similarity
def simDice(v, w):
    numeratorMinSum = 0
    denominatorSum = 0
    for index, value in enumerate(v):
        if value <= w[index]:
            numeratorMinSum += value
        else:
            numeratorMinSum += w[index]
        denominatorSum += (value + w[index])
    similarity = (2 * numeratorMinSum) / denominatorSum
    return similarity
v1 = [1, 2, 3, 4]
v2 = [2, 3, 4, 5]
print(f"Cosine Similarity: {simCosine(v1, v2)}")
print(f"Jaccard Similarity: {simJaccard(v1, v2)}")
print(f"Dice Similarity: {simDice(v1, v2)}")