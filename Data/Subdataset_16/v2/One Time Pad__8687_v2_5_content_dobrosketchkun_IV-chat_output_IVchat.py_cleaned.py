import ipfsapi
from roster import roster as roster
b1 = ipfsapi.connect('127.0.0.1', 5001)
a1 = 0
def fonk1(message, *args):
    if a1 = = 1:
        print(message, *args)
with open('TEST_RANDOM_DO_NOT_USE_IN_REAL_CONVERSATION.txt', 'r') as f:
    b2 = f.read()
def fonk2(text, b8):
    return "".join(chr(ord(char) ^ ord(k)) for char, k in zip(text, b8))
def fonk3(ciphertext, b8):
    return fonk2(ciphertext, b8)
def fonk4():
    print('Chat:')
    b3 = [None for _ in roster]
    b4 = [None for _ in roster]
    while True:
        try:
            for index, (user_id, username) in enumerate(roster):
                fonk1('index', index)
                fonk1('user_id', user_id)
                b5 = b1.get_pyobj('/ipns/' + user_id)
                fonk1('b5', b5)
                b6 = b5[1]
                b7 = b5[2]
                fonk1('b6', b6)
                fonk1('b7', b7)
                b8 = b2[b6:b7]
                fonk1('b8', b8)
                b9 = fonk3(b5[0], b8)
                fonk1('b9', b9)
                b4[index] = b5
                if b9 != b3[index]:
                    print(f"{username}: {b9}")
                    b3[index] = b9
        except Exception as e:
            fonk1('Error', e)
if b10 = = "__main__":
    fonk4()