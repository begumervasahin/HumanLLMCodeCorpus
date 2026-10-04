__author__ = 's'
import numpy as np
def write_to_file(filename, data, message):
    with open(filename, "r+") as f:
        f.write(str(data))
        f.write(message)
        f.write("\n")
        f.write(str(data))
def create_and_modify_array():
    similarity = np.zeros((2, 2))
    similarity[1, 0] = 2
    similarity[0, 1] = similarity[1, 0]
    similarity[1, 0] -= 1
    return similarity[1, 0], similarity[0, 1]
if __name__ == "__main__":
    data = [0, ",", 1]
    message = "hello"
    write_to_file("distance2.csv", data, message)
    modified_values = create_and_modify_array()
    print(modified_values[0], modified_values[1])