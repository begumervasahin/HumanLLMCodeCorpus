import ipfsapi
from roster import roster
api = ipfsapi.connect('127.0.0.1', 5001)
DEBUG = False
def debug_print(message, *args):
    if DEBUG:
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
                debug_print('Index:', index)
                debug_print('User ID:', user_id)
                data = api.get_pyobj('/ipns/' + user_id)
                debug_print('Data:', data)
                point, end = data[1], data[2]
                debug_print('Point:', point)
                debug_print('End:', end)
                key = all_random[point:end]
                debug_print('Key:', key)
                decrypted_message = decrypt(data[0], key)
                debug_print('Decrypted Message:', decrypted_message)
                current_data[index] = data
                if decrypted_message != previous_messages[index]:
                    print(f"{username}: {decrypted_message}")
                    previous_messages[index] = decrypted_message
        except Exception as e:
            debug_print('Error:', e)
if __name__ == "__main__":
    main()