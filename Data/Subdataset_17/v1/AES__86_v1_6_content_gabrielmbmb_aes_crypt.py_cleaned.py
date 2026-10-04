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
    '--input-file',
    '-i',
    required=True,
    type=click.Path(exists=True),
    help="Path to the input file."
)
@click.option(
    '--output-file',
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
        AES = aes.AES(key, int(key_length))
        if block_cipher_mode == "ECB":
            bcm = aes.ECB(AES)
        elif block_cipher_mode == "CBC":
            bcm = aes.CBC(AES, 16)
        elif block_cipher_mode == "CTR":
            bcm = aes.CTR(AES)
        bcm.cipher(input_file, output_file)
        print("Cipher Key:", key)
        write_key(key)
    else:
        key = read_key()
        if key == 1:
            print("File key.txt doesn't exist! Can't decrypt without key.")
            exit(1)
        key_length = len(key) * 8
        AES = aes.AES(key, key_length)
        if block_cipher_mode == "ECB":
            bcm = aes.ECB(AES)
        elif block_cipher_mode == "CBC":
            bcm = aes.CBC(AES, 16)
        elif block_cipher_mode == "CTR":
            bcm = aes.CTR(AES)
        bcm.decipher(input_file, output_file)
def read_key():
    try:
        with open("key.txt", "r") as f:
            key = f.read()
        return key
    except IOError:
        return 1
def write_key(key):
    with open("key.txt", "w") as f:
        f.write(key)
if __name__ == "__main__":
    main()