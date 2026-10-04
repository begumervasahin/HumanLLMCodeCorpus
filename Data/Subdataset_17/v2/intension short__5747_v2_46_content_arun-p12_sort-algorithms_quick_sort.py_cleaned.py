def quick_sort(arr, verbose=0, descending=False):
    def partition(low, high):
        pivot = arr[low]
        left = low + 1
        right = high
        while True:
            while left <= right and arr[left] <= pivot:
                left += 1
            while left <= right and arr[right] > pivot:
                right -= 1
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                if verbose == 2:
                    print(f"Sub-array after swap: pivot={pivot}, left={left}, right={right} :: {arr}")
            else:
                break
        arr[low], arr[right] = arr[right], arr[low]
        return right
    def quicksort_recursive(low, high):
        if low < high:
            partition_idx = partition(low, high)
            if verbose:
                print(f"Partition index={partition_idx}, low={low}, high={high} :: {arr}")
            quicksort_recursive(low, partition_idx - 1)
            quicksort_recursive(partition_idx + 1, high)
    quicksort_recursive(0, len(arr) - 1)
    if descending:
        arr.reverse()
    return arr
if __name__ == "__main__":
    data = [24, 3, 45, 12, 56, 18, 39, 17, 8]
    sorted_data = quick_sort(data, verbose=1, descending=False)
    print("Sorted array:", sorted_data)