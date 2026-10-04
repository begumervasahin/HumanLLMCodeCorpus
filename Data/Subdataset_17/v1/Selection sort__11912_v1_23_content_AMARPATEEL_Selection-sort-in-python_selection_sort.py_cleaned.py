def selection_sort(arr):
    for fillslot in range(len(arr) - 1, 0, -1):
        position_of_max = 0
        for location in range(1, fillslot + 1):
            if arr[location] > arr[position_of_max]:
                position_of_max = location
        arr[fillslot], arr[position_of_max] = arr[position_of_max], arr[fillslot]
if __name__ == "__main__":
    alist = [54, 45, 67, 12, 34, 98, 66]
    print("List before sorting:", alist)
    selection_sort(alist)
    print("List after sorting:", alist)