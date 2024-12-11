def fonk1(l, value, b1 = 0, b2 = -1):
    if not l: return -1
    if(b2 = = -1): b2 = len(l)-1
    if b1 = = b2:
        if l[b1] == value: return b1
        else: return -1
    b3 = (b1+b2)
    if l[b3] > value: return fonk1(l, value, b1, b3-1)
    elif l[b3] < value: return fonk1(l, value, b3+1, b2)
    else: return b3