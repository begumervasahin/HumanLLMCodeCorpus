import numpy as np
import distance
import time
def calculate_distance_matrix(seq, count):
    dist_matrix = np.zeros((count + 1, count + 1))
    values = []
    for i in range(count + 1):
        for j in range(i):
            if i != j:
                dist = distance.levenshtein(seq[i], seq[j])
                dist_matrix[i][j] = dist_matrix[j][i] = dist
                values.append(dist)
                print(f"Calculating distance for pair ({i}, {j})")
    values.sort()
    return dist_matrix
def preprocess_sequences(lines):
    seq = {}
    count = -1
    t = len(lines)
    i = 0
    while i < t:
        line = lines[i]
        if line.startswith('>'):
            r = ""
            i += 1
            while i < t and not lines[i].startswith('>'):
                r += lines[i]
                i += 1
            count += 1
            seq[count] = r
    return seq, count
def main():
    with open("data_amino2.txt", "r") as f:
        lines = f.read().splitlines()
    start_time = time.time()
    seq, count = preprocess_sequences(lines)
    print(f"Preprocessing done in {time.time() - start_time:.2f} seconds")
    start_time = time.time()
    distance_matrix = calculate_distance_matrix(seq, count)
    print(f"Distance Matrix Calculation done in {time.time() - start_time:.2f} seconds")
    np.save('distance_matrix.npy', distance_matrix)
    print("Distance matrix saved to 'distance_matrix.npy'")
if __name__ == "__main__":
    main()