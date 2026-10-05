import numpy as np
with open("distance2.csv", "r+") as file:
    data = [0, ",", 1]
    file.write(str(data))
    file.write("hello\n")
    file.write(str(data))
    similarity_matrix = np.zeros((2, 2))
    similarity_matrix[1][0] = 2
    similarity_matrix[0][1] = similarity_matrix[1][0]
    similarity_matrix[1][0] -= 1
    print("Modified values:", similarity_matrix[1][0], similarity_matrix[0][1])