def fonk1(b10, start, end):
    b1 = b10[start]
    b2 = start+1
    b3 = end
    b4 = False
    while not b4:
        while b2 <= b3 and b10[b2] <= b1:
            b2 = b2 + 1
        while b10[b3] >= b1 and b3 >=b2:
            b3 = b3 -1
        if b3 < b2:
            b4 = True
        else:
            b5 = b10[b2]
            b10[b2]=b10[b3]
            b10[b3]=b5
    b5 = b10[start]
    b10[start]=b10[b3]
    b10[b3]=b5
    return b3
a1 = 0
def fonk2(b10, start, end):
    global a1
    if start < end:
        a1+=end-start
        b6 = fonk3(b10, start, end)
        a1+=abs(start-(b6-1))
        fonk4(b10, start, b6-1)
        a1+=abs((b6+1)-end)
        fonk4(b10, b6+1, end)
    return b10
'''
def fonk3(b10, start, end):
    b1 = b10[start]
    print("b1!", b1)
    b7 = start+1
    b8 = start
    b3 = end
    b9 = False
    while b3>b8:
        print("compare", b1, b10[b3], b3, b8)
        if b10[b3]<b1:
             b10 = b10[:start] + [b10[b3]] + b10[start:]
             del b10[b3+1]
             b3+=1
                if b3!=len(b10)-1:
                    b10 = [b10[:b8]] + [b10[b3]]+ [b10[b8]] + [b10[b8+1:b3]] + [b10[b3+1:]]
                else:
                    b10 = b10[:b8] + [b10[b3]] + [b10[b8]] + [b10[b8+1:b3]]
             b8+=1
        b3-=1
        print(b10)
    return b8
def fonk4(b10, start, end):
    if end>start:
        b6 = fonk3(b10, start, end)
        fonk4(b10, start, b6-1)
        fonk4(b10, b6+1, end)
    return b10
'''
def fonk5():
    b10 = [int(x) for x in open("list.txt", "r").readlines()]
    b11 = fonk4(b10,0,len(b10)-1)
    print(b11)
fonk5()
print(a1)