import numpy as np
import sys
def read_file(file_name, num_columns, num_rows):
    matrix = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                line_values = line.strip().split(",")
                if len(line_values) != num_columns:
                    print(f"Warning: Expected {num_columns} elements per row, found {len(line_values)}.")
                matrix.append(line_values)
                if len(matrix) >= num_rows:
                    break
    except FileNotFoundError:
        print("Error: The specified file was not found.")
        sys.exit()
    except ValueError:
        print("Error: There was a problem with the data in the file.")
        sys.exit()
    return matrix
def main():
    file_name = input("Enter the name of the file to read (including its extension, e.g., .txt):\n")
    try:
        num_columns = int(input("Enter the number of elements per row in the file:\n"))
        num_rows = int(input("Enter the number of rows in the file:\n"))
    except ValueError:
        print("Error: Please enter valid integers for the number of columns and rows.")
        sys.exit()
    matrix = read_file(file_name, num_columns, num_rows)
    print("Requested matrix (NxM):")
    matrix_np = np.array(matrix)
    print(matrix_np)
if __name__ == "__main__":
    main()