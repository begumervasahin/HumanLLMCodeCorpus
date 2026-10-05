import os
import re
import string
def fonk1(root):
    b1 = []
    for root_path, _, filenames in os.walk(root):
        for filename in filenames:
            b1.append(os.path.join(root_path, filename))
    return b1
def fonk2(file_path):
    with open(file_path, 'r') as file:
        return file.read()
def fonk3(text):
    b2 = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\b6\\n]')
    b3 = b2.sub(" ", text)
    b4 = b3.split(" ")
    b4 = [word.lower() for word in b4 if len(word) > 2]
    return b4
def fonk4(text):
    b4 = []
    if len(text) < 3:
        return b4
    b5 = re.escape(string.punctuation)
    b6 = iter(b5)
    b5 = '|'.join(a + b for a, b in zip(b6, b6))
    b5 += '|[0-9]|\r|\b6|\n|]'
    b7 = re.compile(b5)
    b8 = re.sub(b7, ' ', text)
    b4 = b8.split(' ')
    a1 = 0
    while a1 < len(b4):
        b4[a1] = b4[a1].lower()
        if len(b4[a1]) < 3:
            b4.pop(a1)
        else:
            a1 += 1
    return b4
def fonk5(file_path, terms):
    b9 = set()
    with open(file_path, 'r') as file:
        for line in file:
            b10 = fonk3(line)
            for term in terms:
                if term in b10:
                    b9.add(line)
                    if len(b9) == 2:
                        return b9
    return b9
def fonk6(file_paths, terms):
    if terms is None:
        b11 = ' !!!nothing to be found!!! '
    else:
        b11 = ' '.join(terms)
    if not file_paths:
        a2 = 0
    else:
        a2 = len(file_paths)
    b12 = '<html>\n<body>\n'
    b13 = f'<h2>Search results for <b>{b11}</b> in {a2} b1</h2>'
    b12 += b13
    b12 += '\n\n'
    if file_paths:
        a3 = 0
        for file_path in file_paths:
            b14 = 'file:
            b15 = f'<p><a href="{b14}">{file_path}</a><br>'
            b9 = fonk5(file_path, terms)
            b16 = ''
            for line in b9:
                b16 += line + '<br>'
            b15 += b16
            b15 += '<br>\n\n'
            b12 += b15
            a3 += 1
            if a3 >= 100:
                break
    b12 += '</body>\n</html>\n'
    return b12
def fonk7(file_paths):
    return [os.path.basename(path) for path in file_paths]
if b17 = = '__main__':
    b18 = 'aaaa!bbbb"cccc             ",mmmm-nnnn.oooo/pppp:qqqq;rrrr<ssss=tttt>uuuu?vvvv@wwww' \
                 '[xxxx\yyyy]zzzz^AAAA_BBBB`CCCC{DDDD|EEEE}FF~GHH[]IJK{}LMNOPQRSTUVWXYZ'
    print(fonk3(b18))
    print(fonk4(b18))
    b19 = print(fonk3(b19))
    print(fonk4(b19))