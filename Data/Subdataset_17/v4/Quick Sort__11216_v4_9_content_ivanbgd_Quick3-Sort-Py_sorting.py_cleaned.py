import random
def partition3(arr, left, right):
    pivot = arr[left]
    j, o = left, left
    for i in range(left + 1, right + 1):
        if arr[i] < pivot:
            o += 1
            arr[i], arr[o] = arr[o], arr[i]
            arr[j], arr[o] = arr[o], arr[j]
            j += 1
        elif arr[i] == pivot:
            o += 1
            arr[i], arr[o] = arr[o], arr[i]
    if j > left:
        arr[left], arr[j - 1] = arr[j - 1], arr[left]
    else:
        arr[left], arr[j] = arr[j], arr[left]
    return j, o
def randomized_quick_sort3(arr, left, right):
    if left >= right:
        return
    k = random.randint(left, right)
    arr[left], arr[k] = arr[k], arr[left]
    m1, m2 = partition3(arr, left, right)
    randomized_quick_sort3(arr, left, m1 - 1)
    randomized_quick_sort3(arr, m2 + 1, right)
if __name__ == '__main__':
    input_data = "5\n2 3 9 2 2"
    input_list = list(map(int, input_data.split()))
    n = input_list[0]
    arr = input_list[1:]
    randomized_quick_sort3(arr, 0, n - 1)
    print("Sorted array:", arr)