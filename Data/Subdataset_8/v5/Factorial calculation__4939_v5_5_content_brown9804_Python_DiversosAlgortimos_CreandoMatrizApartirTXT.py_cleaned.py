import numpy as np
def read_file(file_name, columns, rows):
    data = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                line_data = line.strip().split(",")
                for _ in range(rows):
                    data.extend(line_data)
        file.close()
    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Invalid data types or values.")
    return data
file_name = input("Enter the name of the file to read (include the .txt extension): ")
rows = int(input("Enter the number of elements per sentence in the file (.txt): "))
columns = int(input("Enter the number of sentences in the file (.txt): "))
matrix = read_file(file_name, columns, rows)
print("Requested NxM matrix:")
matrix_with_brackets = np.matrix(matrix)
matrix_without_brackets = str(matrix_with_brackets)[1:-1]
print(matrix_without_brackets)
print()