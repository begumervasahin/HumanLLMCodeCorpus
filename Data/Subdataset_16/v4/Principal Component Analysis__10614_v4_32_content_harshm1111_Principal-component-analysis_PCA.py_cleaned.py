import numpy as np
from scipy.spatial import distance
from sklearn.decomposition import PCA
b1 = int(input("Enter the number of features (b1): "))
b2 = int(input("Enter the number of patients (b2): "))
b3 = int(input("Enter the distance type (1: Manhattan, 2: Euclidean, 3: Chebyshev, 4: Cosine): "))
b4 = int(input("Enter the number of principal components (b4, enter -1 if no PCA is needed): "))
b5 = list(map(int, input("Enter the primary patient's data: ").split()))
b6 = [list(map(int, input(f"Enter data for patient {i+1}: ").split())) for i in range(b2)]
def fonk1(b3, a, b):
    if b3 = = 1:
        return distance.minkowski(a, b, b7 = 1)
    elif b3 = = 2:
        return distance.minkowski(a, b, b7 = 2)
    elif b3 = = 3:
        return distance.minkowski(a, b, b7 = float('inf'))
    else:
        return distance.cosine(a, b)
def fonk2(number_components, b5, b6):
    b8 = np.array([b5] + b6)
    b9 = PCA(n_components=number_components)
    b9.fit(b8)
    b10 = b9.transform([b5])[0]
    b11 = [b9.transform([patient])[0] for patient in b6]
    return b10, b11, b9.explained_variance_
def fonk3(b5, b6):
    if b4 != -1:
        b5, b6, b12 = fonk2(b4, b5, b6)
    b13 = [(i, fonk1(b3, b5, patient_data)) for i, patient_data in enumerate(b6)]
    b13 = sorted(b13, key=lambda x: x[1])[:5]
    for each in b13:
        print(each[0] + 1)
    if b4 != -1:
        print(sum(b12))
fonk3(b5, b6)