import ipfsapi
DEBUG = False
POINT_FILENAME = 'pointt'
KEY_FILENAME = 'TEST_RANDOM_DO_NOT_USE_IN_REAL_CONVERSATION.txt'
IPFS_HOST = '127.0.0.1'
IPFS_PORT = 5001
api = ipfsapi.connect(IPFS_HOST, IPFS_PORT)
with open(KEY_FILENAME, 'r') as f:
    all_random = f.read()
def save_point(point):
    with open(POINT_FILENAME, 'w') as fpoint:
        fpoint.write(str(point))
def debug_print(message, *args):
    if DEBUG:
        print(message, *args)
def encrypt(text, key):
    return "".join(chr(ord(char) ^ ord(k)) for char, k in zip(text, key))
def main():
    global point
    point = 0
    print("You:")
    while True:
        data = input()
        debug_print('Current point:', point)
        end = point + len(data)
        debug_print('End point:', end)
        key = all_random[point:end]
        debug_print('Encryption key:', key)
        encrypted_data = encrypt(data, key)
        debug_print('Encrypted data:', encrypted_data)
        data_ipfs = api.add_pyobj([encrypted_data, point, end])
        debug_print('IPFS data:', [encrypted_data, point, end])
        data_ipns = api.name_publish('/ipfs/' + data_ipfs)
        debug_print('IPFS name published:', data_ipns)
        point = end
        save_point(point)
if __name__ == "__main__":
    main()