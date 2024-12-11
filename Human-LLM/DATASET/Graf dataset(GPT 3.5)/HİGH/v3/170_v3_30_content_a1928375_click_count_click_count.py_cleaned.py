def fonk1(b13, keyword, b3):
    b1 = fonk2(b13, keyword)
    if b1:
        for entry in b1:
            if entry[0] == b3:
                entry[1] += 1
def fonk2(b13, keyword):
    for entry in b13:
        if entry[0] == keyword:
            return entry[1]
    return None
def fonk3(b13, keyword, b3):
    for entry in b13:
        if entry[0] == keyword:
            for b2, _ in entry[1]:
                if b2 = = b3:
                    return
            entry[1].append([b3, 0])
            return
    b13.append([keyword, [[b3, 0]]])
def fonk4(b3):
    try:
        if b3 = = "http:
            return '''<html> <body> This is a test b10 for learning to crawl!
<p> It is a good idea to
<a b4 = "http:
learn to crawl</a> before you try to
<a b4 = "http:
<a b4 = "http:
        elif b3 = = "http:
            return '''<html> <body> I have not learned to crawl yet, but I am
quite good at  <a b4 = "http:
</body> </html>'''
        elif b3 = = "http:
            return '''<html> <body> I can't get enough
<a b4 = "http:
        elif b3 = = "http:
            return '<html><body>The magic b15 are Squeamish Ossifrage!</body></html>'
    except:
        return ""
    return ""
def fonk5(a, b):
    for e in b:
        if e not in a:
            a.append(e)
def fonk6(b10):
    b5 = b10.find('<a b4=')
    if b5 = = -1:
        return None, 0
    b6 = b10.find('"', b5)
    b7 = b10.find('"', b6 + 1)
    b3 = b10[b6 + 1:b7]
    return b3, b7
def fonk7(b10):
    b8 = []
    while True:
        b3, b9 = fonk6(b10)
        if b3:
            b8.append(b3)
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
def fonk9(b13, b3, b14):
    b15 = b14.split()
    for word in b15:
        fonk3(b13, word, b3)
b13 = fonk8('http:
print(fonk2(b13, 'good'))
fonk1(b13, 'good', 'http:
print(fonk2(b13, 'good'))
fonk1(b13, 'good', 'http:
print(fonk2(b13, 'good'))