b1 = "0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZ?"
b2 = list(b1)
b3 = "This is the Message!!!!! What time should we meeT? 12:30?"
b4 = ("One thing that you will get to know about programming, is that programmers like to be lazy. "
       "If something has been done before, why should you do it again?")
def fonk1(s):
    return [c.upper() for c in s if c.upper() in b1]
def fonk2(message_char, key_char):
    b5 = b1.index(message_char)
    b6 = b1.index(key_char)
    b7 = (b5 + b6) % len(b1)
    return b2[b7]
def fonk3(b3, b4):
    b8 = fonk1(b3)
    b9 = fonk1(b4)
    b10 = [fonk2(b8[i], b9[i]) for i in range(len(b8))]
    return "".join(b10)
def fonk4(encrypted_char, key_char):
    b7 = b1.index(encrypted_char)
    b6 = b1.index(key_char)
    b11 = (b7 - b6) % len(b1)
    return b2[b11]
def fonk5(b13, b4):
    b10 = fonk1(b13)
    b9 = fonk1(b4)
    b12 = [fonk4(b10[i], b9[i]) for i in range(len(b10))]
    return "".join(b12)
b13 = fonk3(b3, b4)
b14 = fonk5(b13, b4)
print(f"Original Message: {b3}")
print(f"Encrypted Message: {b13}")
print(f"Decrypted Message: {b14}")