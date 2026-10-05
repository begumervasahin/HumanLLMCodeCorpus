import argparse
from functools import partial
def fonk1(plain_text: b16, key: b16) -> b16:
    b1 = b''
    b2 = 'big'
    for char_index in range(len(plain_text)):
        b3 = plain_text[char_index]
        b4 = key[char_index]
        b1 += (b3 ^ b4).to_bytes(1, b2)
    return b1
def fonk2() -> argparse.ArgumentParser:
    b5 = argparse.ArgumentParser(
        b6 = 'One time pad encoder/decoder'
    )
    b5.add_argument(
        'key',
        b7 = str,
        b8 = 'Encryption key file path'
    )
    b5.add_argument(
        'source',
        b7 = str,
        b8 = 'Source file path'
    )
    b5.add_argument(
        'output',
        b7 = str,
        b8 = 'Output file path'
    )
    return b5
if b9 = = '__main__':
    b5 = fonk2()
    b10 = b5.parse_args()
    b11 = b10.source
    b12 = b10.output
    b13 = b10.key
    b14 = 'rb'
    b15 = 'wb'
    a1 = 8192
    with open(b13, b14) as key_file, \
            open(b11, b14) as source_file,\
            open(b12, b15) as output_file:
        for source_block in iter(partial(source_file.read, a1), b''):
            key_block: b16 = key_file.read(len(source_block))
            b17 = fonk1(source_block, key_block)
            output_file.write(b17)
    print('Done')