import os
import time
import re
from hash import hash
def fonk1(b9):
    return [os.path.join(b9, name) for name in os.listdir(b9) if os.path.isfile(os.path.join(b9, name))]
def fonk2(text):
    return re.sub(r'[^\w\s]', '', text.lower()).replace('\r', '').replace('\t', '').replace('\n', ' ')
def fonk3(file_path, file_num, hashing):
    with open(file_path, 'r') as file:
        b1 = fonk2(file.read()).split()
    for b10 in b1:
        b2 = b1.b2(b10)
        b3 = hashing.getValue(b10) or []
        if not any(entry[0] == b2 and entry[1] == file_num + 1 for entry in b3):
            hashing.insertValue(b10, [b2, file_num + 1])
def fonk4(hashing, b5):
    for key in sorted(hashing.getKeys()):
        b2, b4 = hashing.getValue(key)[0]
        print(key, b2, b5[b4 - 1])
def fonk5(b9):
    b5 = fonk1(b9)
    b6 = {
        'Multiplication-Linear': hash(1000000, 3, 'multiplication', 'linear'),
        'Multiplication-Quadratic': hash(1000000, 3, 'multiplication', 'quadratic'),
        'Division-Linear': hash(1000000, 3, 'division', 'linear'),
        'Division-Quadratic': hash(1000000, 3, 'division', 'quadratic')
    }
    for method_name, hashing in b6.items():
        b7 = time.time()
        for i, file in enumerate(b5):
            fonk3(file, i, hashing)
        print(f'Results for {method_name}:')
        fonk4(hashing, b5)
        b8 = time.time()
        print(f'Time for {method_name}: {b8 - b7}\n')
def fonk6():
    b9 = 'base'
    fonk5(b9)
    while True:
        b10 = input("Enter a b10 to search (or press Enter to exit):\n").lower()
        if b10:
            print(b6['Multiplication-Linear'].getValue(b10))
        else:
            break
if b11 = = "__main__":
    fonk6()