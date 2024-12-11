'''
Quick sort -- time taken as a function of size
    - b1 = => size  O(n.log(n))  worst ==> size**2 i.e. O(n**2)
Take a pivot element, any element (say the first element). Generate two sub-lists;
one that has numbers lower in value to the pivot. Another that has numbers higher in value.
Repeat process for the sublists.
'''
def fonk1(b5, b2 = 0, desc=0):
    import common as c
    def fonk2(lb, ub):
        pivot, start, b3 = b5[lb], lb, ub
        while(start < b3):
            while((b5[start] <= pivot) and (start < ub)): start += 1
            while ((b5[b3] > pivot) and (b3 > lb)): b3 -= 1
            if(start < b3):
                b5[start], b5[b3] = c.swap(b5[start], b5[b3])
            if(b2 = = 2): print("  sub:", pivot, start, b3, " :: ", b5)
        b5[lb], b5[b3] = c.swap(b5[lb], b5[b3])
        return(b3)
    def fonk3(x, y):
        if(x < y):
            b4 = fonk2(x, y)
            if(b2): print("iter :", b4, x, y, " :: ", b5)
            fonk3(x, b4-1)
            fonk3(b4+1, y)
    fonk3(0, len(b5) -1)
    if(desc): b5 = b5[::-1]
    return(b5)