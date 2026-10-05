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
def quick_sort(arr, start, end):
    if start < end:
        split = partition(arr, start, end)
        quick_sort(arr, start, split - 1)
        quick_sort(arr, split + 1, end)
    return arr
def main():
    arr = [int(x) for x in open("list.txt", "r").readlines()]
    sorted_list = quick_sort(arr, 0, len(arr) - 1)
    print(sorted_list)
if __name__ == "__main__":
    main()