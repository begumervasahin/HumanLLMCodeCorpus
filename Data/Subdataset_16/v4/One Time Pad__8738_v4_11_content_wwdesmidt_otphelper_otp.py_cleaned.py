b1 = "0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
b2 = list(b1)
b3 = "This is the Message!!!!! What time should we meeT? 12:30?"
b4 = ("One thing that you will get to know about programming, is that programmers like to be lazy. "
       "If something has been done before, why should you do it again?")
def fonk1(s):
    return [c.upper() for c in s if c.upper() in b1]
def fonk2(m, k):
    b5 = b1.index(m)
    b6 = b1.index(k)
    b7 = (b5 + b6) % len(b1)
    return b2[b7]
def fonk3(b3, b4):
    b8 = fonk1(b3)
    b9 = fonk1(b4)
    b10 = [fonk2(b8[i], b9[i]) for i in range(len(b8))]
    return "".join(b10)
def fonk4(m, k):
    b5 = b1.index(m)
    b6 = b1.index(k)
    b7 = (b5 - b6) % len(b1)
    return b2[b7]
def fonk5(b3, b4):
    b8 = fonk1(b3)
    b9 = fonk1(b4)
    b10 = [fonk4(b8[i], b9[i]) for i in range(len(b8))]
    return "".join(b10)
b11 = fonk3(b3, b4)
b12 = fonk5(b11, b4)
print(f"Original Message: {b3}")
print(f"Encrypted Message: {b11}")
print(f"Decrypted Message: {b12}")