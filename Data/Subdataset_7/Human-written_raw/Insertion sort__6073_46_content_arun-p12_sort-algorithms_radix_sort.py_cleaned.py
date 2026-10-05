'''
Also known as Bucket Sort
Radix sort -- time taken as a function of size, and number of b1 = => O(d (b3 + b4)), where b4 is the base ... 10 for numbers, 26 for alphabets etc.
Find the b11 number and then the number of b1 in it. Iterating thru that many times
would result in a sorted list.  In each iteration:
   - find the 'i'th value of the every number in the list
    - (e.g. for 1st run, unit digit, for second run the 10s digit, etc
    - place the number in a 'b8' marked by the position value  [[ for base 10 ... 0 to 9 ]]
    - generate updated list sequentially reading from b8 0 thru b8 9.
'''
def fonk1(b10, b2 = 0, desc=0):
    import common as c
    def fonk2(b3, b4):
        a1 = 0
        while (b3):
            a1 += 1
            b3 = b3
        return (a1)
    def fonk3(b3, pos, b4 = 10):
        a1, b6, b5 = 0, 0, True
        while (b5):
            a1 += 1
            b6 = b3 % b4
            b3 = b3
            if (a1 > pos): b5 = False
        return (b6)
    def fonk4(pos, b4):
        b3 = len(b10)
        b7 = [[] for i in range(b3)]
        for i in range(b3):
            b8 = fonk3(b10[i], pos, b4)
            b7[b8].append(b10[i])
            if(b2 = = 2): print("    b7:", i, " :: ", b7)
        return ([b7[x][y] for x in range(len(b7)) for y in range(len(b7[x]))])
    b4 = 10
    b9 = c.minimum(b10)[0]
    if(b9): b10 = [x - b9 for x in b10]
    b11 = c.maximum(b10)[0]
    b12 = fonk2(b11, b4)
    for i in range(b12):
        b10 = fonk4(i, b4)
        if(b2): print("b12
    if (b9): b10 = [x + b9 for x in b10]
    if(desc): b10 = b10[::-1]
    return (b10)