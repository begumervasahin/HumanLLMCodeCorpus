def insertion_sort(arr: list) -> None:
    for index in range(1, len(arr)):
        current_value = arr[index]
        position = index
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_value
def main() -> None:
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertion_sort(alist)
    print("Sorted list:", alist)
if __name__ == "__main__":
    main()