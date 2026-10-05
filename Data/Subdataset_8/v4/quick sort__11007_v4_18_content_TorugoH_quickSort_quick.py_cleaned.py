def partition(arr, start, end):
    left = start
    right = end
    pivot = arr[start]
    while left < right:
        while arr[left] <= pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[start] = arr[right]
    arr[right] = pivot
    return right
def quick_sort(arr, start, end):
    if end > start:
        pivot_index = partition(arr, start, end)
        quick_sort(arr, start, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, end)
if __name__ == "__main__":
    size = int(input("Enter the size of your array: "))
    array = []
    print(f"Enter your {size} elements:")
    for i in range(size):
        number = int(input())
        array.append(number)
    print("Your sorted list:")
    quick_sort(array, 0, len(array) - 1)
    for element in array:
        print(element)