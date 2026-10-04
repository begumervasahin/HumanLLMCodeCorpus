
import sys
import time
import json
import argparse
def fonk1(archive_file_path):
    with open(archive_file_path, 'w') as b10:
        json.dump({}, b10)
def fonk2(archive_file_path):
    try:
        with open(archive_file_path, 'r') as b10:
            return json.load(b10)
    except (FileNotFoundError, json.JSONDecodeError):
        print('Error: archive JSON cannot be decoded. Initializing a new archive.')
        fonk1(archive_file_path)
        return {}
def fonk3(number_str):
    try:
        b1 = int(number_str)
        if b1 < 0:
            raise ValueError
        return b1
    except ValueError:
        raise ValueError('Input is not a valid natural b1')
def fonk4(b1):
    b2 = time.time()
    b3 = []
    a1 = 2
    while a1 * a1 <= b1:
        if b1 % a1:
            a1 += 1
        else:
            b1
            b3.append(a1)
    if b1 > 1:
        b3.append(b1)
    return b3, time.time() - b2
def fonk5(b1, b3, archive_file_path):
    b4 = fonk2(archive_file_path)
    b4[str(b1)] = b3
    with open(archive_file_path, 'w') as b10:
        json.dump(b4, b10)
def fonk6():
    b5 = argparse.ArgumentParser(
        b6 = 'Find prime b3 of an integer b1 and store the results in an archive JSON file.'
    )
    b5.add_argument('-n', b7 = str, required=True, help='Integer b1 to factorize', dest='b1')
    b5.add_argument('-a', b7 = str, default='archive.json', help='Archive JSON file path', dest='b10')
    b5.add_argument('-t', b8 = 'store_true', default=False, help='Flag for b11 output format', dest='b11')
    b9 = b5.parse_args()
    b1 = fonk3(b9.b1)
    b10 = b9.b10
    b11 = b9.b11
    b4 = fonk2(b10)
    if str(b1) in b4:
        b12 = b4[str(b1)]
        a2 = 0
    else:
        b12, a2 = fonk4(b1)
        fonk5(b1, b12, b10)
    if b11:
        print(json.dumps({b1: b12, "a2": a2}))
    else:
        print(f'Prime b3 of {b1} are {", ".join(map(str, b12))} - found in: {a2:.6f} sec')
if b13 = = '__main__':
    fonk6()