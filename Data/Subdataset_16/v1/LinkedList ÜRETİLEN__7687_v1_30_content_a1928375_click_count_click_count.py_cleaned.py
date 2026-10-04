def fonk1(b12, keyword, b2):
    b1 = fonk2(b12, keyword)
    if b1:
        for entry in b1:
            if entry[0] == b2:
                entry[1] = entry[1] + 1
def fonk2(b12, keyword):
    for entry in b12:
        if entry[0] == keyword:
            return entry[1]
    return None
def fonk3(b12, keyword, b2):
    for entry in b12:
        if entry[0] == keyword:
            for b1 in entry[1]:
                if b1[0] == b2:
                    return
            entry[1].append([b2, 0])
            return
    b12.append([keyword, [[b2, 0]]])
def fonk4(b2):
    try:
        if b2 = = "http:
            return '''<html> <body> This is a test b9 for learning to crawl!
<p> It is a good idea to
<a b3 = "http:
learn to crawl</a> before you try to
<a b3 = "http:
<a b3 = "http:
        elif b2 = = "http:
            return '''<html> <body> I have not learned to crawl yet, but I am
quite good at  <a b3 = "http:
</body> </html>'''
        elif b2 = = "http:
            return '''<html> <body> I can't get enough
<a b3 = "http:
        elif b2 = = "http:
            return '<html><body>The magic b14 are Squeamish Ossifrage!</body></html>'
    except:
        return ""
    return ""
def fonk5(a, b):
    for e in b:
        if e not in a:
            a.append(e)
def fonk6(b9):
    b4 = b9.find('<a b3=')
    if b4 = = -1:
        return None, 0
    b5 = b9.find('"', b4)
    b6 = b9.find('"', b5 + 1)
    b2 = b9[b5 + 1:b6]
    return b2, b6
def fonk7(b9):
    b7 = []
    while True:
        b2, b8 = fonk6(b9)
        if b2:
            b7.append(b2)
            b9 = b9[b8:]
        else:
            break
    return b7
def fonk8(seed):
    b10 = [seed]
    b11 = []
    b12 = []
    while b10:
        b9 = b10.pop()
        if b9 not in b11:
            b13 = fonk4(b9)
            fonk9(b12, b9, b13)
            fonk5(b10, fonk7(b13))
            b11.append(b9)
    return b12
def fonk9(b12, b2, b13):
    b14 = b13.split()
    for word in b14:
        fonk3(b12, word, b2)
b12 = fonk8('http:
print(fonk2(b12, 'good'))
fonk1(b12, 'good', 'http:
print(fonk2(b12, 'good'))
fonk1(b12, 'good', 'http:
print(fonk2(b12, 'good'))