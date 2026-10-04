def quick_sort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort(arr, left, pivot_index)
        quick_sort(arr, pivot_index + 1, right)
def partition(arr, left, right):
    pivot = arr[left]
    s = left
    for i in range(left + 1, right):
        if arr[i] < pivot:
            s += 1
            arr[s], arr[i] = arr[i], arr[s]
    arr[left], arr[s] = arr[s], arr[left]
    return s
def main():
    array = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print("Original array:", array)
    quick_sort(array, 0, len(array))
    print("Sorted array:", array)
if __name__ == "__main__":
    main()