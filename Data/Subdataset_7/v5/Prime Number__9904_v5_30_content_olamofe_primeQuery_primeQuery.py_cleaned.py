def fonk1(n, first, second, values, queries):
    if n != len(values):
        raise ValueError("Number of b1 and values are not equal")
    b1 = queries
    b2 = values
    b3 = list(zip(first, second))
    b4 = {}
    for index in range(1, n + 1):
        b4[index] = []
    b5 = [x[1] if x.index(1) == 0 else x[0] for x in b3 if 1 in x]
    b4[1] = b5
    def fonk2(index, dic, pairs_list):
        if index not in dic:
            return
        b6 = dic[index][:]
        while b6:
            b7 = b6.pop()
            for idx, node_pairs in enumerate(pairs_list[:]):
                if b7 in node_pairs:
                    b8 = node_pairs[1] if node_pairs.index(b7) == 0 else node_pairs[0]
                    dic[b7] = dic.get(b7, []) + [b8]
                    del pairs_list[idx]
                    b6.append(b8)
        return dic
    b9 = fonk2(1, b4, b3.copy())
    def fonk3(x):
        if x < 2:
            return False
        if x in (2, 3, 5, 7):
            return True
        for b10 in range(2, int(x ** 0.5) + 1):
            if x % b10 = = 0:
                return False
        return True
    def fonk4(node_dict, b7, b2):
        if b7 not in node_dict:
            return 0
        b11 = 1 if fonk3(b2[b7 - 1]) else 0
        for child_node in node_dict[b7]:
            b11 += fonk4(node_dict, child_node, b2)
        return b11
    b12 = [fonk4(b9, b7, b2) for b7 in b1]
    b13 = '\n'.join(map(str, b12))
    return b13