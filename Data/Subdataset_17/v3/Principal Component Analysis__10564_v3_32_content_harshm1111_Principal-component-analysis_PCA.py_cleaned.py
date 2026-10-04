import numpy as np
from scipy.spatial import distance
from sklearn.decomposition import PCA
def get_input_data():
    D = int(input("Enter the number of features (D): "))
    N = int(input("Enter the number of patients (N): "))
    distance_type = int(input("Enter the distance type (1: Manhattan, 2: Euclidean, 3: Chebyshev, 4: Cosine): "))
    X = int(input("Enter the number of principal components (X, enter -1 if no PCA is needed): "))
    P_data = list(map(int, input("Enter the primary patient's data: ").split()))
    other_patient_data = [list(map(int, input(f"Enter data for patient {i+1}: ").split())) for i in range(N)]
    return D, N, distance_type, X, P_data, other_patient_data
def calculate_distance(distance_type, a, b):
    if distance_type == 1:
        return distance.minkowski(a, b, p=1)
    elif distance_type == 2:
        return distance.minkowski(a, b, p=2)
    elif distance_type == 3:
        return distance.minkowski(a, b, p=float('inf'))
    else:
        return distance.cosine(a, b)
def apply_pca(number_components, P_data, other_patient_data):
    train_data = np.array([P_data] + other_patient_data)
    pca = PCA(n_components=number_components)
    pca.fit(train_data)
    P_data_transformed = pca.transform([P_data])[0]
    other_data_transformed = [pca.transform([patient])[0] for patient in other_patient_data]
    return P_data_transformed, other_data_transformed, pca.explained_variance_
def find_closest_patients(P_data, other_patient_data, distance_type, X):
    if X != -1:
        P_data, other_patient_data, variance = apply_pca(X, P_data, other_patient_data)
    distance_list = [(i, calculate_distance(distance_type, P_data, patient_data)) for i, patient_data in enumerate(other_patient_data)]
    closest_patients = sorted(distance_list, key=lambda x: x[1])[:5]
    for patient in closest_patients:
        print(patient[0] + 1)
    if X != -1:
        print(sum(variance))
def main():
    D, N, distance_type, X, P_data, other_patient_data = get_input_data()
    find_closest_patients(P_data, other_patient_data, distance_type, X)
if __name__ == "__main__":
    main()