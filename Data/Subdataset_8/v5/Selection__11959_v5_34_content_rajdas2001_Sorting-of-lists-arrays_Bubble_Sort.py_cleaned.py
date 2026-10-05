def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = [110, 34, 25, 32, 28, 10, 90]
bubble_sort(arr)
print("Sorted array is:")
for num in arr:
    print(num)