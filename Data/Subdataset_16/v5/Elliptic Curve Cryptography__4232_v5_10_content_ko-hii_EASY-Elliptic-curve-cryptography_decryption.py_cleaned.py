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
    b7 = [
        {'point': b2, 'send_data': b5, 'b3': b3},
        {'point': b2, 'send_data': b6, 'b3': b3}
    ]
    with Pool(2) as pool:
        b8 = pool.map(decrypt_secret_key, b7)
    alice_secret_key, b9 = b8
    print(f'Alice secret b10 = {alice_secret_key}')
    print(f'Bob secret b10 = {b9}')
    return {'alice_secret': alice_secret_key, 'bob_secret': b9}
if b11 = = "__main__":
    b12 = {
        'b2': (2, 3),
        'b5': (5, 1),
        'b6': (9, 4)
    }
    b13 = {'a': 1, 'b': 1, 'p': 23}
    b14 = fonk2(b12, b13)
    print(b14)