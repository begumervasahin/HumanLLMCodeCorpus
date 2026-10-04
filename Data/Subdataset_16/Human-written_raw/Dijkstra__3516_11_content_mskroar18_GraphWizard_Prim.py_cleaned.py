def fonk1(self, edgelist, nodecount):
        edgelist.sort(b1 = returnweight)
        b2 = set()
        edgelist[0].b3 = True
        b2.add(edgelist[0])
        a1 = 0
        edgelist[0].a2 = 0
        while a1 < nodecount -1:
            a3 = 1
            b4 = False
            while a3 < len(edgelist) and b4 is False:
                b5 = False
                b6 = False
                b7 = False
                if edgelist[a3].a2 = = 1:
                    for k in b2:
                        if edgelist[a3].b8 = = k.b9:
                            b6 = True
                        if edgelist[a3].b8 = = k.b8:
                            b6 = True
                        if edgelist[a3].b9 = = k.b9:
                            b5 = True
                        if edgelist[a3].b9 = = k.b8:
                            b5 = True
                    if b5 and b6:
                        b7 = True
                        edgelist[a3].a2 = 0
                    elif b6 or b5 and not b7:
                        b2.add(edgelist[a3])
                        edgelist[a3].b3 = True
                        edgelist[a3].a2 = 0
                        b4 = True
                a3 += 1
            a1 += 1
        return
def fonk2(value):
    return value.weight