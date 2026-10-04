import time
import sys
def insertion_sort_list(input_list):
    for i in range(1, len(input_list)):
        item = input_list[i]
        pointer = i
        while pointer > 0 and input_list[pointer - 1] > item:
            input_list[pointer] = input_list[pointer - 1]
            pointer -= 1
        input_list[pointer] = item
if len(sys.argv) != 3:
    print("Incorrect Format!! Enter [filename].py [input file name] [Output file name]")
    sys.exit(1)
try:
    with open(sys.argv[1], 'r') as f:
        input_list = [int(x) for x in f.read().split(',')]
except FileNotFoundError:
    print("Input file not found.")
    sys.exit(1)
except ValueError:
    print("Error in input file format.")
    sys.exit(1)
start_time = time.time()
insertion_sort_list(input_list)
end_time = time.time()
print(f"Running time = {end_time - start_time:.6f} secs")
try:
    with open(sys.argv[2], 'w') as fout:
        fout.write(','.join(map(str, input_list)))
except IOError:
    print("Error writing to output file.")
    sys.exit(1)