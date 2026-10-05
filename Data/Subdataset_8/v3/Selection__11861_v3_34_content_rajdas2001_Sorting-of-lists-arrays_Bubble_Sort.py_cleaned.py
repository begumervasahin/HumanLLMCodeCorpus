def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = [110, 34, 25, 32, 28, 10, 90]
bubble_sort(arr)
print("Sorted array:")
for num in arr:
    print(num)