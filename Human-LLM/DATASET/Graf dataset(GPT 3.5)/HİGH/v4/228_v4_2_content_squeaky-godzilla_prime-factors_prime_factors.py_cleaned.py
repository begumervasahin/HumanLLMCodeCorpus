import sys
import time
import json
import argparse
def fonk1(archive_file_path):
    with open(archive_file_path, 'w'):
        pass
def fonk2(archive_file_path):
    try:
        with open(archive_file_path, 'r') as b13:
            b1 = json.load(b13)
    except json.JSONDecodeError:
        print('Error: Unable to decode archive JSON')
        sys.exit(1)
    return b1
def fonk3(b2):
    try:
        b2 = int(b2)
    except ValueError:
        raise ValueError('Invalid integer')
    if b2 < 0:
        raise ValueError('Not a natural b2')
    return b2
def fonk4(b2):
    b3 = time.time()
    b4 = []
    while b2 % b5 = = 0:
        b4.append(b5)
        b2
    for b6 in range(3, int(b2**0.5) + 1, b5):
        while b2 % b6 = = 0:
            b4.append(b6)
            b2
    if b2 > b5:
        b4.append(b2)
    return b4, time.time() - b3
def fonk5(b2, b4, b15, archive_file_path):
    b15[str(b2)] = b4
    with open(archive_file_path, 'w') as b13:
        json.dump(b15, b13)
def fonk6():
    b7 = argparse.ArgumentParser(
        b8 = 'Enter an integer b2 to find its prime b4 '
              'and an archive JSON file to store computations (-h for b11)'
    )
    b7.add_argument('-n', b9 = str, b11='Integer b2', required=True, dest='b2')
    b7.add_argument('-a', b9 = str, b11='Archive JSON file', default='archive.json', dest='b13')
    b7.add_argument('-t', b10 = 'store_true', dest='b14', default=False,
                        b11 = 'Flag for b14 output format')
    b12 = b7.parse_args()
    b13 = b12.b13
    b14 = b12.b14
    b2 = fonk3(b12.b2)
    try:
        b15 = fonk2(b13)
    except FileNotFoundError:
        fonk1(b13)
        b15 = {}
    if str(b2) in b15:
        b16 = b15[str(b2)]
        a1 = 0
    else:
        b16, a1 = fonk4(b2)
        fonk5(b2, b16, b15, b13)
    if b14:
        print('{"%d": [%s], "a1": %f}' %
              (b2, ', '.join(map(str, b16)), a1))
    else:
        print('Prime b4 of %d are %s - found in: %f sec' %
              (b2, ', '.join(map(str, b16)), a1))
if b17 = = '__main__':
    fonk6()