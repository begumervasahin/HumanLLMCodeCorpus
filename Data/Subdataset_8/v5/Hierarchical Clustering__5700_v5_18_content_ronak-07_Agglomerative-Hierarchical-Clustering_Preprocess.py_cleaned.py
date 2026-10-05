import distance
import time
import numpy as np
def calculate_distance_matrix(sequences):
    num_sequences = len(sequences)
    dist_matrix = np.zeros(shape=(num_sequences, num_sequences))
    for i in range(num_sequences):
        for j in range(i):
            dist_ij = distance.levenshtein(sequences[i], sequences[j])
            dist_matrix[i][j] = dist_ij
            dist_matrix[j][i] = dist_ij
    return dist_matrix
def preprocess_sequences(lines):
    sequences = []
    current_sequence = ""
    for line in lines:
        if line.startswith('>'):
            if current_sequence:
                sequences.append(current_sequence)
            current_sequence = ""
        else:
            current_sequence += line.strip()
    if current_sequence:
        sequences.append(current_sequence)
    return sequences
if __name__ == "__main__":
    with open("data_amino2.txt", "r") as file:
        file_content = file.read()
    lines = file_content.splitlines()
    start_preprocessing = time.time()
    sequences = preprocess_sequences(lines)
    preprocessing_time = time.time() - start_preprocessing
    print("Preprocessing done in:", preprocessing_time, "seconds")
    start_calculation = time.time()
    distance_matrix = calculate_distance_matrix(sequences)
    calculation_time = time.time() - start_calculation
    print("Distance Matrix Calculation done in:", calculation_time, "seconds")
    np.save('distance_matrix.npy', distance_matrix)