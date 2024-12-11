import os
import re
import string
import glob
def fonk1(root):
    return [os.path.join(dp, b1) for dp, dn, filenames in os.walk(root) for b1 in filenames]
def fonk2(fileName):
    b1 = open(fileName)
    b2 = b1.read()
    b1.close()
    return b2
def fonk3(text):
    b3 = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\b8\\n]')
    b4 = b3.sub(" ", text)
    b5 = b4.split(" ")
    b5 = [w for w in b5 if len(w) > 2]
    b5 = [w.lower() for w in b5]
    return b5
def fonk4(text):
    b6 = []
    if len(text) < 3:
        return b6
    b7 = re.escape(string.punctuation)
    b8 = iter(b7)
    b7 = '|'.join(a+b for a,b in zip(b8, b8))
    b7 += '|[0-9]|\r|\b8|\n|]'
    b9 = re.compile(b7)
    b10 = re.sub(b9, ' ', text)
    b6 = b10.split(' ')
    b11 = len(b6)
    a1 = 0
    while a1 < b11:
        b6[a1] = b6[a1].lower()
        if len(b6[a1]) < 3:
            b6.pop(a1)
            b11 -= 1
        else:
            a1 += 1
    return b6
def fonk5(file, b14):
    b12 = set()
    with open (file, 'r') as myfile:
        for line in myfile:
            b13 = fonk3(line)
            for a1 in range(len(b14)):
                if b14[a1] in b13:
                    b12.add(line)
                    if len(b12) == 2: return b12
    return b12
def fonk6(b16, b14):
    if b14 = = None:
        b15 = ' !!!nothing to be found!!! '
    else:
        b15 = ' '.join(b14)
    if b16 = = None or len(b16) == 0:
        a2 = 0
    else:
        a2 = len(b16)
    b17 = '<html>\n<body>\n'
    b18 = '<h2>Search results for <b>' + b15 + '</b> in ' + str(a2) + ' files</h2>'
    b17 += b18
    b17 += '\n\n'
    if a2:
        a3 = 0
        for file in b16:
            b19 = 'file:
            b20 = '<p><a href="' + b19 + '">' + file + '</a><br>'
            b21 = fonk5(file, b14)
            b22 = ''
            for line in b21:
                b22 += line + '<br>'
            b20 += b22
            b20 += '<br>'
            b20 += '\n\n'
            b17 += b20
            a3 += 1
            if a3 >= 100: break
    b17 += '</body>\n</html>\n'
    return b17
def fonk7(b16):
    if b16 is None:
        return []
    return [os.path.basename(d) for d in b16]
if b23 = = '__main__':
    b24 = 'aaaa!bbbb"cccc
             ',mmmm-nnnn.oooo/pppp:qqqq;rrrr<b25 = tttt>uuuu?vvvv@wwww' \
             '[xxxx\yyyy]zzzz^AAAA_BBBB`CCCC{DDDD|EEEE}FF~GHH[]IJK{}LMNOPQRSTUVWXYZ'
    print fonk3(b24)
    print fonk4(b24)
    b26 = print fonk3(b26)
    print fonk4(b26)