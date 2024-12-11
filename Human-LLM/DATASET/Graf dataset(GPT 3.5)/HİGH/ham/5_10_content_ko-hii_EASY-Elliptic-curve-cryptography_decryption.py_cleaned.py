from key_exchange import add_point
from multiprocessing import Pool
def fonk1(dic):
    b1 = dic['send_data']
    b2 = dic['point']
    b3 = dic['b3']
    b4 = b2
    a1 = 1
    while True:
        a1 += 1
        b4 = add_point(b4, b2, b3)
        if b4 = = b1:
            return a1
def fonk2(info, b3):
    b2 = info['b2']
    b5 = info['b5']
    b6 = info['b6']
    b7 = Pool(2)
    alice_secret_key, b8 = b7.map(decryption, [
        {'point': b2, 'send_data': b5, 'b3': b3},
        {'point': b2, 'send_data': b6, 'b3': b3}
    ])
    print('alice secret b9 = ' + str(alice_secret_key))
    print('bob secret b9 = ' + str(b8))
    return {'alice_secret': alice_secret_key, 'bob_secret': b8}