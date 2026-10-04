def merge(a, left, right):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1
def merge_sort(a):
    if len(a) > 1:
        mid = len(a)
        left_half = a[:mid]
        right_half = a[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        merge(a, left_half, right_half)
def main():
    arr = [54, 45, 67, 12, 34, 98, 66]
    print("Array before sorting:", arr)
    merge_sort(arr)
    print("Array after sorting:", arr)
if __name__ == "__main__":
    main()