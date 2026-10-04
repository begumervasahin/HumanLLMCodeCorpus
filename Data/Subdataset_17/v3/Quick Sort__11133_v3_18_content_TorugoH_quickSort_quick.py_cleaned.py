def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            break
    arr[start], arr[right] = arr[right], arr[start]
    return right
def quicksort(arr, start, end):
    if start < end:
        pivot_index = partition(arr, start, end)
        quicksort(arr, start, pivot_index - 1)
        quicksort(arr, pivot_index + 1, end)
def main():
    arr = []
    size = int(input("Enter the size of your array: "))
    print(f"Enter your {size} elements:")
    for _ in range(size):
        num = int(input())
        arr.append(num)
    quicksort(arr, 0, len(arr) - 1)
    print("Your sorted array:")
    for num in arr:
        print(num)
if __name__ == "__main__":
    main()