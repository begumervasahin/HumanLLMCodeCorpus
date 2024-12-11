import os
import re
import string
def fonk1(root):
    b1 = [os.path.join(dp, f) for dp, dn, filenames in os.walk(root) for f in filenames]
    return b1
def fonk2(fileName):
    with open(fileName, 'r') as file:
        b2 = file.read()
    return b2
def fonk3(b2):
    b3 = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\b6\\n]')
    b2 = b3.sub(" ", b2)
    b4 = [word.lower() for word in b2.split() if len(word) > 2]
    return b4
def fonk4(b2):
    b4 = []
    if len(b2) < 3:
        return b4
    b5 = re.escape(string.punctuation)
    b6 = iter(b5)
    b5 = '|'.join(a+b for a, b in zip(b6, b6))
    b5 += '|[0-9]|\r|\b6|\n|]'
    b7 = re.compile(b5)
    b8 = re.sub(b7, ' ', b2)
    b4 = [word.lower() for word in b8.split() if len(word) > 2]
    return b4
def fonk5(file, terms):
    b9 = set()
    with open(file, 'r') as myfile:
        for line in myfile:
            b10 = fonk3(line)
            for term in terms:
                if term in b10:
                    b9.add(line)
                    if len(b9) == 2:
                        return b9
    return b9
def fonk6(docs, terms):
    if terms is None:
        b11 = ' !!!nothing to be found!!! '
    else:
        b11 = ' '.join(terms)
    if docs is None or len(docs) == 0:
        a1 = 0
    else:
        a1 = len(docs)
    b12 = '<html>\n<body>\n'
    b13 = f'<h2>Search results for <b>{b11}</b> in {a1} files</h2>'
    b12 += b13 + '\n\n'
    if a1:
        a2 = 0
        for file in docs:
            b14 = 'file:
            b15 = f'<p><a href="{b14}">{file}</a><br>'
            b16 = fonk5(file, terms)
            b17 = '<br>'.join(b16)
            b15 += b17 + '<br>\n\n'
            b12 += b15
            a2 += 1
            if a2 >= 100:
                break
    b12 += '</body>\n</html>\n'
    return b12
def fonk7(docs):
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]
if b18 = = '__main__':
    b19 = 'aaaa!bbbb"cccc,mmmm-nnnn.oooo/pppp:qqqq;rrrr<ssss=tttt>uuuu?vvvv@wwww[xxxx\\yyyy]zzzz^AAAA_BBBB`CCCC{DDDD|EEEE}FF~GHH[]IJK{}LMNOPQRSTUVWXYZ'
    print(fonk3(b19))
    print(fonk4(b19))
    b20 = print(fonk3(b20))
    print(fonk4(b20))