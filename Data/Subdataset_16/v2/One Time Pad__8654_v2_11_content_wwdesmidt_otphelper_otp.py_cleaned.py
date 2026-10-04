
b1 = "0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
b2 = list(b1)
def fonk1(s):
    return [c.upper() for c in s if c.upper() in b1]
def fonk2(m, k):
    b3 = b1.index(m)
    b4 = b1.index(k)
    b5 = (b3 + b4) % len(b1)
    return b2[b5]
def fonk3(b10, b11):
    b6 = fonk1(b10)
    b7 = fonk1(b11)
    b8 = [fonk2(b6[i], b7[i % len(b7)]) for i in range(len(b6))]
    return "".join(b8)
def fonk4(m, k):
    b3 = b1.index(m)
    b4 = b1.index(k)
    b5 = (b3 - b4) % len(b1)
    return b2[b5]
def fonk5(b10, b11):
    b6 = fonk1(b10)
    b7 = fonk1(b11)
    b8 = [fonk4(b6[i], b7[i % len(b7)]) for i in range(len(b6))]
    return "".join(b8)
if b9 = = "__main__":
    b10 = "This is the Message!!!!! What time should we meeT? 12:30?"
    b11 = ("One thing that you will get to know about programming, is that programmers "
           "like to be lazy. If something has been done before, why should you do it again?")
    b12 = fonk3(b10, b11)
    b13 = fonk5(b12, b11)
    print(f"Original Message: {b10}")
    print(f"Encrypted Message: {b12}")
    print(f"Decrypted Message: {b13}")