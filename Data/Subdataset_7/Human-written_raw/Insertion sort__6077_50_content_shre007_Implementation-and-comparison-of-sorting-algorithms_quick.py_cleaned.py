import statistics
def fonk1(b10,first,last) :
    b1 = b10[first]
    b2 = b10[last]
    b3 = (first + last)
    b4 = statistics.median([b1,b10[b3],b2])
    if b4 = = b1 :
        b5 = first
    elif b4 = = b2 :
        b5 = last
    else :
        b5 = b3
    b10[last],b10[b5] = b10[b5], b10[last]
    b6 = b10[last]
    b7 = first
    b8 = last-1
    while True:
        while b7<=b8 and b10[b7] <= b6:
            b7 = b7 + 1
        while b7<=b8 and b10[b8] >= b6:
            b8 = b8-1
        if b8<b7 :
            break
        else :
            b10[b7], b10[b8] = b10[b8], b10[b7]
    b10[first], b10[b8] = b10[b8], b10[first]
    return b8
def fonk2(b10,first,last) :
    if first<last :
        b9 = fonk1(b10,first,last)
        fonk2(b10,first,b9-1)
        fonk2(b10,b9+1,last)
b10 = [56,26,93,17,31,44]
b11 = len(b10)
fonk2(b10,0,b11-1)
print(b10)