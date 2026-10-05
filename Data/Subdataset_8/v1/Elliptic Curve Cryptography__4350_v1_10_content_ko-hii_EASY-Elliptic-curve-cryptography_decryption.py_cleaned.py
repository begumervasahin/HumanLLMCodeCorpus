from key_exchange import add_point
from multiprocessing import Pool
def decryption(dic):
    target = dic['send_data']
    public_point = dic['point']
    param = dic['param']
    temp = public_point
    secret_key = 1
    while True:
        secret_key += 1
        temp = add_point(temp, public_point, param)
        if temp == target:
            return secret_key
def decryption_main(info, param):
    public_point = info['public_point']
    send_data_alice = info['send_data_alice']
    send_data_bob = info['send_data_bob']
    p = Pool(2)
    alice_secret_key, bob_secret_key = p.map(decryption, [
        {'point': public_point, 'send_data': send_data_alice, 'param': param},
        {'point': public_point, 'send_data': send_data_bob, 'param': param}
    ])
    print('Alice secret key =', alice_secret_key)
    print('Bob secret key =', bob_secret_key)
    return {'alice_secret': alice_secret_key, 'bob_secret': bob_secret_key}
if __name__ == "__main__":
    info = {
        'public_point': (1, 2),
        'send_data_alice': (3, 4),
        'send_data_bob': (5, 6)
    }
    param = None
    decryption_main(info, param)