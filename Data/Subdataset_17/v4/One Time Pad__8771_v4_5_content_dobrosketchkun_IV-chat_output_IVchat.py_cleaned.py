import ipfsapi
from roster import roster as roster
api = ipfsapi.connect('127.0.0.1', 5001)
DEBUG = 0
point = 0
def debug_print(message, *args):
    if DEBUG == 1:
        print(message, *args)
def encrypt(string, key):
    return "".join(chr(ord(i) ^ ord(j)) for i, j in zip(string, key))
def decrypt(ciphertext, key):
    return encrypt(ciphertext, key)
with open('TEST_RANDOM_DO_NOT_USE_IN_REAL_CONVERSATION.txt', 'r') as f:
    all_random = f.read()
print('Chat:')
data1 = [None for _ in roster]
data2 = [None for _ in roster]
while True:
    try:
        for number in range(len(roster)):
            debug_print('number', number)
            debug_print('IPNS key', roster[number][0])
            data = api.get_pyobj('/ipns/' + roster[number][0])
            debug_print('data from IPFS', data)
            point = data[1]
            debug_print('point', point)
            end = data[2]
            debug_print('end', end)
            key = all_random[point:end]
            debug_print('key', key)
            decrypted_message = decrypt(data[0], key)
            debug_print('decrypted message', decrypted_message)
            data2[number] = data
            debug_print('data2', data2)
            if decrypted_message != data1[number]:
                print(f"{roster[number][1]}: {decrypted_message}")
                data1[number] = decrypted_message
    except Exception as e:
        debug_print('Exception', e)