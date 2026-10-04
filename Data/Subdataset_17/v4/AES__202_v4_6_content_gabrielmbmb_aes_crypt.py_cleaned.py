import click
import aes
@click.command()
@click.option(
    '--encrypt/--decrypt',
    '-e/-d',
    default=True,
    help="Specify whether to encrypt or decrypt."
)
@click.option(
    '--input_file',
    '-i',
    required=True,
    type=click.Path(exists=True),
    help="Path to the input file."
)
@click.option(
    '--output_file',
    '-o',
    required=True,
    type=click.Path(),
    help="Path to the output file."
)
@click.option(
    '--block-cipher-mode',
    '-m',
    type=click.Choice(["ECB", "CBC", "CTR"]),
    default="CTR",
    help="Block cipher mode to use."
)
@click.option(
    '--key-length',
    '-l',
    type=click.Choice(["128", "192", "256"]),
    default="128",
    help="Key length for AES encryption."
)
def main(encrypt, input_file, output_file, block_cipher_mode, key_length):
    if encrypt:
        key = aes.random_key_generator(int(key_length))
        aes_instance = aes.AES(key, int(key_length))
        block_cipher = get_block_cipher(block_cipher_mode, aes_instance)
        block_cipher.cipher(input_file, output_file)
        print("Cipher Key:", key)
        write_key(key)
    else:
        key = read_key()
        if key is None:
            print("File key.txt doesn't exist! Can't decrypt without key.")
            exit(1)
        key_length = len(key) * 8
        aes_instance = aes.AES(key, key_length)
        block_cipher = get_block_cipher(block_cipher_mode, aes_instance)
        block_cipher.decipher(input_file, output_file)
def get_block_cipher(block_cipher_mode, aes_instance):
    if block_cipher_mode == "ECB":
        return aes.ECB(aes_instance)
    elif block_cipher_mode == "CBC":
        return aes.CBC(aes_instance, 16)
    elif block_cipher_mode == "CTR":
        return aes.CTR(aes_instance)
    else:
        raise ValueError("Invalid block cipher mode")
def read_key():
    try:
        with open("key.txt", "r") as f:
            return f.read()
    except IOError:
        return None
def write_key(key):
    with open("key.txt", "w") as f:
        f.write(key)
if __name__ == "__main__":
    main()