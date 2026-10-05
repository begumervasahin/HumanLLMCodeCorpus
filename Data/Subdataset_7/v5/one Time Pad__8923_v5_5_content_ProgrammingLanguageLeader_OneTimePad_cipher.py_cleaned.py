import argparse
def fonk1(plain_text: bytes, key: bytes) -> bytes:
    b1 = b''
    for plain_char, key_char in zip(plain_text, key):
        b2 = plain_char ^ key_char
        b1 += bytes([b2])
    return b1
def fonk2() -> argparse.ArgumentParser:
    b3 = argparse.ArgumentParser(
        b4 = 'One-time pad encoder/decoder'
    )
    b3.add_argument(
        'key',
        b5 = str,
        b6 = 'Encryption key file path'
    )
    b3.add_argument(
        'source',
        b5 = str,
        b6 = 'Source file path'
    )
    b3.add_argument(
        'output',
        b5 = str,
        b6 = 'Output file path'
    )
    return b3
def fonk3():
    b3 = fonk2()
    b7 = b3.parse_args()
    b8 = b7.source
    b9 = b7.output
    b10 = b7.key
    a1 = 8192
    with open(b10, 'rb') as key_file, \
            open(b8, 'rb') as source_file,\
            open(b9, 'wb') as output_file:
        while True:
            b11 = source_file.read(a1)
            if not b11:
                break
            b12 = key_file.read(len(b11))
            b13 = fonk1(b11, b12)
            output_file.write(b13)
    print('Encryption/decryption completed successfully.')
if b14 = = '__main__':
    fonk3()