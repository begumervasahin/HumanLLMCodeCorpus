
import sys
import time
import json
import argparse
def fonk1(archive_file_path):
    with open(archive_file_path, 'w') as b12:
        pass
def fonk2(archive_file_path):
    try:
        with open(archive_file_path, 'r') as b12:
            b1 = json.load(b12)
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
    b4 = []
    a1 = 2
    b5 = b2
    while a1 * a1 <= b2:
        if b2 % a1:
            a1 += 1
        else:
            b2
            b4.append(a1)
    if b2 > 1:
        b4.append(b2)
    return b5, b4, time.time() - b3
def fonk5(b2, b4, b14, archive_file_path):
    b14[b2] = b4
    with open(archive_file_path, 'w') as b12:
        json.dump(b14, b12)
def fonk6():
    b6 = argparse.ArgumentParser(
        b7 = 'Find prime b4 of an integer and store results in an archive JSON file.'
    )
    b6.add_argument('-n', b8 = str, required=True, dest='b2',
                        b9 = 'integer b2 to find prime b4 for')
    b6.add_argument('-a', b8 = str, default='archive.json', dest='b12',
                        b9 = 'path to the archive JSON file')
    b6.add_argument('-t', b10 = 'store_true', dest='b13', default=False,
                        b9 = 'flag for b13 b16 format')
    b11 = b6.parse_args()
    b2 = fonk3(b11.b2)
    b12 = b11.b12
    b13 = b11.b13
    try:
        b14 = fonk2(b12)
    except FileNotFoundError:
        fonk1(b12)
        b14 = {}
    if str(b2) in b14:
        b15 = b14[str(b2)]
        a2 = 0
    else:
        _, b15, a2 = fonk4(b2)
        fonk5(b2, b15, b14, b12)
    if b13:
        b16 = {
            str(b2): b15,
            "a2": a2
        }
        print(json.dumps(b16))
    else:
        print(f'Prime b4 of {b2} are {", ".join(map(str, b15))} - found in {a2:.6f} sec')
if b17 = = '__main__':
    fonk6()