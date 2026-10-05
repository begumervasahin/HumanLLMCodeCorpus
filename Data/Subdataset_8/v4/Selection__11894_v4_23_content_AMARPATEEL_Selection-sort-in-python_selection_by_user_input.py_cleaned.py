def selection_sort(arr):
    for i in range(0, len(arr)):
        min_idx = i
        print("Current minimum is:", arr[i])
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print("New minimum is:", arr[i])
        print(arr)
        print()
arr = []
num_elements = int(input("Number of elements in the list: "))
for i in range(0, num_elements):
    num = int(input("Enter an element: "))
    arr.append(num)
print("List before sorting:", arr)
selection_sort(arr)
print("List after sorting:", arr)