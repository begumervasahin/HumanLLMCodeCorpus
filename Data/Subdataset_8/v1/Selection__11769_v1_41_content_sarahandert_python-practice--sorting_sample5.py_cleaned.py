import random
import time
def generate_nums(filename, n):
    random.seed(0)
    with open(filename, 'w') as f:
        for _ in range(n):
            f.write(str(random.randrange(0, 100)) + "\n")
def merge(left, right):
    merged_list = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1
    merged_list.extend(left[left_index:])
    merged_list.extend(right[right_index:])
    return merged_list
def merge_sort(aList):
    if len(aList) <= 1:
        return aList
    else:
        mid = len(aList)
        left = merge_sort(aList[:mid])
        right = merge_sort(aList[mid:])
        return merge(left, right)
def selection_sort(aList):
    n = len(aList)
    for i in range(n - 1):
        smallNdx = i
        for j in range(i + 1, n):
            if aList[j] < aList[smallNdx]:
                smallNdx = j
        aList[i], aList[smallNdx] = aList[smallNdx], aList[i]
    return aList
def analyze_mergesort(inputfile, outputfile):
    start_input = time.time()
    with open(inputfile, 'r') as f:
        lst = [int(line.strip()) for line in f]
    end_input = time.time()
    start_sort = time.time()
    sorted_lst = merge_sort(lst)
    end_sort = time.time()
    start_output = time.time()
    with open(outputfile, 'w') as f:
        for num in sorted_lst:
            f.write(str(num) + "\n")
    end_output = time.time()
    total_time = end_output - start_input
    print(f"It took {end_input - start_input:.6f} seconds to input values from file {inputfile}")
    print(f"It took {end_sort - start_sort:.6f} seconds to sort {len(lst)} values using merge sort")
    print(f"It took {end_output - start_output:.6f} seconds to output {len(sorted_lst)} sorted values to file {outputfile}")
    print(f"Total time the program took is {total_time:.6f} seconds\n")
def analyze_selection(inputfile, outputfile):
    start_input = time.time()
    with open(inputfile, 'r') as f:
        lst = [int(line.strip()) for line in f]
    end_input = time.time()
    start_sort = time.time()
    sorted_lst = selection_sort(lst)
    end_sort = time.time()
    start_output = time.time()
    with open(outputfile, 'w') as f:
        for num in sorted_lst:
            f.write(str(num) + "\n")
    end_output = time.time()
    total_time = end_output - start_input
    print(f"It took {end_input - start_input:.6f} seconds to input values from file {inputfile}")
    print(f"It took {end_sort - start_sort:.6f} seconds to sort {len(lst)} values using selection sort")
    print(f"It took {end_output - start_output:.6f} seconds to output {len(sorted_lst)} sorted values to file {outputfile}")
    print(f"Total time the program took is {total_time:.6f} seconds\n")
def main():
    filename = input("Enter the filename: ")
    n = int(input("Enter number of values: "))
    generate_nums(filename, n)
    outputfile = input("Please enter output file name: ")
    analyze_mergesort(filename, outputfile)
    analyze_selection(filename, outputfile)
if __name__ == "__main__":
    main()