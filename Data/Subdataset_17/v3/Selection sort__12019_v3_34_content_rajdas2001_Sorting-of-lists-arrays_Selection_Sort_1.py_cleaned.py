def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Step {i + 1}: {arr}")
def main():
    arr = [49, 25, 26, 2, 99]
    print("Original array:", arr)
    selection_sort(arr)
    print("Sorted array:", arr)
if __name__ == "__main__":
    main()