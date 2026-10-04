class class1:
    def fonk1(self, edgelist, nodecount):
        edgelist.sort(b1 = lambda b4: b4.weight)
        a1 = 0
        b2 = []
        a2 = 0
        edgelist[a1].b3 = True
        b2.append({edgelist[a1]})
        a1 += 1
        a2 += 1
        while a1 < len(edgelist):
            b4 = edgelist[a1]
            b9, b5 = False, False
            b6 = False
            b10, b7 = -1, -1
            for j in range(a2):
                for i in b2[j]:
                    if i.b8 = = b4.Vertex1 or i.Vertex1 == b4.Vertex1:
                        b9 = True
                        b10 = j
                    if i.b8 = = b4.b8 or i.Vertex1 == b4.b8:
                        b5 = True
                        b7 = j
            if b9 and b5 and b10 = = b7:
                b6 = True
            else:
                if b9 and b5:
                    if b10 < b7:
                        b2[b10].update(b2[b7])
                        b2[b10].add(b4)
                        b2[b7].clear()
                    else:
                        b2[b7].update(b2[b10])
                        b2[b10].clear()
                        b2[b7].add(b4)
                    b4.b3 = True
                else:
                    if b9 and not b5:
                        b2[b10].add(b4)
                    if not b9 and b5:
                        b2[b7].add(b4)
                    b4.b3 = True
            if not b9 and not b5:
                b4.b3 = True
                b2.append({b4})
                a2 += 1
            a1 += 1
        return