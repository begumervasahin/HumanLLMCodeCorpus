import numpy as np
def fonk1(file_name, b5, b4):
    b1 = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                b2 = line.strip().split(",")
                b1.extend(b2)
    except FileNotFoundError:
        print("File not found.")
    except ValueError:
        print("Error in b1 types or values.")
    return b1
b3 = input("Enter the name of the file to read with its extension (.txt): ")
b4 = int(input("Enter the number of elements per sentence in the file (.txt): "))
b5 = int(input("Enter the number of sentences in the file (.txt): "))
b6 = fonk1(b3, b5, b4)
print("Requested NxM b6:")
b7 = np.b6(b6)
b8 = str(b7)[1:-1]
print(b8)
print()