import random
def partition(a, l, r):
    pivot = a[l]
    i = l
    j = r + 1
    while True:
        while True:
            i += 1
            if i >= len(a) or a[i] >= pivot:
                break
        while True:
            j -= 1
            if j < 0 or a[j] <= pivot:
                break
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j
def quicksort_helper(a, l, r):
    if l < r:
        s = partition(a, l, r)
        quicksort_helper(a, l, s - 1)
        quicksort_helper(a, s + 1, r)
def quicksort(a):
    quicksort_helper(a, 0, len(a) - 1)
if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(10)]
    print("Array before sorting:", arr)
    quicksort(arr)
    print("Array after sorting:", arr)