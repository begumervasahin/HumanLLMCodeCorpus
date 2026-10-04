import re
import text2num
b1 = {
    'a': 'one',
    'dozen': 'twelve',
    'and': '',
}
b2 = set(["hundred"])
for d in [text2num.Small, text2num.Magnitude, b1]:
    b2 = b2.union(set(d.keys()))
def fonk1(b3):
    b3 = re.sub("[\W_]", ' ', b3)
    '''b4 = [b1[t]
            if t in b1 and b1[t] not None else t
            for t in b3.split()]'''
    b4 = []
    for token in b3.split():
        b5 = b1.get(token)
        if b5 is not None and b5 is not '':
            b4.append(b1[token])
        elif b5 is None:
            b4.append(token)
    return b4
def fonk2(b3):
    b4 = fonk1(b3)
    b6 = len(b4)
    for i in range(len(b4))[::-1]:
        if b4[i] in b2:
            b6 = i
        else:
            break
    return text2num.text2num(b4[b6:])
def fonk3(b3):
    b4 = fonk1(b3)
    b7 = text2num.text2num(b4)
    return b7