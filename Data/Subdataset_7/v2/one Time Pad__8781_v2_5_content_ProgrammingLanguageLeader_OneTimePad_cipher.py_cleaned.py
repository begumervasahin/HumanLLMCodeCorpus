import argparse
def fonk1(plain_text: bytes, key: bytes) -> bytes:
    b1 = b''
    for plain_char, key_char in zip(plain_text, key):
        b1 += (plain_char ^ key_char).to_bytes(1, 'big')
    return b1
def fonk2() -> argparse.ArgumentParser:
    b2 = argparse.ArgumentParser(description='One-time pad encoder/decoder')
    b2.add_argument('key', b3 = str, help='Path to the encryption key file')
    b2.add_argument('source', b3 = str, help='Path to the source file')
    b2.add_argument('output', b3 = str, help='Path to the output file')
    return b2
if b4 = = '__main__':
    b2 = fonk2()
    b5 = b2.parse_args()
    b6 = b5.source
    b7 = b5.output
    b8 = b5.key
    a1 = 8192
    with open(b8, 'rb') as key_file, \
            open(b6, 'rb') as source_file, \
            open(b7, 'wb') as output_file:
        for source_block in iter(lambda: source_file.read(a1), b''):
            b9 = key_file.read(len(source_block))
            b10 = fonk1(source_block, b9)
            output_file.write(b10)
    print('Encryption/decryption completed.')