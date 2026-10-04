def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right
def quicksort(arr, start, end):
    global total_operations
    if start < end:
        total_operations += end - start
        split_point = partition(arr, start, end)
        total_operations += abs(start - (split_point - 1))
        quicksort(arr, start, split_point - 1)
        total_operations += abs((split_point + 1) - end)
        quicksort(arr, split_point + 1, end)
    return arr
def main():
    with open("list.txt", "r") as file:
        my_list = [int(x) for x in file.readlines()]
    sorted_list = quicksort(my_list, 0, len(my_list) - 1)
    print("Sorted List:", sorted_list)
    print("Total Operations:", total_operations)
if __name__ == "__main__":
    total_operations = 0
    main()