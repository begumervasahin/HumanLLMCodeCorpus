import random
import time
def generate_numbers(filename, n):
    random.seed(0)
    with open(filename, 'w') as file:
        for _ in range(n):
            file.write(f"{random.randrange(0, 100)}\n")
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
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
def analyze_sorting(input_file, output_file, sorting_algorithm):
    start_time = time.time()
    with open(input_file, 'r') as file:
        values = [int(line.strip()) for line in file]
    input_time = time.time() - start_time
    print(f"Input time: {input_time:.6f} seconds")
    sorted_values = sorting_algorithm(values)
    sorting_time = time.time() - start_time - input_time
    print(f"Sorting time: {sorting_time:.6f} seconds")
    with open(output_file, 'w') as file:
        for value in sorted_values:
            file.write(f"{value}\n")
    output_time = time.time() - start_time - input_time - sorting_time
    print(f"Output time: {output_time:.6f} seconds")
    total_time = time.time() - start_time
    print(f"Total time: {total_time:.6f} seconds\n")
if __name__ == '__main__':
    input_filename = input("Enter the filename: ")
    num_values = int(input("Enter number of values: "))
    generate_numbers(input_filename, num_values)
    output_filename = input("Please enter output file name: ")
    analyze_sorting(input_filename, output_filename, merge_sort)
    analyze_sorting(input_filename, output_filename, selection_sort)