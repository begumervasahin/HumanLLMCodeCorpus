def primeQuery(n, first, second, values, queries):
    if n != len(values):
        raise ValueError("Number of nodes and values are not equal")
    node = queries
    value = values
    pairs = []
    for x, y in zip(first, second):
        pair = [x, y]
        pairs.append(pair)
    dic = {}
    for index in range(1, n + 1):
        dic[index] = []
    tmp = []
    savedpairs = []
    for x in pairs:
        savedpairs.append(x)
    while savedpairs != []:
        pairtmp = savedpairs
        for x in pairtmp:
            if 1 in x:
                if x.index(1) == 0:
                    rootchild = x[1]
                    pairtmp.remove(x)
                    pairs.remove(x)
                else:
                    rootchild = x[0]
                    pairtmp.remove(x)
                    pairs.remove(x)
                tmp.append(rootchild)
            else:
                pairtmp.remove(x)
        savedpairs = pairtmp
    dic[1] = tmp
    def createdic(index, dic, listy):
        stack = []
        tmp = []
        currentlist = dic.get(index)
        if currentlist == []:
            return
        for x in currentlist:
            stack.append(x)
        while stack != []:
            for node in stack[::-1]:
                index = 0
                while index < len(listy):
                    nodepairs = listy[index]
                    if node in nodepairs:
                        if nodepairs.index(node) == 0:
                            nodecomp = nodepairs[1]
                        else:
                            nodecomp = nodepairs[0]
                        tmp.append(nodecomp)
                        listy.remove(nodepairs)
                        index -= 1
                    index += 1
                dic[node] = tmp
                createdic(node, dic, listy)
                stack.pop()
                tmp = []
        return dic
    treex = createdic(1, dic, pairs)
    tmpdic = treex.copy()
    def countNode(dic, node, value):
        nonlocal countex
        nonlocal primecounter
        if node not in dic.keys():
            return primecounter
        else:
            valueAtNode = dic.get(node)
            valueinsidenode = value[node - 1]
            if prime(valueinsidenode):
                primecounter += 1
            stack = []
            if valueAtNode == []:
                return primecounter
            for x in valueAtNode:
                stack.append(x)
            while stack != []:
                for x in stack[::-1]:
                    countex += 1
                    countNode(dic, x, value)
                    stack.pop()
        return primecounter
    def prime(x):
        primelist = [2, 3, 5, 7]
        if x == 1 or x == 0:
            return False
        if x in primelist:
            return True
        for ele in primelist:
            if x % ele == 0:
                return False
        return True
    tmp = []
    for node in queries:
        countex = 0
        primecounter = 0
        if node in dic.keys():
            prime = countNode(tmpdic, node, value)
            tmp.append(prime)
    total = "\n".join(map(str, tmp))
    print(total)
    return total
n = 5
first = [1, 2, 2, 3, 3]
second = [2, 3, 4, 5, 6]
values = [10, 10, 10, 10, 10]
queries = [1, 2, 3, 4, 5]
primeQuery(n, first, second, values, queries)