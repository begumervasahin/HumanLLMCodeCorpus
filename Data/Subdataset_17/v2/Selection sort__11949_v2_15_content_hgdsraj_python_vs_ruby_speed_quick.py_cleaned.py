
arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
for i in range(len(arr)):
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("Sorted array:")
print(arr)