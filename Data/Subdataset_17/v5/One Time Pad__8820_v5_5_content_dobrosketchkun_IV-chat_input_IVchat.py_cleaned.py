import ipfsapi
DEBUG = 0
point = 0
api = ipfsapi.connect('127.0.0.1', 5001)
with open('TEST_RANDOM_DO_NOT_USE_IN_REAL_CONVERSATION.txt', 'r') as f:
    all_random = f.read()
def save_point(point):
    with open('pointt', 'w') as fpoint:
        fpoint.write(str(point))
def debug_print(message, *args):
    if DEBUG:
        print(message, *args)
def encrypt(string, key):
    return "".join(chr(ord(s) ^ ord(k)) for s, k in zip(string, key))
def main():
    global point
    print("You:")
    while True:
        data = input("")
        debug_print('point:', point)
        end = point + len(data)
        debug_print('end:', end)
        key = all_random[point:end]
        debug_print('key:', key)
        data_enc = encrypt(data, key)
        debug_print('data_enc:', data_enc)
        data_ipfs = api.add_pyobj([data_enc, point, end])
        debug_print('data_ipfs:', [data_enc, point, end])
        data_ipns = api.name_publish('/ipfs/' + data_ipfs)
        debug_print('IPFS published:', data_ipns)
        point = end
        save_point(point)
if __name__ == "__main__":
    main()