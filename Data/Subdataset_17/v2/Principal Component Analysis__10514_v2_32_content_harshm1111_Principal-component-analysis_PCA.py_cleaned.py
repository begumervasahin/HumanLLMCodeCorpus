import numpy as np
from scipy.spatial import distance
from sklearn.decomposition import PCA
def get_distance(distance_type, a, b):
    if distance_type == 1:
        return distance.minkowski(a, b, p=1)
    elif distance_type == 2:
        return distance.minkowski(a, b, p=2)
    elif distance_type == 3:
        return distance.minkowski(a, b, p=float('inf'))
    else:
        return distance.cosine(a, b)
def get_pca_vectors(number_components, P_data, other_patient_data):
    train_data = np.array([P_data] + other_patient_data)
    pca = PCA(n_components=number_components)
    pca.fit(train_data)
    P_data_transformed = pca.transform([P_data])[0]
    other_patient_data_transformed = pca.transform(other_patient_data)
    return P_data_transformed, other_patient_data_transformed, pca.explained_variance_
def get_index_list(P_data, other_patient_data, distance_type, X):
    if X != -1:
        P_data, other_patient_data, variance = get_pca_vectors(X, P_data, other_patient_data)
    distance_list = [(i, get_distance(distance_type, P_data, other_patient_data[i])) for i in range(len(other_patient_data))]
    closest_patients = sorted(distance_list, key=lambda x: x[1])[:5]
    for patient in closest_patients:
        print(patient[0] + 1)
    if X != -1:
        print(sum(variance))
def main():
    D = int(input("Enter the value for D: "))
    N = int(input("Enter the value for N: "))
    distance_type = int(input("Enter the distance type: "))
    X = int(input("Enter the value for X: "))
    P_data = list(map(int, input("Enter the P_data values: ").split()))
    other_patient_data = [list(map(int, input(f"Enter the data for patient {i + 1}: ").split())) for i in range(N)]
    get_index_list(P_data, other_patient_data, distance_type, X)
if __name__ == "__main__":
    main()