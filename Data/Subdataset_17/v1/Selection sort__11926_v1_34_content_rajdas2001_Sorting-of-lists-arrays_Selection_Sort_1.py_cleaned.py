def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
def main():
    arr = [49, 25, 26, 2, 99]
    print("Original array:", arr)
    selection_sort(arr)
    print("Sorted array is:")
    for element in arr:
        print(element, end=' ')
if __name__ == "__main__":
    main()