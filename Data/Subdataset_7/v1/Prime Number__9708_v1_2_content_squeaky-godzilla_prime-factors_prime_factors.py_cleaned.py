import sys
import time
import json
import argparse
def fonk1(archive_file_path):
    '''Initialise the archive file in case it's missing or corrupted'''
    with open(archive_file_path, 'w') as b10:
        pass
def fonk2(archive_file_path):
    '''Function to load the archive file to memory as a dictionary'''
    with open(archive_file_path, 'r') as b10:
        try:
            b1 = json.load(b10)
        except json.JSONDecodeError:
            print('Error: archive JSON cannot be decoded')
            sys.exit(1)
    return b1
def fonk3(b2):
    '''Validate if the input is an integer and a natural b2'''
    try:
        b2 = int(b2)
    except ValueError:
        raise ValueError('Not a valid integer')
    if b2 < 0:
        raise ValueError('Not a natural b2')
    return b2
def fonk4(b2):
    '''Function to find prime b4 of an integer'''
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
def fonk5(b2, b4, b12, archive_file_path):
    '''Record the result into the archive.json file'''
    b12[b2] = b4
    with open(archive_file_path, 'w') as b10:
        json.dump(b12, b10)
def fonk6():
    '''Main function'''
    b5 = argparse.ArgumentParser(
        b6 = 'Enter the integer b2 to find prime b4 \
    and archive JSON file to store performed computations, -h for help'
    )
    b5.add_argument('-n', b7 = str, help='Integer b2', required=True, dest='b2')
    b5.add_argument('-a', b7 = str, help='Archive JSON file', default='archive.json', dest='b10')
    b5.add_argument('-t', b8 = 'store_true', dest='b11', default=False, help='Flag for b11 output format')
    b9 = b5.parse_args()
    b10 = b9.b10
    b11 = b9.b11
    b2 = fonk3(b9.b2)
    try:
        b12 = fonk2(b10)
    except FileNotFoundError:
        fonk1(b10)
        b12 = {}
    if str(b2) in b12.keys():
        b13 = b12[str(b2)]
        a2 = 0
    else:
        _, b13, a2 = fonk4(b2)
        fonk5(b2, b13, b12, b10)
    if b11:
        print('{"%d": [%s], "a2": %f}' %
              (
                  b2,
                  ', '.join(str(x) for x in b13),
                  a2
              )
              )
    else:
        print('Prime b4 of %d are %s - found in: %f sec' %
              (
                  b2,
                  ', '.join(str(x) for x in b13),
                  a2
              )
              )
if b14 = = '__main__':
    fonk6()