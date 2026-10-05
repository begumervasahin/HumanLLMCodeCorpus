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
def fonk1(b7):
    b3 = re.findall(r"[\w']+|[.,!?;]", b7)
    for i, token in enumerate(b3):
        b4 = b1.get(token)
        if b4:
            b3[i] = b4
        elif b4 is None:
            b3[i] = token
    return b3
def fonk2(b7):
    b3 = fonk1(b7)
    b5 = len(b3)
    for i in range(len(b3))[::-1]:
        if b3[i] in b2:
            b5 = i
        else:
            break
    return text2num.text2num(b3[b5:])
def fonk3(b7):
    b3 = fonk1(b7)
    b6 = text2num.text2num(b3)
    return b6
b7 = "a dozen apples and two hundred oranges"
print("Extracted number:", fonk2(b7))
print("Converted to integer:", fonk3(b7))