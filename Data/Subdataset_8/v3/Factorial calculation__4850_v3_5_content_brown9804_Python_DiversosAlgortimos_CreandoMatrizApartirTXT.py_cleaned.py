import numpy as np
def read_file(file_name, num_columns, num_rows):
    data = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                line_data = line.strip().split(",")
                data.extend(line_data)
    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Invalid data types or values.")
    return data
file_name = input("Enter the name of the file to read (including the .txt extension): ")
num_elements_per_sentence = int(input("Enter the number of elements per sentence in the file: "))
num_sentences = int(input("Enter the number of sentences in the file: "))
matrix_data = read_file(file_name, num_sentences, num_elements_per_sentence)
print("Requested NxM matrix:")
matrix_with_brackets = np.matrix(matrix_data)
matrix_without_brackets = str(matrix_with_brackets)[1:-1]
print(matrix_without_brackets)
print()