import click
import aes
@click.command()
@click.option(
    '--encrypt/--decrypt',
    '-e/-d',
    default=True,
    help="Specify whether to encrypt or decrypt the input file."
)
@click.option(
    '--input_file',
    '-i',
    required=True,
    help="Input file to be encrypted or decrypted."
)
@click.option(
    '--output_file',
    '-o',
    required=True,
    help="Output file to store the encrypted or decrypted data."
)
@click.option(
    '--block-cipher-mode',
    '-m',
    type=click.Choice(["ECB", "CBC", "CTR"]),
    default="CTR",
    help="Specify the block cipher mode (ECB, CBC, CTR) for encryption."
)
@click.option(
    '--key-length',
    '-l',
    type=click.Choice(["128", "192", "256"]),
    default="128",
    help="Specify the length of the encryption key (128, 192, 256)."
)
def main(encrypt, input_file, output_file, block_cipher_mode, key_length):
    if encrypt:
        key = aes.random_key_generator(int(key_length))
        AES = aes.AES(key, int(key_length))
        bcm = get_block_cipher_mode(block_cipher_mode, AES)
        bcm.cipher(input_file, output_file)
        print("Cipher Key:", key)
        write_key(key)
    else:
        key = read_key()
        if key == 1:
            print("File key.txt doesn't exist! Can't decrypt without key")
            exit(1)
        AES = aes.AES(key, len(key) * 4)
        bcm = get_block_cipher_mode(block_cipher_mode, AES)
        bcm.decipher(input_file, output_file)
def get_block_cipher_mode(mode, AES):
    if mode == "ECB":
        return aes.ECB(AES)
    elif mode == "CBC":
        return aes.CBC(AES, 16)
    elif mode == "CTR":
        return aes.CTR(AES)
def read_key():
    try:
        with open("key.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return 1
def write_key(key):
    with open("key.txt", "w") as f:
        f.write(key)
if __name__ == "__main__":
    main()