def fonk1(b13, keyword, b7):
    b1 = fonk2(b13, keyword)
    if b1:
        for entry in b1:
            if entry[0] == b7:
                entry[1] += 1
def fonk2(b13, keyword):
    for entry in b13:
        if entry[0] == keyword:
            return entry[1]
    return None
def fonk3(b13, keyword, b7):
    for entry in b13:
        if entry[0] == keyword:
            for b1 in entry[1]:
                if b1[0] == b7:
                    return
            entry[1].append([b7, 0])
            return
    b13.append([keyword, [[b7, 0]]])
def fonk4(b7):
    try:
        b2 = {
            "http:
<p> It is a good idea to
<a b3 = "http:
learn to crawl</a> before you try to
<a b3 = "http:
<a b3 = "http:
            "http:
quite good at  <a b3 = "http:
</body> </html>''',
            "http:
<a b3 = "http:
            "http:
        }
        return b2.get(b7, "")
    except:
        return ""
def fonk5(a, b):
    for e in b:
        if e not in a:
            a.append(e)
def fonk6(b10):
    b4 = b10.find('<a b3=')
    if b4 = = -1:
        return None, 0
    b5 = b10.find('"', b4)
    b6 = b10.find('"', b5 + 1)
    b7 = b10[b5 + 1:b6]
    return b7, b6
def fonk7(b10):
    b8 = []
    while True:
        b7, b9 = fonk6(b10)
        if b7:
            b8.append(b7)
            b10 = b10[b9:]
        else:
            break
    return b8
def fonk8(seed):
    b11 = [seed]
    b12 = []
    b13 = []
    while b11:
        b10 = b11.pop()
        if b10 not in b12:
            b14 = fonk4(b10)
            fonk9(b13, b10, b14)
            fonk5(b11, fonk7(b14))
            b12.append(b10)
    return b13
def fonk9(b13, b7, b14):
    b15 = b14.split()
    for word in b15:
        fonk3(b13, word, b7)
if b16 = = "__main__":
    b13 = fonk8('http:
    print(fonk2(b13, 'good'))
    fonk1(b13, 'good', 'http:
    print(fonk2(b13, 'good'))
    fonk1(b13, 'good', 'http:
    print(fonk2(b13, 'good'))