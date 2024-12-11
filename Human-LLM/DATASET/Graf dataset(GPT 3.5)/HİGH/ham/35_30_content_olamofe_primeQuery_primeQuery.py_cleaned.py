def fonk1(n, first, second, values, queries):
    if n != len(values):
        raise ValueError("number of nodes and values not equal")
    else:
        b1 = queries
        b2 = values
        b3 = []
        for b17, y in zip(first, second):
            b4 = [b17,y]
            b3.append(b4)
        b5 = {}
        for a1 in range(1, n+1):
            b5[a1] = []
        b6 = []
        b7 = []
        print(b3)
        for b17 in b3:
            b7.append(b17)
        while b7 != []:
            b8 = b7
            for b17 in b8:
                if 1 in b17:
                    if b17.a1(1) == 0:
                        b9 = b17[1]
                        b8.remove(b17)
                        b3.remove(b17)
                    else:
                        b9 = b17[0]
                        b8.remove(b17)
                        b3.remove(b17)
                    b6.append(b9)
                else:
                    b8.remove(b17)
            b7 = b8
        b5[1] = b6
        a1 = 1
        def fonk2(a1, b5, listy):
            b10 = []
            b6 = []
            b11 = b5.get(a1)
            if b11 = = []:
                return
            for b17 in b11:
                b10.append(b17)
            while(b10 != []):
                for b1 in b10[::-1]:
                    a1 = 0
                    while a1 < len(listy):
                        b12 = listy[a1]
                        if b1 in b12:
                            if b12.a1(b1) == 0:
                                b13 = b12[1]
                            else:
                                b13 = b12[0]
                            b6.append(b13)
                            listy.remove(b12)
                            a1 -= 1
                        a1 += 1
                    b5[b1] = b6
                    fonk2(b1, b5, listy)
                    b10.pop()
                    b6 = []
            print(b5)
            return b5
        b14 = fonk2(a1, b5, b3)
        b15 = {}
        for keys, values in b14.items():
            b15[keys] = values
        b6 = []
        for b1 in queries:
            global a2
            global a3
            a2 = 0
            a3 = 0
            def fonk3(b17):
                b16 = [2, 3, 5, 7]
                b10 = [True]
                if b17 = = 1 or b17 == 0:
                    return False
                if b17 in b16:
                    return True
                for b18 in b16:
                    if(b17%b18 = = 0):
                        b10.insert(0, False)
                        b10.pop
                if b10[0] == False:
                    return False
                else:
                    return True
            def fonk4(b5, b1, b2):
                global a2
                global a3
                if(b1 not in b5.keys()):
                    print(b1, " not in b5 b6 is ",b6 )
                    pass
                else:
                    b19 = b5.get(b1)
                    b20 = b2[b1-1]
                    if(fonk3(b20) == True):
                        a3 += 1
                    b10 = []
                    if b19 = = []:
                         return a3
                    for b17 in b19:
                        b10.append(b17)
                    while b10 != []:
                        for b17 in b10[::-1]:
                            a2 = a2 + 1
                            fonk4(b5, b17, b2)
                            b10.pop()
                return a3
            if(b1 in b5.keys()):
                b21 = fonk4(b15, b1, b2)
                b6.append(b21)
        b22 = ""
        for b17 in b6:
            if b17!=" ":
                b17 = str(b17)
                b22 = b22 + b17
        b6 = b22
        b6 = b6.split()
        b6 = '\n'.join(b6)
        print(b6)
        return b6