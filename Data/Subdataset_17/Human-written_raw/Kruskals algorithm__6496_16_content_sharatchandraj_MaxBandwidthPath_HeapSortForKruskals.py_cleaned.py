def Heapify(H,n,i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and H[i] > H[l]:
        largest = l
    if r < n and H[largest] > H[r]:
        largest = r
    if largest != i:
        H[i], H[largest] = H[largest], H[i]
        Heapify(H, n, largest)
def HeapSort(H):
    n = len(H)
    for i in range(n, -1, -1):
        Heapify(H, n, i)
    for i in range(n - 1, 0, -1):
        H[i], H[0] = H[0], H[i]
        Heapify(H, i, 0)