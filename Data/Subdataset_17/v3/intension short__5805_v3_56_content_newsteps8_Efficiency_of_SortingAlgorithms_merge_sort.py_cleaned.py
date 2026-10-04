import time
def merge_sort(arr):
    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            merge_sort.comparison_count += 1
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    if len(arr) <= 1:
        return arr
    mid = len(arr)
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)
def print_list(arr):
    print(" ".join(map(str, arr)))
def main():
    start_time = time.time()
    with open("case", "r") as file:
        arr = file.read().split()
    array_to_sort = [int(num) for num in arr]
    merge_sort.comparison_count = 0
    sorted_array = merge_sort(array_to_sort)
    print("Sorted array is:")
    print_list(sorted_array)
    print(f"Number of comparisons: {merge_sort.comparison_count}")
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds")
if __name__ == "__main__":
    main()