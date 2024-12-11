
a1 = 43
a2 = 59
b1 = a1 * a2
a3 = 13
def fonk1():
    b2 = input("\nEnter your message: ").upper()
    print("User Message:", b2)
    return b2
def fonk2(b2):
    b3 = [str(ord(character) - ord('A')) for character in b2]
    print("Message Integers:", b3)
    return b3
def fonk3():
    b4 = len(str(b1))
    print("Block Size:", b4)
    return b4
def fonk4(b3, b4):
    b5 = [b3[i:i+b4] for i in range(0, len(b3), b4)]
    print("Blocked Message Integers:", b5)
    return b5
def fonk5(block, b4):
    if len(block) < b4:
        block += ['0'] * (b4 - len(block))
    return block
def fonk6(b5):
    b6 = [(int(''.join(block)) ** a3) % b1 for block in b5]
    print("Encrypted Messages:", b6)
    return b6
def fonk7(b6):
    b7 = ''.join(map(str, b6))
    print("\nEncrypted Messages:", b7)
    return b7
def fonk8():
    b2 = fonk1()
    b3 = fonk2(b2)
    b4 = fonk3()
    b5 = fonk4(b3, b4)
    b8 = [fonk5(block, b4) for block in b5]
    b6 = fonk6(b8)
    fonk7(b6)
if b9 = = "__main__":
    fonk8()