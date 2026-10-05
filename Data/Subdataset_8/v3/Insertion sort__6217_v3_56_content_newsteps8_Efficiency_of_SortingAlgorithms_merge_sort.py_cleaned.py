import time
def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)
    left_half = arr[:mid]
    right_half = arr[mid:]
    merge_sort(left_half)
    merge_sort(right_half)
    merge(arr, left_half, right_half)
def merge(arr, left_half, right_half):
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
def print_list(arr):
    print(" ".join(map(str, arr)))
if __name__ == '__main__':
    start_time = time.time()
    with open("case", "r") as fp:
        arr = list(map(int, fp.read().split()))
    merge_sort(arr)
    print("Sorted array:")
    print_list(arr)
    end_time = time.time()
    print("Execution time:", end_time - start_time)