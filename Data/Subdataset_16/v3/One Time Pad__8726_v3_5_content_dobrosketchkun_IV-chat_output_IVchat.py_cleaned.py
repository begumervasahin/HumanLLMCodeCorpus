import ipfsapi
from roster import roster
b1 = ipfsapi.connect('127.0.0.1', 5001)
b2 = False
def fonk1(message, *args):
    if b2:
        print(message, *args)
with open('TEST_RANDOM_DO_NOT_USE_IN_REAL_CONVERSATION.txt', 'r') as f:
    b3 = f.read()
def fonk2(text, b8):
    return "".join(chr(ord(char) ^ ord(k)) for char, k in zip(text, b8))
def fonk3(ciphertext, b8):
    return fonk2(ciphertext, b8)
def fonk4():
    print('Chat:')
    b4 = [None for _ in roster]
    b5 = [None for _ in roster]
    while True:
        try:
            for index, (user_id, username) in enumerate(roster):
                fonk1('Index:', index)
                fonk1('User ID:', user_id)
                b6 = b1.get_pyobj('/ipns/' + user_id)
                fonk1('Data:', b6)
                point, b7 = b6[1], b6[2]
                fonk1('Point:', point)
                fonk1('End:', b7)
                b8 = b3[point:b7]
                fonk1('Key:', b8)
                b9 = fonk3(b6[0], b8)
                fonk1('Decrypted Message:', b9)
                b5[index] = b6
                if b9 != b4[index]:
                    print(f"{username}: {b9}")
                    b4[index] = b9
        except Exception as e:
            fonk1('Error:', e)
if b10 = = "__main__":
    fonk4()