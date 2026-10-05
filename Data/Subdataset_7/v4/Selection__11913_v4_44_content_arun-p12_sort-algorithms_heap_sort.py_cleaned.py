'''
Heap sort:
- Time complexity: O(b5 log(b5))
- Build max heap from the input data such that the largest number is at the root node.
- Replace it with the last item in the heap, and also reduce the size of the heap by one.
- With the new item in the root node, run heapify again.
- The active list contains the unsorted numbers, with the largest number always at the root.
- The sorted list continues to grow on the passive side of the list.
'''
import common as c
def fonk1(b6, b1 = 0, desc=0):
    def fonk2(i, b5):
        b2 = i
        b3 = i * 2 + 1
        b4 = b3 + 1
        while b3 < b5 and b6[b3] > b6[b2]:
            b2 = b3
        while b4 < b5 and b6[b4] > b6[b2]:
            b2 = b4
        if b1 = = 2:
            print("  sub:", i, b5, " :: ", b6)
        if i != b2:
            b6[i], b6[b2] = c.swap(b6[i], b6[b2])
            fonk2(b2, b5 - 1)
    def fonk3():
        b5 = len(b6)
        for i in range((b5
            fonk2(i, b5)
            if b1:
                print("iter")
        for i in range(b5 - 1, 0, -1):
            b6[0], b6[i] = c.swap(b6[0], b6[i])
            fonk2(0, i)
            if b1:
                print("iter")
    fonk3()
    if desc:
        b6 = b6[::-1]
    return b6