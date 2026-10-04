import time
import sys
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        current_value = numbers[i]
        position = i
        while position > 0 and numbers[position - 1] > current_value:
            numbers[position] = numbers[position - 1]
            position -= 1
        numbers[position] = current_value
def read_input_file(filename):
    try:
        with open(filename, 'r') as file:
            return list(map(int, file.read().strip().split(',')))
    except FileNotFoundError:
        sys.exit(f"Error: The file '{filename}' was not found.")
    except ValueError:
        sys.exit("Error: The input file contains non-integer values.")
def write_output_file(filename, data):
    try:
        with open(filename, 'w') as file:
            file.write(','.join(map(str, data)))
    except IOError:
        sys.exit(f"Error: Unable to write to the file '{filename}'.")
def main(input_file, output_file):
    input_list = read_input_file(input_file)
    start_time = time.time()
    insertion_sort(input_list)
    elapsed_time = time.time() - start_time
    print(f"Sorting completed in {elapsed_time:.6f} seconds.")
    write_output_file(output_file, input_list)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Usage: python <script_name>.py <input_file> <output_file>")
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    main(input_filename, output_filename)