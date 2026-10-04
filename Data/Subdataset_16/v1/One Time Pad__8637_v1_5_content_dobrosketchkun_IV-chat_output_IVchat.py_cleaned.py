import ipfsapi
from roster import roster as roster
b1 = ipfsapi.connect('127.0.0.1', 5001)
a1 = 0
def fonk1(x, *kargs):
    if a1 = = 1:
        print(x)
with open('TEST_RANDOM_DO_NOT_USE_IN_REAL_CONVERSATION.txt', 'r') as f:
    b2 = f.read()
def fonk2(string, b8):
    return "".join(chr(ord(i) ^ ord(j)) for (i, j) in zip(string, b8))
def fonk3(ciphertext, b8):
    return fonk2(ciphertext, b8)
print('Chat:')
b3 = [None for x in roster]
b4 = [None for x in roster]
while True:
    try:
        for number in range(len(roster)):
            fonk1('number', number)
            fonk1(roster[number][0])
            b5 = b1.get_pyobj('/ipns/' + roster[number][0])
            fonk1(['b4', b5])
            b6 = b5[1]
            fonk1(['b6', b6])
            b7 = b5[2]
            fonk1(['b7', b7])
            b8 = b2[b6:b7]
            fonk1(['b8', b8])
            b9 = fonk3(b5[0], b8)
            fonk1(['b9', b9])
            b4[number] = b5
            fonk1(b4)
            if b9 != b3[number]:
                print(roster[number][1] + ':', b9)
                b3[number] = b9
    except Exception as e:
        fonk1(['Nope,', e])