import time
def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr)
    left_half, left_comparisons = merge_sort(arr[:mid])
    right_half, right_comparisons = merge_sort(arr[mid:])
    merged_arr, merge_comparisons = merge(left_half, right_half)
    total_comparisons = left_comparisons + right_comparisons + merge_comparisons
    return merged_arr, total_comparisons
def merge(left, right):
    merged_arr = []
    i = j = 0
    comparisons = 0
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] < right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
    merged_arr.extend(left[i:])
    merged_arr.extend(right[j:])
    return merged_arr, comparisons
def print_list(arr):
    print(" ".join(map(str, arr)))
def main():
    start_time = time.time()
    with open("case", "r") as file:
        arr = list(map(int, file.read().split()))
    sorted_arr, total_comparisons = merge_sort(arr)
    print("Sorted array is:")
    print_list(sorted_arr)
    print(f"Total comparisons: {total_comparisons}")
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")
if __name__ == '__main__':
    main()