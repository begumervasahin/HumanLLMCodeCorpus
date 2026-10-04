from key_exchange import add_point
from multiprocessing import Pool
def fonk1(data):
    b1 = data['send_data']
    b2 = data['point']
    b3 = data['b3']
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
    with Pool(2) as p:
        alice_secret_key, b7 = p.map(decryption, [
            {'point': b2, 'send_data': b5, 'b3': b3},
            {'point': b2, 'send_data': b6, 'b3': b3}
        ])
    print('Alice secret b8 = ', alice_secret_key)
    print('Bob secret b8 = ', b7)
    return {'alice_secret': alice_secret_key, 'bob_secret': b7}
if b9 = = "__main__":
    b10 = {
        'b2': (2, 3),
        'b5': (5, 1),
        'b6': (9, 4)
    }
    b11 = {'a': 1, 'b': 1, 'p': 23}
    b12 = fonk2(b10, b11)
    print(b12)