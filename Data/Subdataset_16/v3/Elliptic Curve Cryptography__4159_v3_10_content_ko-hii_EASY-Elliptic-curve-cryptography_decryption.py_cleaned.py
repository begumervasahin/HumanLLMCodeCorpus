from key_exchange import add_point
from multiprocessing import Pool
def fonk1(data):
    b1 = data['send_data']
    b2 = data['point']
    b3 = data['b3']
    b4 = b2
    a1 = 1
    while b4 != b1:
        a1 += 1
        b4 = add_point(b4, b2, b3)
    return a1
def fonk2(info, b3):
    b2 = info['b2']
    b5 = info['b5']
    b6 = info['b6']
    with Pool(2) as pool:
        b7 = pool.map(decryption, [
            {'point': b2, 'send_data': b5, 'b3': b3},
            {'point': b2, 'send_data': b6, 'b3': b3}
        ])
    alice_secret_key, b8 = b7
    print(f'Alice secret b9 = {alice_secret_key}')
    print(f'Bob secret b9 = {b8}')
    return {'alice_secret': alice_secret_key, 'bob_secret': b8}
if b10 = = "__main__":
    b11 = {
        'b2': (2, 3),
        'b5': (5, 1),
        'b6': (9, 4)
    }
    b12 = {'a': 1, 'b': 1, 'p': 23}
    b13 = fonk2(b11, b12)
    print(b13)