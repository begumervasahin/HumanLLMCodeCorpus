def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_value
def main():
    example_array = [32, 13, 14, 15, 98]
    print("Original array:", example_array)
    insertion_sort(example_array)
    print("Sorted array:", example_array)
if __name__ == "__main__":
    main()