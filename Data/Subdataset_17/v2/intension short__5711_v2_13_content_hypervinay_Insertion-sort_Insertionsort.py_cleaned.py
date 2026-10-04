import time
import sys
def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        current_value = input_list[i]
        position = i
        while position > 0 and input_list[position - 1] > current_value:
            input_list[position] = input_list[position - 1]
            position -= 1
        input_list[position] = current_value
def main(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            input_list = list(map(int, file.read().strip().split(',')))
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        sys.exit(1)
    except ValueError:
        print("Error: The input file contains non-integer values.")
        sys.exit(1)
    start_time = time.time()
    insertion_sort(input_list)
    end_time = time.time()
    print(f"Sorting completed in {end_time - start_time:.6f} seconds.")
    try:
        with open(output_file, 'w') as file:
            file.write(','.join(map(str, input_list)))
    except IOError:
        print(f"Error: Unable to write to the file '{output_file}'.")
        sys.exit(1)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python <script_name>.py <input_file> <output_file>")
        sys.exit(1)
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    main(input_filename, output_filename)