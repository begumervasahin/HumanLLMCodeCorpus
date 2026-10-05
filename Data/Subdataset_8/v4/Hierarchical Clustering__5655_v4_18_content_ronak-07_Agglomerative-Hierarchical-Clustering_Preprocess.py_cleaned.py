import distance
import time
import numpy as np
def calculate_distance_matrix(seq):
    dist = np.zeros(shape=(len(seq), len(seq)))
    for i in range(len(seq)):
        for j in range(i):
            dist_ij = distance.levenshtein(seq[i], seq[j])
            dist[i][j] = dist_ij
            dist[j][i] = dist_ij
    return dist
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