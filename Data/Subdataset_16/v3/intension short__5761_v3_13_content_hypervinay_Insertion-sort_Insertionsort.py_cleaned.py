import time
import sys
def fonk1(numbers):
    for i in range(1, len(numbers)):
        b1 = numbers[i]
        b2 = i
        while b2 > 0 and numbers[b2 - 1] > b1:
            numbers[b2] = numbers[b2 - 1]
            b2 -= 1
        numbers[b2] = b1
def fonk2(filename):
    try:
        with open(filename, 'r') as file:
            return list(map(int, file.read().strip().split(',')))
    except FileNotFoundError:
        sys.exit(f"Error: The file '{filename}' was not found.")
    except ValueError:
        sys.exit("Error: The input file contains non-integer values.")
def fonk3(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write(','.join(map(str, data)))
    except IOError:
        sys.exit(f"Error: Unable to write to the file '{filename}'.")
def fonk4(input_file, output_file):
    b3 = fonk2(input_file)
    b4 = time.time()
    fonk1(b3)
    b5 = time.time() - b4
    print(f"Sorting completed in {b5:.6f} seconds.")
    fonk3(output_file, b3)
if b6 = = "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python <script_name>.py <input_file> <output_file>")
    b7 = sys.argv[1]
    b8 = sys.argv[2]
    fonk4(b7, b8)