def partition(arr, start, end):
    left = start
    right = end
    pivot = arr[start]
    while left < right:
        while left < len(arr) and arr[left] <= pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right
def quicksort(arr, start, end):
    if start < end:
        pivot_index = partition(arr, start, end)
        quicksort(arr, start, pivot_index - 1)
        quicksort(arr, pivot_index + 1, end)
if __name__ == "__main__":
    arr = []
    print("Enter the size of your array:")
    size = int(input())
    print(f"Enter your {size} elements:")
    for i in range(size):
        num = int(input())
        arr.append(num)
    print("Your sorted array:")
    quicksort(arr, 0, len(arr) - 1)
    for num in arr:
        print(num)