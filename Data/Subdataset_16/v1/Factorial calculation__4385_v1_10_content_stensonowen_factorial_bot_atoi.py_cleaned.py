import re
from text2num import text2num, Small, Magnitude
b1 = {
    'a': 'one',
    'dozen': 'twelve',
    'and': '',
}
b2 = set(["hundred"])
for d in [Small, Magnitude, b1]:
    b2 = b2.union(set(d.keys()))
def fonk1(b3):
    b3 = re.sub("[\W_]", ' ', b3)
    b4 = []
    for token in b3.split():
        b5 = b1.get(token)
        if b5 is not None and b5 != '':
            b4.append(b5)
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
    return text2num(b4[b6:])
def fonk3(b3):
    b4 = fonk1(b3)
    b7 = text2num(b4)
    return b7
b3 = "I have a dozen apples and twenty-five oranges"
print(f"Extracted number: {fonk2(b3)}")
print(f"Converted number: {fonk3(b3)}")