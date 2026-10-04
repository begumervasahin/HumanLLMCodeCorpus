
arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
for i in range(0, 9):
    for j in range(0, 9):
        if arr[j] > arr[i]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print(arr)
print("\n")