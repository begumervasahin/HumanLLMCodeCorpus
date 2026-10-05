def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
my_list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", my_list)
sorted_list_insertion = insertion_sort(my_list.copy())
print("Sorted list (Insertion Sort):", sorted_list_insertion)
sorted_list_bubble = bubble_sort(my_list.copy())
print("Sorted list (Bubble Sort):", sorted_list_bubble)