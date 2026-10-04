def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start], arr[right] = arr[right], arr[start]
    return right
def quick_sort(arr, start, end):
    if start < end:
        pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)
def get_input_array():
    size = int(input("Enter the size of the array: "))
    print(f"Enter {size} elements:")
    return [int(input()) for _ in range(size)]
def main():
    arr = get_input_array()
    quick_sort(arr, 0, len(arr) - 1)
    print("Sorted array:")
    for num in arr:
        print(num)
if __name__ == "__main__":
    main()