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
def read_numbers_from_file(filename):
    with open(filename, 'r') as file:
        return [int(number) for number in file.read().strip().split(',')]
def write_numbers_to_file(filename, numbers):
    with open(filename, 'w') as file:
        file.write(','.join(map(str, numbers)))
def main(input_file, output_file):
    numbers = read_numbers_from_file(input_file)
    start_time = time.time()
    insertion_sort(numbers)
    elapsed_time = time.time() - start_time
    print(f"Sorting completed in {elapsed_time:.6f} seconds")
    write_numbers_to_file(output_file, numbers)
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)