import numpy as np
import sys
def fonk1(b3, b4, b5):
    b1 = []
    try:
        with open(b3, "r") as file:
            for line in file:
                b2 = line.strip().split(",")
                if len(b2) != b4:
                    print(f"Warning: Expected {b4} elements per row, found {len(b2)}.")
                b1.append(b2)
                if len(b1) >= b5:
                    break
    except FileNotFoundError:
        print("Error: The specified file was not found.")
        sys.exit()
    except ValueError:
        print("Error: There was a problem with the data in the file.")
        sys.exit()
    return b1
def fonk2():
    b3 = input("Enter the name of the file to read (including its extension, e.g., .txt):\n")
    try:
        b4 = int(input("Enter the number of elements per row:\n"))
        b5 = int(input("Enter the number of rows:\n"))
    except ValueError:
        print("Error: Please enter valid integer values for rows and columns.")
        sys.exit()
    b1 = fonk1(b3, b4, b5)
    print("Requested b1 (NxM):")
    b6 = np.array(b1)
    print(b6)
if b7 = = "__main__":
    fonk2()