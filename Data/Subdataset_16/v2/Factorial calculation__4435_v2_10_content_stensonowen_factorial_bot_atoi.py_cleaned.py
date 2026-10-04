import re
from text2num import text2num, Small, Magnitude
b1 = {
    'a': 'one',
    'dozen': 'twelve',
    'and': '',
}
b2 = set(["hundred"])
for dictionary in [Small, Magnitude, b1]:
    b2.update(dictionary.keys())
def fonk1(b3):
    b3 = re.sub(r"[\W_]", ' ', b3)
    b4 = []
    for token in b3.split():
        b5 = b1.get(token)
        if b5 is not None and b5 != '':
            b4.append(b5)
        else:
            b4.append(token)
    return b4
def fonk2(b3):
    b4 = fonk1(b3)
    b6 = len(b4)
    for i in reversed(range(len(b4))):
        if b4[i] in b2:
            b6 = i
        else:
            break
    return text2num(b4[b6:])
def fonk3(b3):
    b4 = fonk1(b3)
    return text2num(b4)
if b7 = = "__main__":
    b8 = "I have a dozen apples and twenty-five oranges"
    print(f"Extracted number: {fonk2(b8)}")
    print(f"Converted number: {fonk3(b8)}")