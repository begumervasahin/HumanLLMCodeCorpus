def bubble_sort(arr: list) -> None:
    n = len(arr)
    for passnum in range(n - 1, 0, -1):
        for i in range(passnum):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
def main() -> None:
    unsorted_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print("Unsorted list:", unsorted_list)
    bubble_sort(unsorted_list)
    print("Sorted list:", unsorted_list)
if __name__ == "__main__":
    main()