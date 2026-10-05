import time
import sys
def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        item = input_list[i]
        pointer = i
        while pointer > 0 and input_list[pointer - 1] > item:
            input_list[pointer] = input_list[pointer - 1]
            pointer -= 1
        input_list[pointer] = item
def main():
    if len(sys.argv) != 3:
        print("Incorrect Format!! Enter [filename].py [input file name] [output file name]")
        sys.exit()
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    with open(input_filename, 'r') as f:
        input_list = [int(x) for x in f.read().split(',')]
    start_time = time.time()
    insertion_sort(input_list)
    print("Running time =", time.time() - start_time, "secs")
    with open(output_filename, 'w') as fout:
        fout.write(','.join(map(str, input_list)))
if __name__ == "__main__":
    main()