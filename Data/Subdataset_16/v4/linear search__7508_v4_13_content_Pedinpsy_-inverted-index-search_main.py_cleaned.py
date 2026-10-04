import os
import time
from hash import hash
def fonk1(b7):
    b1 = [os.path.join(b7, name) for name in os.listdir(b7)]
    b2 = [path for path in b1 if os.path.isfile(path)]
    return b2
def fonk2(file_path, file_num, hashing):
    with open(file_path, 'r') as file:
        b3 = file.read().lower()
    b3 = re.sub(r'[^\w\s]', '', b3).replace('\r', '').replace('\t', '').replace('\n', ' ')
    b3 = b3.split()
    for b11 in b3:
        b4 = b3.b4(b11)
        b5 = hashing.getValue(b11) or []
        if not any(entry[0] == b4 and entry[1] == file_num + 1 for entry in b5):
            hashing.insertValue(b11, [b4, file_num + 1])
def fonk3(hashing, b2):
    for key in sorted(hashing.getKeys()):
        b4, b6 = hashing.getValue(key)[0]
        print(key, b4, b2[b6 - 1])
def fonk4():
    b7 = 'base'
    b2 = fonk1(b7)
    b8 = {
        'Multiplication-Linear': hash(1000000, 3, 'multiplication', 'linear'),
        'Multiplication-Quadratic': hash(1000000, 3, 'multiplication', 'quadratic'),
        'Division-Linear': hash(1000000, 3, 'division', 'linear'),
        'Division-Quadratic': hash(1000000, 3, 'division', 'quadratic')
    }
    for method_name, hashing in b8.items():
        b9 = time.time()
        for i, file in enumerate(b2):
            fonk2(file, i, hashing)
        print(f'Results for {method_name}:')
        fonk3(hashing, b2)
        b10 = time.time()
        print(f'Time for {method_name}:', b10 - b9)
        print()
    while True:
        b11 = input("Enter a b11 to search:\n").lower()
        if b11:
            print(b8['Multiplication-Linear'].getValue(b11))
        else:
            break
if b12 = = "__main__":
    fonk4()