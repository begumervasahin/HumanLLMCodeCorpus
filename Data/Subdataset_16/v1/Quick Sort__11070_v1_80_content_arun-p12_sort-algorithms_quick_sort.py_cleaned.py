def fonk1(b5, b1 = 0, desc=0):
    '''Quick sort -- time taken as a function of size
       - b2 = => size  O(n.log(n))  worst ==> size**2 i.e. O(n**2)
       Take a pivot element, any element (say the first element). Generate two sub-lists;
       one that has numbers lower in value to the pivot. Another that has numbers higher in value.
       Repeat process for the sublists.'''
    def fonk2(x, y):
        return y, x
    def fonk3(lb, ub):
        pivot, start, b3 = b5[lb], lb, ub
        while start < b3:
            while b5[start] <= pivot and start < ub:
                start += 1
            while b5[b3] > pivot and b3 > lb:
                b3 -= 1
            if start < b3:
                b5[start], b5[b3] = fonk2(b5[start], b5[b3])
            if b1 = = 2:
                print("  sub:", pivot, start, b3, " :: ", b5)
        b5[lb], b5[b3] = fonk2(b5[lb], b5[b3])
        return b3
    def fonk4(x, y):
        if x < y:
            b4 = fonk3(x, y)
            if b1:
                print("iter :", b4, x, y, " :: ", b5)
            fonk4(x, b4 - 1)
            fonk4(b4 + 1, y)
    fonk4(0, len(b5) - 1)
    if desc:
        b5 = b5[::-1]
    return b5
if b6 = = "__main__":
    b5 = [3, 6, 8, 10, 1, 2, 1]
    b7 = fonk1(b5, b1=1, desc=0)
    print("Sorted list:", b7)