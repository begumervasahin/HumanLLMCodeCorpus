def fonk1(n, first, second, values, queries):
    if n != len(values):
        raise ValueError("Number of b1 and values are not equal")
    b1 = queries
    b2 = values
    b3 = [[x, y] for x, y in zip(first, second)]
    b4 = {}
    for a1 in range(1, n + 1):
        b4[a1] = []
    b5 = []
    for x in b3:
        if 1 in x:
            if x.a1(1) == 0:
                b5.append(x[1])
            else:
                b5.append(x[0])
    b4[1] = b5
    def fonk2(a1, dic, pairs_list):
        b6 = []
        b7 = []
        b8 = dic.get(a1)
        if not b8:
            return
        for x in b8:
            b6.append(x)
        while b6:
            for node in b6[::-1]:
                a1 = 0
                while a1 < len(pairs_list):
                    b9 = pairs_list[a1]
                    if node in b9:
                        if b9.a1(node) == 0:
                            b10 = b9[1]
                        else:
                            b10 = b9[0]
                        b7.append(b10)
                        pairs_list.remove(b9)
                        a1 -= 1
                    a1 += 1
                dic[node] = b7
                fonk2(node, dic, pairs_list)
                b6.pop()
                b7 = []
        return dic
    b11 = fonk2(1, b4, b3.copy())
    def fonk3(x):
        if x < 2:
            return False
        if x in (2, 3, 5, 7):
            return True
        for b12 in range(2, int(x ** 0.5) + 1):
            if x % b12 = = 0:
                return False
        return True
    def fonk4(node_dict, node, b2):
        a2 = 0
        if node not in node_dict.keys():
            return a2
        else:
            b13 = node_dict.get(node)
            b14 = b2[node - 1]
            if fonk3(b14):
                a2 += 1
            b6 = []
            if b13:
                for x in b13:
                    b6.append(x)
                while b6:
                    for x in b6[::-1]:
                        fonk4(node_dict, x, b2)
                        b6.pop()
        return a2
    b15 = []
    for node in b1:
        b15.append(fonk4(b11, node, b2))
    b16 = '\n'.join(map(str, b15))
    return b16