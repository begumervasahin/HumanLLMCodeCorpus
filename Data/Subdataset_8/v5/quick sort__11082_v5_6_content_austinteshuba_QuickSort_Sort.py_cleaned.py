def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right
def quicksort(arr, start, end):
    if start < end:
        split = partition(arr, start, end)
        quicksort(arr, start, split - 1)
        quicksort(arr, split + 1, end)
    return arr
def main():
    with open("list.txt", "r") as file:
        myList = [int(line.strip()) for line in file.readlines()]
    sortedList = quicksort(myList, 0, len(myList) - 1)
    print(sortedList)
if __name__ == "__main__":
    main()