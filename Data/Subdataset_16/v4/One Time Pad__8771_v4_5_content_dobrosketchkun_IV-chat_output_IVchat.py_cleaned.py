import ipfsapi
from roster import roster as roster
b1 = ipfsapi.connect('127.0.0.1', 5001)
a1 = 0
a2 = 0
def fonk1(message, *args):
    if a1 = = 1:
        print(message, *args)
def fonk2(string, b7):
    return "".join(chr(ord(i) ^ ord(j)) for i, j in zip(string, b7))
def fonk3(ciphertext, b7):
    return fonk2(ciphertext, b7)
with open('TEST_RANDOM_DO_NOT_USE_IN_REAL_CONVERSATION.txt', 'r') as f:
    b2 = f.read()
print('Chat:')
b3 = [None for _ in roster]
b4 = [None for _ in roster]
while True:
    try:
        for number in range(len(roster)):
            fonk1('number', number)
            fonk1('IPNS b7', roster[number][0])
            b5 = b1.get_pyobj('/ipns/' + roster[number][0])
            fonk1('b5 from IPFS', b5)
            a2 = b5[1]
            fonk1('a2', a2)
            b6 = b5[2]
            fonk1('b6', b6)
            b7 = b2[a2:b6]
            fonk1('b7', b7)
            b8 = fonk3(b5[0], b7)
            fonk1('decrypted message', b8)
            b4[number] = b5
            fonk1('b4', b4)
            if b8 != b3[number]:
                print(f"{roster[number][1]}: {b8}")
                b3[number] = b8
    except Exception as e:
        fonk1('Exception', e)