def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(test_list)
print(test_list)
