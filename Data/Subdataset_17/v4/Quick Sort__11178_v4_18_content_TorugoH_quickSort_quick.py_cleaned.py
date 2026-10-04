def partition(arr, start, end):
    left = start
    right = end
    pivot = arr[start]
    while left < right:
        while left < right and arr[left] <= pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right
def quick_sort(arr, start, end):
    if start < end:
        pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)
def main():
    arr = []
    print("Enter the size of the array:")
    size = int(input())
    print(f"Enter {size} elements:")
    for _ in range(size):
        num = int(input())
        arr.append(num)
    print("Sorted array:")
    quick_sort(arr, 0, len(arr) - 1)
    for num in arr:
        print(num)
if __name__ == "__main__":
    main()