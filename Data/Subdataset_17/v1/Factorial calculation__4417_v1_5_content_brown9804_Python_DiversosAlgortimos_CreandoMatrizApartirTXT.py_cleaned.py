import numpy as np
def read_file(file_name, rows, cols):
    matrix = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                line_values = line.strip().split(",")
                if len(line_values) != rows:
                    print(f"Warning: Expected {rows} elements per row, found {len(line_values)}.")
                matrix.append(line_values)
                if len(matrix) > cols:
                    break
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit()
    except ValueError:
        print("Error: Data type value issue.")
        sys.exit()
    return matrix
def main():
    file_name = input("Enter the name of the file to read, including its extension (e.g., .txt):\n")
    try:
        rows = int(input("Enter the number of elements per row in the file:\n"))
        cols = int(input("Enter the number of rows in the file:\n"))
    except ValueError:
        print("Error: Please enter valid integers for rows and columns.")
        sys.exit()
    matrix = read_file(file_name, rows, cols)
    print("Requested matrix (NxM):")
    matrix_np = np.array(matrix)
    print(matrix_np)
if __name__ == "__main__":
    main()