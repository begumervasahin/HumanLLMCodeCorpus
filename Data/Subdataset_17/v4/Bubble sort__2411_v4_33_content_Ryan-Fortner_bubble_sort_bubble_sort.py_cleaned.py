arr = [1, 5, 3, 2, 0, 8]
def bubble_sort(arr):
    count = 0
    n = len(arr)
    for j in range(n - 1):
        print("\n\n", "-" * 50, "Iteration", j + 1)
        for i in range(n - 1 - j):
            count += 1
            print("\n", "*" * 80, "\nComparing", arr[i], "and", arr[i + 1])
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                print("Swapped", arr[i], "and", arr[i + 1])
                print("Array is now", arr)
            else:
                print("No need to swap", arr[i], "and", arr[i + 1])
    print("Number of evaluations =", count)
    return arr
print("Original array:", arr)
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)