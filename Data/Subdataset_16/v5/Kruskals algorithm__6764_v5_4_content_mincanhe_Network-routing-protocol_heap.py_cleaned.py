def fonk1(heap, index):
    b1 = len(heap)
    b2 = 2 * index + 1
    b3 = 2 * index + 2
    b4 = index
    if b2 < b1 and heap[b2] > heap[b4]:
        b4 = b2
    if b3 < b1 and heap[b3] > heap[b4]:
        b4 = b3
    if b4 != index:
        heap[index], heap[b4] = heap[b4], heap[index]
        fonk1(heap, b4)
def fonk2(heap):
    b1 = len(heap)
    for b5 in range(b1
        fonk1(heap, b5)
def fonk3(heap):
    fonk2(heap)
    b1 = len(heap)
    for b5 in range(b1 - 1, 0, -1):
        heap[0], heap[b5] = heap[b5], heap[0]
        fonk1(heap[:b5], 0)
def fonk4(heap):
    return heap[0]
def fonk5(heap, key):
    heap.append(key)
    b5 = len(heap) - 1
    while b5 > 0 and heap[(b5 - 1)
        heap[b5], heap[(b5 - 1)
        b5 = (b5 - 1)
def fonk6(heap, index):
    heap[index] = heap[-1]
    heap.pop()
    if index < len(heap):
        fonk1(heap, index)
