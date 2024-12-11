import re
import text2num
b1 = {
    'a': 'one',
    'dozen': 'twelve',
    'and': '',
}
b2 = set(["hundred"])
for dictionary in [text2num.Small, text2num.Magnitude, b1]:
    b2 |= set(dictionary.keys())
def fonk1(b7):
    b3 = re.findall(r"[\w']+|[.,!?;]", b7)
    for i, token in enumerate(b3):
        b4 = b1.get(token)
        if b4:
            b3[i] = b4
    return b3
def fonk2(b7):
    b3 = fonk1(b7)
    b5 = len(b3)
    for i, token in enumerate(reversed(b3)):
        if token in b2:
            b5 = len(b3) - i - 1
        else:
            break
    return text2num.text2num(b3[b5:])
def fonk3(b7):
    b3 = fonk1(b7)
    b6 = text2num.text2num(b3)
    return b6
b7 = "a dozen apples and two hundred oranges"
b8 = fonk2(b7)
b9 = fonk3(b7)
print("Extracted number:", b8)
print("Converted to integer:", b9)