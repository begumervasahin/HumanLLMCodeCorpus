import numpy as np
def read_file(file_name, columns, rows):
    data = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                line_data = line.strip().split(",")
                data.extend(line_data)
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Error in data types or values.")
    return data
file_to_extract = input("Enter the name of the file to read with its extension (.txt): ")
rows = int(input("Enter the number of elements per sentence in the file (.txt): "))
columns = int(input("Enter the number of sentences in the file (.txt): "))
matrix = read_file(file_to_extract, columns, rows)
print("Requested NxM matrix:")
matrix_with_brackets = np.matrix(matrix)
matrix_without_brackets = str(matrix_with_brackets)[1:-1]
print(matrix_without_brackets)
print()