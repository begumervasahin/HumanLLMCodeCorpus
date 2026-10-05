import time
comparison_count = 0
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        merge(arr, left_half, right_half)
def merge(arr, left_half, right_half):
    global comparison_count
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        comparison_count += 1
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        comparison_count += 1
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        comparison_count += 1
        arr[k] = right_half[j]
        j += 1
        k += 1
def print_list(arr):
    for num in arr:
        print(num, end=" ")
    print()
if __name__ == '__main__':
    start_time = time.time()
    with open("case") as file:
        input_list = list(map(int, file.read().split()))
    merge_sort(input_list)
    print("Sorted array:")
    print_list(input_list)
    print("Total comparisons:", comparison_count)
    end_time = time.time()
    print("Execution time:", end_time - start_time)