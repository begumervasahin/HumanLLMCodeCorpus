def find_min_index(arr, start):
    min_idx = start
    for i in range(start + 1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = find_min_index(arr, i)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
arr = []
num_elements = int(input("Number of elements in the list: "))
for i in range(num_elements):
    num = int(input("Enter an element: "))
    arr.append(num)
print("List before sorting:", arr)
selection_sort(arr)
print("List after sorting:", arr)