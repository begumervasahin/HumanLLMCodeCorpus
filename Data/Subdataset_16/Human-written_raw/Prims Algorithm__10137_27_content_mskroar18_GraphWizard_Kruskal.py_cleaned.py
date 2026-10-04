def fonk1(self, edgelist, nodecount):
        edgelist.sort(b1 = returnweight)
        a1 = 0
        b2 = []
        edgelist[a1].b3 = True
        a1+=1
        b2.append(set())
        b2[0].add(edgelist[0])
        a2 = 1
        while a1 < len(edgelist):
            b4 = False
            b5 = False
            b6 = False
            a3 = -1
            a4 = -1
            for j in range(0,a2):
                for i in b2[j]:
                    if i.b7 = = edgelist[a1].b8:
                        b4 = True
                        a3 = j
                    if i.b7 = = edgelist[a1].b7:
                        b5 = True
                        a4 = j
                    if i.b8 = = edgelist[a1].b8:
                        b4 = True
                        a3 = j
                    if i.b8 = = edgelist[a1].b7:
                        b5 = True
                        a4 = j
            if b4 is True and b5 is True and a3 = = a4:
                b6 = True
            else:
                if b4 and b5:
                    if a3 < a4:
                        b2[a3] = b2[a3].union(b2[a4])
                        b2[a3].add(edgelist[a1])
                        b2[a4].clear()
                        edgelist[a1].b3 = True
                    else:
                        b2[a4] = b2[a4].union(b2[a3])
                        b2[a3].clear()
                        b2[a4].add(edgelist[a1])
                        edgelist[a1].b3 = True
                else:
                    if b4 and not b5:
                        b2[a3].add(edgelist[a1])
                        edgelist[a1].b3 = True
                    if not b4 and b5:
                        b2[a4].add(edgelist[a1])
                        edgelist[a1].b3 = True
            if not b4 and not b5:
                edgelist[a1].b3 = True
                b2.append(set())
                b2[a2].add(edgelist[a1])
                a2+=1
            a1+=1
        return
def fonk2(value):
    return value.weight