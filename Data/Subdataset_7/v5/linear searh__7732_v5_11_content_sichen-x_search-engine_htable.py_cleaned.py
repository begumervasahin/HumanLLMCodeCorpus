
def fonk1(nbuckets):
    return [[] for _ in range(nbuckets)]
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
    b1 = fonk2(key) % len(table)
    b2 = table[b1]
    for i, (b3, existing_value) in enumerate(b2):
        if b3 = = key:
            b2[i] = (key, existing_value | value)
            return
    b2.append((key, value))
def fonk4(table, key):
    if table is None or len(table) == 0:
        return None
    b1 = fonk2(key) % len(table)
    b2 = table[b1]
    for b4, entry_value in b2:
        if b4 = = key:
            return entry_value
    return None
def fonk5(table):
    if table is None:
        return None
    b5 = ""
    for i, b2 in enumerate(table):
        b5 += str(i).zfill(4) + '->'
        for b4, entry_value in b2:
            b5 += str(b4) + ':' + str(entry_value) + ', '
        b5 = b5.rstrip(', ') + '\n'
    return b5
def fonk6(table):
    if table is None:
        return None
    b5 = '{'
    for b2 in table:
        for b4, entry_value in b2:
            b5 += str(b4) + ':' + str(entry_value) + ', '
    b5 = b5.rstrip(', ') + '}'
    return b5