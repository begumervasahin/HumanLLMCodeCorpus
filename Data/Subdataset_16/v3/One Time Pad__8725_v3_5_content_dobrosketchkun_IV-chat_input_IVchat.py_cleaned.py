import ipfsapi
b1 = False
b2 = 'pointt'
b3 = 'TEST_RANDOM_DO_NOT_USE_IN_REAL_CONVERSATION.txt'
b4 = '127.0.0.1'
a1 = 5001
b5 = ipfsapi.connect(b4, a1)
with open(b3, 'r') as f:
    b6 = f.read()
def fonk1(a2):
    with open(b2, 'w') as fpoint:
        fpoint.write(str(a2))
def fonk2(message, *args):
    if b1:
        print(message, *args)
def fonk3(text, b9):
    return "".join(chr(ord(char) ^ ord(k)) for char, k in zip(text, b9))
def fonk4():
    global a2
    a2 = 0
    print("You:")
    while True:
        b7 = input()
        fonk2('Current a2:', a2)
        b8 = a2 + len(b7)
        fonk2('End a2:', b8)
        b9 = b6[a2:b8]
        fonk2('Encryption b9:', b9)
        b10 = fonk3(b7, b9)
        fonk2('Encrypted b7:', b10)
        b11 = b5.add_pyobj([b10, a2, b8])
        fonk2('IPFS b7:', [b10, a2, b8])
        b12 = b5.name_publish('/ipfs/' + b11)
        fonk2('IPFS name published:', b12)
        a2 = b8
        fonk1(a2)
if b13 = = "__main__":
    fonk4()