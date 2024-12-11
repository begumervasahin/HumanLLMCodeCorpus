def fonk1(source, example):
    a1 = 0
    for char in source:
        if char in example:
            a1 += 1
    return a1
a2 = 0
b1 = "aeiuo"
b2 = "qrtpsdfghjklzxcvbnmy"
while True:
    try:
        b4, b3 = input("Input two names divided by comma (e.g. 'Jan, Joanna'): ").split(",")
        b4 = b4.lower().strip()
        b3 = b3.lower().strip()
        break
    except ValueError:
        print("Wrong input")
if b4[0] == b3[0]:
    a2 += 20
if (b4[0] in b1) and (b3[0] in b1):
    a2 += 10
if (b4[0] in b2) and (b3[0] in b2):
    a2 += 5
if fonk1(b4, b1) == fonk1(b3, b1):
    a2 += 12
if fonk1(b4, b2) == fonk1(b3, b2):
    a2 += 12
if ('l' in b4 and 'l' in b3) or ('o' in b4 and 'o' in b3) \
        or ('v' in b4 and 'v' in b3) or ('e' in b4 and 'e' in b3):
    a2 += 7
print("Your love points are %d" % a2)
print("REMEMBER: your relationship depends only on you and your partner, not from the stupid love calculator!")