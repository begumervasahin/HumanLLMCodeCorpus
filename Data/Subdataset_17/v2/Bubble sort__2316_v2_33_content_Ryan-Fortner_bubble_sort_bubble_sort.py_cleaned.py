arr = [1, 5, 3, 2, 0, 8]
def bubble_sort(arr):
    count = 0
    for j in range(len(arr) - 1):
        print("\n", "-" * 50, f"Iteration {j + 1}")
        for i in range(len(arr) - 1 - j):
            count += 1
            print("\n", "*" * 80)
            print(f"Comparing {arr[i]} and {arr[i + 1]}")
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                print(f"Swapped: {arr[i]} and {arr[i + 1]}")
                print("Array is now:", arr)
            else:
                print(f"No need to swap: {arr[i]} and {arr[i + 1]}")
    print("Number of evaluations =", count)
    return arr
sorted_arr = bubble_sort(arr)
print("\nSorted array:", sorted_arr)