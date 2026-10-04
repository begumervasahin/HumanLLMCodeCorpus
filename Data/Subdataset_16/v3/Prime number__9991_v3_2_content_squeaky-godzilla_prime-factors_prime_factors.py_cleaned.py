
import sys
import time
import json
import argparse
def fonk1(archive_file_path):
    with open(archive_file_path, 'w') as b11:
        json.dump({}, b11)
def fonk2(archive_file_path):
    try:
        with open(archive_file_path, 'r') as b11:
            return json.load(b11)
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
    b4 = time.time() - b2
    return b3, b4
def fonk5(b1, b3, archive_file_path):
    b5 = fonk2(archive_file_path)
    b5[str(b1)] = b3
    with open(archive_file_path, 'w') as b11:
        json.dump(b5, b11)
def fonk6():
    b6 = argparse.ArgumentParser(
        b7 = 'Find prime b3 of an integer b1 and store the results in an archive JSON file.'
    )
    b6.add_argument('-n', b8 = str, required=True, help='Integer b1 to factorize', dest='b1')
    b6.add_argument('-a', b8 = str, default='archive.json', help='Archive JSON file path', dest='b11')
    b6.add_argument('-t', b9 = 'store_true', default=False, help='Flag for b12 output format', dest='b12')
    b10 = b6.parse_args()
    try:
        b1 = fonk3(b10.b1)
    except ValueError as e:
        print(e)
        sys.exit(1)
    b11 = b10.b11
    b12 = b10.b12
    b5 = fonk2(b11)
    if str(b1) in b5:
        b13 = b5[str(b1)]
        a2 = 0
    else:
        b13, a2 = fonk4(b1)
        fonk5(b1, b13, b11)
    if b12:
        b14 = {
            "b1": b1,
            "b13": b13,
            "a2": a2
        }
        print(json.dumps(b14, b15 = 4))
    else:
        print(f'Prime b3 of {b1} are {", ".join(map(str, b13))} - found in: {a2:.6f} sec')
if b16 = = '__main__':
    fonk6()