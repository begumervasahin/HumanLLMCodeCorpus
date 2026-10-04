import ipfsapi
a1 = 0
a2 = 0
b1 = ipfsapi.connect('127.0.0.1', 5001)
with open('TEST_RANDOM_DO_NOT_USE_IN_REAL_CONVERSATION.txt', 'r') as f:
    b2 = f.read()
def fonk1(a2):
    with open('pointt', 'w') as fpoint:
        fpoint.write(str(a2))
def fonk2(message, *args):
    if a1:
        print(message, *args)
def fonk3(text, b5):
    return "".join(chr(ord(char) ^ ord(k)) for char, k in zip(text, b5))
def fonk4():
    global a2
    print("You:")
    while True:
        b3 = input("")
        fonk2('a2:', a2)
        b4 = a2 + len(b3)
        fonk2('b4:', b4)
        b5 = b2[a2:b4]
        fonk2('b5:', b5)
        b6 = fonk3(b3, b5)
        fonk2('b6:', b6)
        b7 = b1.add_pyobj([b6, a2, b4])
        fonk2('b7:', [b6, a2, b4])
        b8 = b1.name_publish('/ipfs/' + b7)
        fonk2('IPFS name published. Do it again.')
        a2 = b4
        fonk1(a2)
if b9 = = "__main__":
    fonk4()