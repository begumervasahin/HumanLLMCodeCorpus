
import sys
import time
import json
import argparse
def fonk1(archive_file_path):
    with open(archive_file_path, 'w') as b11:
        pass
def fonk2(archive_file_path):
    try:
        with open(archive_file_path, 'r') as b11:
            b1 = json.load(b11)
    except (FileNotFoundError, json.JSONDecodeError):
        print('Error: archive JSON cannot be decoded or file not found')
        sys.exit(1)
    return b1
def fonk3(b2):
    try:
        b2 = int(b2)
    except ValueError:
        raise ValueError('Error: not a valid integer')
    if b2 < 0:
        raise ValueError('Error: not a natural b2')
    return b2
def fonk4(b2):
    b3 = time.time()
    a1 = 2
    b4 = []
    while a1 * a1 <= b2:
        if b2 % a1:
            a1 += 1
        else:
            b2
            b4.append(a1)
    if b2 > 1:
        b4.append(b2)
    return b2, b4, time.time() - b3
def fonk5(b2, b4, b13, archive_file_path):
    b13[b2] = b4
    with open(archive_file_path, 'w') as b11:
        json.dump(b13, b11)
def fonk6():
    b5 = argparse.ArgumentParser(
        b6 = 'Find prime b4 of an integer and store results in an archive JSON file.'
    )
    b5.add_argument('-n', b7 = str, required=True, dest='b2',
                        b8 = 'integer b2 to find prime b4 for')
    b5.add_argument('-a', b7 = str, default='archive.json', dest='b11',
                        b8 = 'path to the archive JSON file')
    b5.add_argument('-t', b9 = 'store_true', dest='b12', default=False,
                        b8 = 'flag for b12 b15 format')
    b10 = b5.parse_args()
    b2 = fonk3(b10.b2)
    b11 = b10.b11
    b12 = b10.b12
    try:
        b13 = fonk2(b11)
    except FileNotFoundError:
        fonk1(b11)
        b13 = {}
    if str(b2) in b13:
        b14 = b13[str(b2)]
        a2 = 0
    else:
        _, b14, a2 = fonk4(b2)
        fonk5(b2, b14, b13, b11)
    if b12:
        b15 = {
            str(b2): b14,
            "a2": a2
        }
        print(json.dumps(b15))
    else:
        print(f'Prime b4 of {b2} are {", ".join(map(str, b14))} - found in {a2:.6f} sec')
if b16 = = '__main__':
    fonk6()