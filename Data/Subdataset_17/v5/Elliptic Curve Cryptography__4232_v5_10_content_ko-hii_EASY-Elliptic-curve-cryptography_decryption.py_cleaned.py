from key_exchange import add_point
from multiprocessing import Pool
def decrypt_secret_key(data):
    target = data['send_data']
    public_point = data['point']
    param = data['param']
    temp_point = public_point
    secret_key = 1
    while temp_point != target:
        secret_key += 1
        temp_point = add_point(temp_point, public_point, param)
    return secret_key
def decryption_main(info, param):
    public_point = info['public_point']
    send_data_alice = info['send_data_alice']
    send_data_bob = info['send_data_bob']
    data_for_decryption = [
        {'point': public_point, 'send_data': send_data_alice, 'param': param},
        {'point': public_point, 'send_data': send_data_bob, 'param': param}
    ]
    with Pool(2) as pool:
        secret_keys = pool.map(decrypt_secret_key, data_for_decryption)
    alice_secret_key, bob_secret_key = secret_keys
    print(f'Alice secret key = {alice_secret_key}')
    print(f'Bob secret key = {bob_secret_key}')
    return {'alice_secret': alice_secret_key, 'bob_secret': bob_secret_key}
if __name__ == "__main__":
    example_info = {
        'public_point': (2, 3),
        'send_data_alice': (5, 1),
        'send_data_bob': (9, 4)
    }
    example_param = {'a': 1, 'b': 1, 'p': 23}
    result = decryption_main(example_info, example_param)
    print(result)