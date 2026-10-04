import time
import sys
def fonk1(b3):
    for i in range(1, len(b3)):
        b1 = b3[i]
        b2 = i
        while b2 > 0 and b3[b2 - 1] > b1:
            b3[b2] = b3[b2 - 1]
            b2 -= 1
        b3[b2] = b1
def fonk2(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            b3 = list(map(int, file.read().strip().split(',')))
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        sys.exit(1)
    except ValueError:
        print("Error: The input file contains non-integer values.")
        sys.exit(1)
    b4 = time.time()
    fonk1(b3)
    b5 = time.time()
    print(f"Sorting completed in {b5 - b4:.6f} seconds.")
    try:
        with open(output_file, 'w') as file:
            file.write(','.join(map(str, b3)))
    except IOError:
        print(f"Error: Unable to write to the file '{output_file}'.")
        sys.exit(1)
if b6 = = "__main__":
    if len(sys.argv) != 3:
        print("Usage: python <script_name>.py <input_file> <output_file>")
        sys.exit(1)
    b7 = sys.argv[1]
    b8 = sys.argv[2]
    fonk2(b7, b8)