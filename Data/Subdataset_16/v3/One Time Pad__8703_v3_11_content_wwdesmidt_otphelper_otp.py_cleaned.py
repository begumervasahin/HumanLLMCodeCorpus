b1 = "0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
b2 = list(b1)
def fonk1(s):
    return [c.upper() for c in s if c.upper() in b1]
def fonk2(m, k):
    b3 = b1.index(m)
    b4 = b1.index(k)
    b5 = (b3 + b4) % len(b1)
    return b2[b5]
def fonk3(c, k):
    b5 = b1.index(c)
    b4 = b1.index(k)
    b3 = (b5 - b4) % len(b1)
    return b2[b3]
def fonk4(b12, b13):
    b6 = fonk1(b12)
    b7 = fonk1(b13)
    b8 = [fonk2(b6[i], b7[i % len(b7)]) for i in range(len(b6))]
    return "".join(b8)
def fonk5(b14, b13):
    b9 = fonk1(b14)
    b7 = fonk1(b13)
    b10 = [fonk3(b9[i], b7[i % len(b7)]) for i in range(len(b9))]
    return "".join(b10)
if b11 = = "__main__":
    b12 = "This is the Message!!!!! What time should we meeT? 12:30?"
    b13 = ("One thing that you will get to know about programming, is that programmers "
           "like to be lazy. If something has been done before, why should you do it again?")
    b14 = fonk4(b12, b13)
    b15 = fonk5(b14, b13)
    print(f"Original Message: {b12}")
    print(f"Encrypted Message: {b14}")
    print(f"Decrypted Message: {b15}")