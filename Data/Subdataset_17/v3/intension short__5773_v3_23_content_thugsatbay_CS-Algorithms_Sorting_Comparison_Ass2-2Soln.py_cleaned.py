def quicksort_iterative(arr, start, end):
    stack = [(start, end)]
    while stack:
        start, end = stack.pop()
        pivot_index = partition(arr, start, end)
        if pivot_index - 1 > start:
            stack.append((start, pivot_index - 1))
        if pivot_index + 1 < end:
            stack.append((pivot_index + 1, end))
def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1
def find_special_value(arr):
    quicksort_iterative(arr, 0, len(arr) - 1)
    for i in range(len(arr)):
        remaining_elements = len(arr) - i
        if arr[i] == remaining_elements:
            print(arr[i])
            return
        elif arr[i] > remaining_elements:
            print(remaining_elements - 1)
            return
    print(len(arr))
def main():
    n = int(input("Enter the value of n: ").strip())
    arr_input = input("Enter array in the format {1,2,3}: ").strip()[1:-1]
    arr = list(map(int, arr_input.split(',')))
    if len(arr) == n:
        find_special_value(arr)
    else:
        print("The value of n and the size of the array don't match. Please validate your input.")
if __name__ == "__main__":
    main()