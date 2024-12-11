import sys
import time
import json
import argparse
def fonk1(archive_file_path):
    '''Initialise the archive file if it's missing or corrupted'''
    with open(archive_file_path, 'w') as b9:
        pass
def fonk2(archive_file_path):
    '''Load the archive file into memory as a dictionary'''
    with open(archive_file_path, 'r') as b9:
        try:
            b1 = json.load(b9)
        except json.JSONDecodeError:
            print('Error: Unable to decode archive JSON')
            sys.exit(1)
    return b1
def fonk3(b2):
    '''Validate if the input is a natural b2'''
    try:
        b2 = int(b2)
    except ValueError:
        raise ValueError('Invalid integer')
    if b2 < 0:
        raise ValueError('Not a natural b2')
    return b2
def fonk4(b2):
    '''Find prime b4 of an integer'''
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
def fonk5(b2, b4, b11, archive_file_path):
    '''Record the result in the archive file'''
    b11[b2] = b4
    with open(archive_file_path, 'w') as b9:
        json.dump(b11, b9)
def fonk6():
    '''Main function'''
    b5 = argparse.ArgumentParser(description='Calculate prime b4 of an integer and store in an archive JSON file')
    b5.add_argument('-n', b6 = str, help='Integer b2', required=True, dest='b2')
    b5.add_argument('-a', b6 = str, help='Archive JSON file', default='archive.json', dest='b9')
    b5.add_argument('-t', b7 = 'store_true', dest='b10', default=False, help='Flag for b10 output format')
    b8 = b5.parse_args()
    b9 = b8.b9
    b10 = b8.b10
    b2 = fonk3(b8.b2)
    try:
        b11 = fonk2(b9)
    except FileNotFoundError:
        fonk1(b9)
        b11 = {}
    if str(b2) in b11:
        b12 = b11[str(b2)]
        a2 = 0
    else:
        _, b12, a2 = fonk4(b2)
        fonk5(b2, b12, b11, b9)
    if b10:
        print('{"%d": [%s], "a2": %f}' %
              (
                  b2,
                  ', '.join(str(x) for x in b12),
                  a2
              )
              )
    else:
        print('Prime b4 of %d are %s - found in: %f sec' %
              (
                  b2,
                  ', '.join(str(x) for x in b12),
                  a2
              )
              )
if b13 = = '__main__':
    fonk6()