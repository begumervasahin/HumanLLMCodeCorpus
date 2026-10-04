def quick_sort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quick_sort(arr, left, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, right)
def partition(arr, left, right):
    pivot = arr[left]
    store_index = left + 1
    for i in range(left + 1, right + 1):
        if arr[i] < pivot:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1
    store_index -= 1
    arr[left], arr[store_index] = arr[store_index], arr[left]
    return store_index
if __name__ == "__main__":
    array = [24, 3, 45, 29, 37, 12, 4]
    print("Original array:", array)
    quick_sort(array, 0, len(array) - 1)
    print("Sorted array:", array)