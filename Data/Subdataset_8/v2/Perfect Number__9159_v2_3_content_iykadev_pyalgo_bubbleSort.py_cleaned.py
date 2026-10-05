def bubble_sort(arr):
    for pass_num in range(len(arr) - 1, 0, -1):
        for i in range(pass_num):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
test_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(test_list)
print(test_list)
