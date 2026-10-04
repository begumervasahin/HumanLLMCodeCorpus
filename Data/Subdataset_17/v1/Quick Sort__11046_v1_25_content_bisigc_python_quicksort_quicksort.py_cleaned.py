def quickSort(A, l, r):
    if l < r:
        pivot = A[l]
        s = l
        for i in range(l + 1, r):
            if A[i] < pivot:
                s = s + 1
                A[s], A[i] = A[i], A[s]
        A[l], A[s] = A[s], A[l]
        quickSort(A, l, s - 1)
        quickSort(A, s + 1, r)
def main():
    A = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
    print("Original array:", A)
    quickSort(A, 0, len(A))
    print("Sorted array:", A)
if __name__ == "__main__":
    main()