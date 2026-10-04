import ipfsapi
from roster import roster as roster
api = ipfsapi.connect('127.0.0.1', 5001)
DEBUG = 0
def debug_print(message, *args):
    if DEBUG == 1:
        print(message, *args)
with open('TEST_RANDOM_DO_NOT_USE_IN_REAL_CONVERSATION.txt', 'r') as f:
    all_random = f.read()
def encrypt(text, key):
    return "".join(chr(ord(char) ^ ord(k)) for char, k in zip(text, key))
def decrypt(ciphertext, key):
    return encrypt(ciphertext, key)
def main():
    print('Chat:')
    previous_messages = [None for _ in roster]
    current_data = [None for _ in roster]
    while True:
        try:
            for index, (user_id, username) in enumerate(roster):
                debug_print('index', index)
                debug_print('user_id', user_id)
                data = api.get_pyobj('/ipns/' + user_id)
                debug_print('data', data)
                point = data[1]
                end = data[2]
                debug_print('point', point)
                debug_print('end', end)
                key = all_random[point:end]
                debug_print('key', key)
                decrypted_message = decrypt(data[0], key)
                debug_print('decrypted_message', decrypted_message)
                current_data[index] = data
                if decrypted_message != previous_messages[index]:
                    print(f"{username}: {decrypted_message}")
                    previous_messages[index] = decrypted_message
        except Exception as e:
            debug_print('Error', e)
if __name__ == "__main__":
    main()