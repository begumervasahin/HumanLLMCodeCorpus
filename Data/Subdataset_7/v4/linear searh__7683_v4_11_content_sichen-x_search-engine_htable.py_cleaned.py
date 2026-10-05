
def fonk1(nbuckets):
    b1 = []
    for i in range(nbuckets):
        b1.append([])
    return b1
def fonk2(o):
    if isinstance(o, int):
        return o
    elif isinstance(o, str):
        a1 = 0
        for char in o:
            a1 = a1 * 31 + ord(char)
        return a1
    else:
        return None
def fonk3(table, key, value):
    if table is None or len(table) == 0:
        return
    b2 = fonk2(key) % len(table)
    b3 = table[b2]
    for i in range(len(b3)):
        if b3[i][0] == key:
            b4 = b3[i][1] | value
            b3[i] = (key, b4)
            return
    b3.append((key, value))
def fonk4(table, key):
    if table is None or len(table) == 0:
        return None
    b2 = fonk2(key) % len(table)
    b3 = table[b2]
    for node in b3:
        if node[0] == key:
            return node[1]
    return None
def fonk5(table):
    if table is None:
        return None
    b5 = ""
    for i in range(len(table)):
        b5 += str(i).zfill(4) + '->'
        for node in table[i]:
            b5 += str(node[0]) + ':' + str(node[1]) + ', '
        b5 = b5.rstrip(', ') + '\n'
    return b5
def fonk6(table):
    if table is None:
        return None
    b5 = '{'
    for i in range(len(table)):
        for node in table[i]:
            b5 += str(node[0]) + ':' + str(node[1]) + ', '
    b5 = b5.rstrip(', ') + '}'
    return b5