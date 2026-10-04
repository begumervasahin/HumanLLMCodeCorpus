def quicksort_stack(arr, start, end):
    size = end - start + 1
    stack = [0] * size
    top = -1
    top += 1
    stack[top] = start
    top += 1
    stack[top] = end
    while top >= 0:
        end = stack[top]
        top -= 1
        start = stack[top]
        top -= 1
        pivot_index = start - 1
        pivot_value = arr[end]
        for j in range(start, end):
            if arr[j] <= pivot_value:
                pivot_index += 1
                arr[pivot_index], arr[j] = arr[j, arr[pivot_index]]
        arr[pivot_index + 1], arr[end] = arr[end, arr[pivot_index + 1]]
        pivot_index += 1
        if abs(start - pivot_index) < abs(end - pivot_index):
            if pivot_index + 1 < end:
                top += 1
                stack[top] = pivot_index + 1
                top += 1
                stack[top] = end
            if pivot_index - 1 > start:
                top += 1
                stack[top] = start
                top += 1
                stack[top] = pivot_index - 1
        else:
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
def gq(arr):
    quicksort_stack(arr, 0, len(arr) - 1)
    print("---GQ---")
    for x in range(len(arr) - 1, -1, -1):
        if len(arr) - x == arr[x]:
            print(arr[x])
            break
        elif len(arr) - x >= arr[x]:
            print(len(arr) - x - 1)
            break
        elif x == 0:
            print(len(arr))
def main():
    n = int(input("Enter value of n: ").strip())
    arr = list(map(int, input("Enter array: [Example: {1,2,3}]: ").strip()[1:-1].split(',')))
    if len(arr) == n:
        gq(arr)
    else:
        print("N and array size don't match, can't proceed. Validate your input. Exiting Program.")
if __name__ == "__main__":
    main()