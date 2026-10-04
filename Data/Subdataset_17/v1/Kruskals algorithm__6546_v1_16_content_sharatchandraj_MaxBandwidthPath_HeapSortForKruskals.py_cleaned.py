def heapify(H, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and H[i] > H[l]:
        largest = l
    if r < n and H[largest] > H[r]:
        largest = r
    if largest != i:
        H[i], H[largest] = H[largest], H[i]
        heapify(H, n, largest)
def heap_sort(H):
    n = len(H)
    for i in range(n
        heapify(H, n, i)
    for i in range(n - 1, 0, -1):
        H[i], H[0] = H[0], H[i]
        heapify(H, i, 0)
if __name__ == "__main__":
    H = [12, 11, 13, 5, 6, 7]
    print("Original array:", H)
    heap_sort(H)
    print("Sorted array:", H)