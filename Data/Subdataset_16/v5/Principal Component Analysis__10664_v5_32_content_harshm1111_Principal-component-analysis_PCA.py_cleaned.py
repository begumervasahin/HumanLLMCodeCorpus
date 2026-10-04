import numpy as np
from scipy.spatial import distance
from sklearn.decomposition import PCA
def fonk1(b1, a, b):
    if b1 = = 1:
        return distance.minkowski(a, b, b2 = 1)
    elif b1 = = 2:
        return distance.minkowski(a, b, b2 = 2)
    elif b1 = = 3:
        return distance.minkowski(a, b, b2 = float('inf'))
    else:
        return distance.cosine(a, b)
def fonk2(n_components, b13, b14):
    b3 = np.array([b13] + b14)
    b4 = PCA(n_components=n_components)
    b4.fit(b3)
    b5 = b4.transform([b13])[0]
    b6 = b4.transform(b14)
    return b5, b6, b4.explained_variance_
def fonk3(b13, b14, b1, b12):
    if b12 != -1:
        b13, b14, b7 = fonk2(b12, b13, b14)
    b8 = [
        (i, fonk1(b1, b13, b14[i]))
        for i in range(len(b14))
    ]
    b9 = sorted(b8, key=lambda x: x[1])[:5]
    for patient in b9:
        print(patient[0] + 1)
    if b12 != -1:
        print(sum(b7))
def fonk4():
    b10 = int(input("Enter the value for b10: "))
    b11 = int(input("Enter the value for b11: "))
    b1 = int(input("Enter the distance type: "))
    b12 = int(input("Enter the value for b12: "))
    b13 = list(map(int, input("Enter the b13 values: ").split()))
    b14 = [
        list(map(int, input(f"Enter the b3 for patient {i + 1}: ").split()))
        for i in range(b11)
    ]
    fonk3(b13, b14, b1, b12)
if b15 = = "__main__":
    fonk4()