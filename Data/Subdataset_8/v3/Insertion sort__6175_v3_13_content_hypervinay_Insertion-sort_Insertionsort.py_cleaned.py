import time
import sys
def insertion_sort(input_list):
    for current_index in range(1, len(input_list)):
        current_value = input_list[current_index]
        position = current_index
        while position > 0 and input_list[position - 1] > current_value:
            input_list[position] = input_list[position - 1]
            position -= 1
        input_list[position] = current_value
def read_input_file(filename):
    with open(filename, 'r') as file:
        return [int(x) for x in file.read().split(',')]
def write_output_file(filename, sorted_list):
    with open(filename, 'w') as file:
        file.write(','.join(map(str, sorted_list)))
def main():
    if len(sys.argv) != 3:
        print("Incorrect Format!! Enter [filename].py [input file name] [output file name]")
        sys.exit()
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    input_list = read_input_file(input_filename)
    start_time = time.time()
    insertion_sort(input_list)
    print("Running time =", time.time() - start_time, "secs")
    write_output_file(output_filename, input_list)
if __name__ == "__main__":
    main()