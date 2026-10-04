def insertion_sort(arr):
    for index in range(1, len(arr)):
        current_value = arr[index]
        position = index
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_value
def main():
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Array before sorting:", arr)
    insertion_sort(arr)
    print("Sorted array:", arr)
if __name__ == "__main__":
    main()