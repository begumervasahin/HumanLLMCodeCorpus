def quicksort_with_stack(arr, start, end):
    stack = [0] * (end - start + 1)
    top = 0
    stack[top] = start
    top += 1
    stack[top] = end
    while top >= 0:
        end = stack[top]
        top -= 1
        start = stack[top]
        top -= 1
        pivot_index = partition(arr, start, end)
        if pivot_index - 1 > start:
            top += 1
            stack[top] = start
            top += 1
            stack[top] = pivot_index - 1
        if pivot_index + 1 < end:
            top += 1
            stack[top] = pivot_index + 1
            top += 1
            stack[top] = end
def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1
def gq(arr):
    quicksort_with_stack(arr, 0, len(arr) - 1)
    print("---GQ---")
    for i in range(len(arr) - 1, -1, -1):
        current_index = len(arr) - i
        if current_index == arr[i]:
            print(arr[i])
            break
        elif current_index >= arr[i]:
            print(current_index - 1)
            break
        elif i == 0:
            print(len(arr))
def main():
    try:
        n = int(input("Enter value of n: ").strip())
        arr_input = input("Enter array (e.g., {1,2,3}): ").strip()[1:-1]
        arr = list(map(int, arr_input.split(',')))
        if len(arr) == n:
            gq(arr)
        else:
            print("N and array size don't match. Can't proceed. Validate your input. Exiting program.")
    except ValueError:
        print("Invalid input. Exiting program.")
if __name__ == "__main__":
    main()