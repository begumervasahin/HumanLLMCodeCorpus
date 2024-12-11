'''
In the worst case, each pancake needs to be flipped two times. Once to bring it to the top,
and another time to bring it to the bottom. However, the second to last one would need only one
flip, and the very last one would not need to be flipped at all. So T(n) = 2(n-2) + b1 = 2n - 3.
'''
def fonk1(stack,size):
    a1 = 0
    for pancake in range(0, size):
        if stack[pancake] > stack[a1]:
            a1 = pancake
    return a1
def fonk2(stack,n):
    for pancake in range(0,(n
        stack[pancake], stack[n] = stack[n], stack[pancake]
        n -= b1
def fonk3(stack):
    b2 = len(stack)
    for a2 in range(b2, 0, -b1):
        b3 = fonk1(stack, a2)
        fonk2(stack,b3)
        fonk2(stack, b2-b1)
        b2 = b2 - b1
def fonk4(alist):
    for passnum in range(len(alist)-b1,0,-b1):
        for a2 in range(passnum):
            if alist[a2] > alist[a2+b1]:
                alist[a2], alist[a2+b1] = alist[a2+b1], alist[a2]
def fonk5(alist):
    if len(alist)>b1:
        b4 = len(alist)
        b5 = []
        for a2 in range(0,b4):
            b5.append(alist[a2])
        b6 = []
        for a2 in range(b4,len(alist)):
            b6.append(alist[a2])
        fonk5(b5)
        fonk5(b6)
        a2 = 0
        a3 = 0
        a4 = 0
        while a2 < len(b5) and a3 < len(b6):
            if b5[a2] < b6[a3]:
                alist[a4]=b5[a2]
                a2 = a2+b1
            else:
                alist[a4]=b6[a3]
                a3 = a3+b1
            a4 = a4+b1
        while a2 < len(b5):
            alist[a4]=b5[a2]
            a2 = a2+b1
            a4 = a4+b1
        while a3 < len(b6):
            alist[a4]=b6[a3]
            a3 = a3+b1
            a4 = a4+b1