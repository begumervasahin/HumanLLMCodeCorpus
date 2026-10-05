def bubble_sort(arr):
    comparisons = 0
    for iteration in range(len(arr) - 1):
        print("\n", "-" * 50, "Iteration", iteration)
        for i in range(len(arr) - 1 - iteration):
            comparisons += 1
            print("\n", "*" * 80, "\nComparing", arr[i], arr[i + 1])
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                print("Swapped", arr[i], arr[i + 1])
                print("Array is now", arr)
            else:
                print("No need to swap", arr[i], arr[i + 1])
    print("Number of comparisons =", comparisons)
    return arr
arr = [1, 5, 3, 2, 0, 8]
print(bubble_sort(arr))