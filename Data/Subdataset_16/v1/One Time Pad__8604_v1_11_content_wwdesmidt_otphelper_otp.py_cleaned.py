b1 = "0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
b2 = list(b1)
def fonk1(s):
    b3 = [c.upper() for c in s if c.upper() in b1]
    return b3
def fonk2(m, k):
    b4 = b1.index(m)
    b5 = b1.index(k)
    b6 = (b4 + b5) % len(b1)
    return b2[b6]
def fonk3(b10, b11):
    b7 = fonk1(b10)
    b8 = fonk1(b11)
    b9 = [fonk2(b7[i], b8[i]) for i in range(len(b7))]
    return "".join(b9)
def fonk4(m, k):
    b4 = b1.index(m)
    b5 = b1.index(k)
    b6 = (b4 - b5) % len(b1)
    return b2[b6]
def fonk5(b10, b11):
    b7 = fonk1(b10)
    b8 = fonk1(b11)
    b9 = [fonk4(b7[i], b8[i]) for i in range(len(b7))]
    return "".join(b9)
b10 = "This is the Message!!!!! What time should we meeT? 12:30?"
b11 = "One thing that you will get to know about programming, is that programmers like to be lazy. If something has been done before, why should you do it again?"
b12 = fonk3(b10, b11)
b13 = fonk5(b12, b11)
print(f"Original Message: {b10}")
print(f"Encrypted Message: {b12}")
print(f"Decrypted Message: {b13}")