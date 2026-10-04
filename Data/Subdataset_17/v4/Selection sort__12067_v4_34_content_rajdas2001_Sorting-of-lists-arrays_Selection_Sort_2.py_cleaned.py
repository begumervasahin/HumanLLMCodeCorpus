def selection_sort(arr):
    n = len(arr)
    for fillslot in range(n - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fillslot + 1):
            if arr[location] > arr[position_of_max]:
                position_of_max = location
        arr[fillslot], arr[position_of_max] = arr[position_of_max], arr[fillslot]
def main():
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Unsorted array is:")
    print(arr)
    selection_sort(arr)
    print("Sorted array is:")
    for element in arr:
        print(element)
if __name__ == "__main__":
    main()