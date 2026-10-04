'''
Script to find prime b4 of an integer value
by
Vitek Urbanec, 2019
'''
import sys
import time
import json
import argparse
def fonk1(archive_file_path):
    '''Initialise the archive file in case it's missing or corrupted'''
    with open(archive_file_path, 'w') as b14:
        pass
def fonk2(archive_file_path):
    '''function to load the archive file to memory as a dictionary'''
    with open(archive_file_path, 'r') as b14:
        try:
            b1 = json.load(b14)
        except json.JSONDecodeError:
            print('Error: archive JSON cannot be decoded')
            sys.exit(1)
    return b1
def fonk3(b2):
    ''' validate if integer and natural b2 '''
    try:
        b2 = int(b2)
    except ValueError:
        raise Exception('not a valid integer')
    if b2 < 0:
        raise Exception('not a natural b2')
    return b2
def fonk4(b2):
    '''function to find prime b4 of an integer'''
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
def fonk5(b2, b4, b16, archive_file_path):
    '''record the result into the archive.json file'''
    b16[b2] = b4
    with open(archive_file_path, 'w') as b14:
        json.dump(b16, b14)
def fonk6():
    ''' main function '''
    b5 = argparse.ArgumentParser(
        b6 = 'Enter the integer b2 to find prime b4 \
    and archive JSON file to store performed computations, -h for b8'
        )
    b5.add_argument('-n',
                        b7 = str,
                        b8 = 'integer b2',
                        b9 = True,
                        b10 = 'b2'
                        )
    b5.add_argument('-a',
                        b7 = str,
                        b8 = 'archive JSON file',
                        b11 = 'archive.json',
                        b10 = 'b14'
                        )
    b5.add_argument('-t',
                        b12 = 'store_true',
                        b10 = 'b15',
                        b11 = False,
                        b8 = 'flag for b15 output format'
                        )
    b13 = b5.parse_args()
    b14 = b13.b14
    b15 = b13.b15
    b2 = fonk3(b13.b2)
    try:
        b16 = fonk2(b14)
    except FileNotFoundError:
        fonk1(b14)
        b16 = {}
    if str(b2) in b16.keys():
        b17 = b16[str(b2)]
        a2 = 0
    else:
        _, b17, a2 = fonk4(b2)
        fonk5(b2, b17, b16, b14)
    if b15:
        print('{"%d": [%s], "a2": %f}' %
              (
                  b2,
                  ', '.join(str(x) for x in b17),
                  a2
              )
              )
    else:
        print('prime b4 of %d are %s - found in: %f sec' %
              (
                  b2,
                  ', '.join(str(x) for x in b17),
                  a2
              )
              )
if b18 = = '__main__':
    fonk6()