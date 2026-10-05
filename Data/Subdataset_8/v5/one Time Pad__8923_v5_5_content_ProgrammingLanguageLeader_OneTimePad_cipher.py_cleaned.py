import argparse
def encrypt_text(plain_text: bytes, key: bytes) -> bytes:
    encrypted_text = b''
    for plain_char, key_char in zip(plain_text, key):
        encrypted_char = plain_char ^ key_char
        encrypted_text += bytes([encrypted_char])
    return encrypted_text
def create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='One-time pad encoder/decoder'
    )
    parser.add_argument(
        'key',
        type=str,
        help='Encryption key file path'
    )
    parser.add_argument(
        'source',
        type=str,
        help='Source file path'
    )
    parser.add_argument(
        'output',
        type=str,
        help='Output file path'
    )
    return parser
def main():
    parser = create_argument_parser()
    args = parser.parse_args()
    source_file_path = args.source
    output_file_path = args.output
    key_file_path = args.key
    block_size = 8192
    with open(key_file_path, 'rb') as key_file, \
            open(source_file_path, 'rb') as source_file,\
            open(output_file_path, 'wb') as output_file:
        while True:
            source_block = source_file.read(block_size)
            if not source_block:
                break
            key_block = key_file.read(len(source_block))
            output_block = encrypt_text(source_block, key_block)
            output_file.write(output_block)
    print('Encryption/decryption completed successfully.')
if __name__ == '__main__':
    main()