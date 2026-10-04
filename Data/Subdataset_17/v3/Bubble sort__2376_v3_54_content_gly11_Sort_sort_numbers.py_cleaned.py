def insertion_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
if __name__ == "__main__":
    sample_list = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:")
    print(sample_list)
    sorted_list_insertion = insertion_sort(sample_list.copy())
    print("\nSorted list using insertion sort:")
    print(sorted_list_insertion)
    sorted_list_bubble = bubble_sort(sample_list.copy())
    print("\nSorted list using bubble sort:")
    print(sorted_list_bubble)