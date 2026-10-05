import numpy as np
def fonk1(b3, num_columns, num_rows):
    b1 = []
    try:
        with open(b3, "r") as file:
            for line in file:
                b2 = line.strip().split(",")
                b1.extend(b2)
    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Invalid b1 types or values.")
    return b1
b3 = input("Enter the name of the file to read (including the .txt extension): ")
b4 = int(input("Enter the number of elements per sentence in the file: "))
b5 = int(input("Enter the number of sentences in the file: "))
b6 = fonk1(b3, b5, b4)
print("Requested NxM matrix:")
b7 = np.matrix(b6)
b8 = str(b7)[1:-1]
print(b8)
print()