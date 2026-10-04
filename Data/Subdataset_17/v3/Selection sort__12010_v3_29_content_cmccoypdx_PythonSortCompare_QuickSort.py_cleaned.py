import random
def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high + 1
    while True:
        while i < high and arr[i] < pivot:
            i += 1
        while j > low and arr[j] > pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j
def quicksort_helper(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort_helper(arr, low, pivot_index - 1)
        quicksort_helper(arr, pivot_index + 1, high)
def quicksort(arr):
    quicksort_helper(arr, 0, len(arr) - 1)
def main():
    arr = [random.randint(1, 100) for _ in range(10)]
    print("Array before sorting:", arr)
    quicksort(arr)
    print("Array after sorting:", arr)
if __name__ == "__main__":
    main()