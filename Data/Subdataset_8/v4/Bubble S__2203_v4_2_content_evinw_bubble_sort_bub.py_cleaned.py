def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
a = [100, 2993, 22, 1, 82, 11, 33]
bubble_sort(a)
print("Sorted:")
for i in range(len(a)):
    print("%d" % a[i], end=" ")