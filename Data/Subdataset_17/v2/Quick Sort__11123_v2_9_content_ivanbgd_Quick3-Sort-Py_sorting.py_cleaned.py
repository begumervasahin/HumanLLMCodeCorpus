import random
def partition3(arr, left, right):
    pivot = arr[left]
    less = left
    equal = left
    for i in range(left + 1, right + 1):
        if arr[i] < pivot:
            less += 1
            arr[i], arr[less] = arr[less], arr[i]
            arr[less], arr[equal] = arr[equal], arr[less]
            equal += 1
        elif arr[i] == pivot:
            equal += 1
            arr[i], arr[equal] = arr[equal], arr[i]
    if less > left:
        arr[left], arr[less - 1] = arr[less - 1], arr[left]
    else:
        arr[left], arr[less] = arr[less], arr[left]
    return less, equal
def randomized_quick_sort3(arr, left, right):
    if left >= right:
        return
    pivot_index = random.randint(left, right)
    arr[left], arr[pivot_index] = arr[pivot_index], arr[left]
    m1, m2 = partition3(arr, left, right)
    randomized_quick_sort3(arr, left, m1 - 1)
    randomized_quick_sort3(arr, m2 + 1, right)
def main():
    input_data = "5\n2 3 9 2 2"
    input_data = list(map(int, input_data.split()))
    n = input_data[0]
    arr = input_data[1:]
    randomized_quick_sort3(arr, 0, n - 1)
    print("Sorted array:", arr)
if __name__ == '__main__':
    main()