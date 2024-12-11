def fonk1(b11, keyword, b5):
    b1 = fonk2(b11, keyword)
    if b1:
        for entry in b1:
            if entry[0] == b5:
                entry[1] += 1
def fonk2(b11, keyword):
    for entry in b11:
        if entry[0] == keyword:
            return entry[1]
    return None
def fonk3(b11, keyword, b5):
    for entry in b11:
        if entry[0] == keyword:
            for url_entry in entry[1]:
                if url_entry[0] == b5:
                    return
            entry[1].append([b5, 0])
            return
    b11.append([keyword, [[b5, 0]]])
def fonk4(b5):
    return ''
def fonk5(a, b):
    for e in b:
        if e not in a:
            a.append(e)
def fonk6(b8):
    b2 = b8.find('<a href=')
    if b2 = = -1:
        return None, 0
    b3 = b8.find('"', b2)
    b4 = b8.find('"', b3 + 1)
    b5 = b8[b3 + 1:b4]
    return b5, b4
def fonk7(b8):
    b6 = []
    while True:
        b5, b7 = fonk6(b8)
        if b5:
            b6.append(b5)
            b8 = b8[b7:]
        else:
            break
    return b6
def fonk8(seed):
    b9 = [seed]
    b10 = []
    b11 = []
    while b9:
        b8 = b9.pop()
        if b8 not in b10:
            b12 = fonk4(b8)
            fonk9(b11, b8, b12)
            fonk5(b9, fonk7(b12))
            b10.append(b8)
    return b11
def fonk9(b11, b5, b12):
    b13 = b12.split()
    for word in b13:
        fonk3(b11, word, b5)
b11 = fonk8('http:
print(fonk2(b11, 'good'))
fonk1(b11, 'good', 'http:
print(fonk2(b11, 'good'))
fonk1(b11, 'good', 'http:
print(fonk2(b11, 'good'))