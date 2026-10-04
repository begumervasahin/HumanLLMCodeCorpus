def merge(a, l, r):
    i = j = n = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            a[n] = l[i]
            i += 1
        else:
            a[n] = r[j]
            j += 1
        n += 1
    while i < len(l):
        a[n] = l[i]
        i += 1
        n += 1
    while j < len(r):
        a[n] = r[j]
        j += 1
        n += 1
    return a
def merge_sort(a):
    if len(a) > 1:
        mid = len(a)
        left_half = a[:mid]
        right_half = a[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        merge(a, left_half, right_half)
if __name__ == "__main__":
    arr = [54, 45, 67, 12, 34, 98, 66]
    print("Array before sorting:", arr)
    merge_sort(arr)
    print("Array after sorting:", arr)