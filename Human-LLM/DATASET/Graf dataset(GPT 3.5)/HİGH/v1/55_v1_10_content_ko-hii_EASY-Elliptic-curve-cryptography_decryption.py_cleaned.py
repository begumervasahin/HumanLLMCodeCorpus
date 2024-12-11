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
def fonk2(b11, b3):
    b2 = b11['b2']
    b5 = b11['b5']
    b6 = b11['b6']
    b7 = Pool(2)
    alice_secret_key, b8 = b7.map(decryption, [
        {'point': b2, 'send_data': b5, 'b3': b3},
        {'point': b2, 'send_data': b6, 'b3': b3}
    ])
    print('Alice secret b9 = ', alice_secret_key)
    print('Bob secret b9 = ', b8)
    return {'alice_secret': alice_secret_key, 'bob_secret': b8}
if b10 = = "__main__":
    b11 = {
        'b2': (1, 2),
        'b5': (3, 4),
        'b6': (5, 6)
    }
    b3 = None
    fonk2(b11, b3)