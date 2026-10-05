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
    b2 = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\b7\\n]')
    b3 = b2.sub(" ", text)
    b4 = b3.split(" ")
    b4 = [word.lower() for word in b4 if len(word) > 2]
    return b4
def fonk4(text):
    b5 = []
    if len(text) < 3:
        return b5
    b6 = re.escape(string.punctuation)
    b7 = iter(b6)
    b6 = '|'.join(a + b for a, b in zip(b7, b7))
    b6 += '|[0-9]|\r|\b7|\n|]'
    b8 = re.compile(b6)
    b9 = re.sub(b8, ' ', text)
    b5 = b9.split(' ')
    a1 = 0
    while a1 < len(b5):
        b5[a1] = b5[a1].lower()
        if len(b5[a1]) < 3:
            b5.pop(a1)
        else:
            a1 += 1
    return b5
def fonk5(file_path, terms):
    b10 = set()
    with open(file_path, 'r') as file:
        for line in file:
            b11 = fonk3(line)
            for term in terms:
                if term in b11:
                    b10.add(line)
                    if len(b10) == 2:
                        return b10
    return b10
def fonk6(file_paths, terms):
    if terms is None:
        b12 = ' !!!nothing to be found!!! '
    else:
        b12 = ' '.join(terms)
    if file_paths is None or len(file_paths) == 0:
        a2 = 0
    else:
        a2 = len(file_paths)
    b13 = '<html>\n<body>\n'
    b14 = f'<h2>Search results for <b>{b12}</b> in {a2} files</h2>'
    b13 += b14
    b13 += '\n\n'
    if a2:
        a3 = 0
        for file_path in file_paths:
            b15 = 'file:
            b16 = f'<p><a href="{b15}">{file_path}</a><br>'
            b10 = fonk5(file_path, terms)
            b17 = ''
            for line in b10:
                b17 += line + '<br>'
            b16 += b17
            b16 += '<br>'
            b16 += '\n\n'
            b13 += b16
            a3 += 1
            if a3 >= 100:
                break
    b13 += '</body>\n</html>\n'
    return b13
def fonk7(file_paths):
    if file_paths is None:
        return []
    return [os.path.basename(path) for path in file_paths]
if b18 = = '__main__':
    b19 = 'aaaa!bbbb"cccc             ",mmmm-nnnn.oooo/pppp:qqqq;rrrr<ssss=tttt>uuuu?vvvv@wwww' \
                 '[xxxx\yyyy]zzzz^AAAA_BBBB`CCCC{DDDD|EEEE}FF~GHH[]IJK{}LMNOPQRSTUVWXYZ'
    print(fonk3(b19))
    print(fonk4(b19))
    b20 = print(fonk3(b20))
    print(fonk4(b20))