import time
comparison_count = 0
def merge_sort(arr):
    global comparison_count
    if len(arr) > 1:
        mid = len(arr)
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
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
    print(" ".join(map(str, arr)))
if __name__ == '__main__':
    start_time = time.time()
    with open("case", "r") as file:
        arr = list(map(int, file.read().split()))
    merge_sort(arr)
    print("Sorted array is:")
    print_list(arr)
    print(f"Total comparisons: {comparison_count}")
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")