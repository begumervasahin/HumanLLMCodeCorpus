'''
Heap sort -- time taken as a function of b1 = => b1 * log(b1)  i.e. O(b6 log(b6))
Build max heap from the input data such that the largest number is at the root node
Replace it with the last item in the heap, and also reduce the b1 of the heap by one.
With the new item in the root node, run heapify again.
The active list contains the unsorted numbers, with the largest number always at the root
And the sorted list continues to grow on the passive side of the list.
'''
def fonk1(b7, b2 = 0, desc=0):
    import common as c
    def fonk2(i, b6):
        b3 = i
        b4 = i*2 + 1
        b5 = b4 + 1
        while((b4 < b6) and (b7[b4] > b7[b3])):
            b3 = b4
        while((b5 < b6) and (b7[b5] > b7[b3])):
            b3 = b5
        if(b2 = = 2): print("  sub:", i, b6, " :: ", b7)
        if(i != b3):
            b7[i], b7[b3] = c.swap(b7[i], b7[b3])
            fonk2(b3, b6-1)
    def fonk3():
        b6 = len(b7)
        for i in range((b6
            fonk2(i, b6)
            if(b2): print("iter
        for i in range(b6-1, 0, -1):
            b7[0], b7[i] = c.swap(b7[0], b7[i])
            fonk2(0, i)
            if(b2): print("iter
    fonk3()
    if(desc): b7 = b7[::-1]
    return(b7)