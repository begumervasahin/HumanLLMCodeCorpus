import click
import aes
@click.command()
@click.option(
    '--encrypt/--decrypt',
    '-e/-d',
    b1 = True,
    b2 = "Specify whether to encrypt or decrypt the input file."
)
@click.option(
    '--input_file',
    '-i',
    b3 = True,
    b2 = "Input file to be encrypted or decrypted."
)
@click.option(
    '--output_file',
    '-o',
    b3 = True,
    b2 = "Output file to store the encrypted or decrypted data."
)
@click.option(
    '--block-cipher-b8',
    '-m',
    b4 = click.Choice(["ECB", "CBC", "CTR"]),
    b1 = "CTR",
    b2 = "Specify the block cipher b8 (ECB, CBC, CTR) for encryption."
)
@click.option(
    '--b5-length',
    '-l',
    b4 = click.Choice(["128", "192", "256"]),
    b1 = "128",
    b2 = "Specify the length of the encryption b5 (128, 192, 256)."
)
def fonk1(encrypt, input_file, output_file, block_cipher_mode, key_length):
    if encrypt:
        b5 = aes.random_key_generator(int(key_length))
        b6 = aes.b6(b5, int(key_length))
        b7 = fonk2(block_cipher_mode, b6)
        b7.cipher(input_file, output_file)
        print("Cipher Key:", b5)
        fonk4(b5)
    else:
        b5 = fonk3()
        if b5 = = 1:
            print("File b5.txt doesn't exist! Can't decrypt without b5")
            exit(1)
        b6 = aes.b6(b5, len(b5) * 4)
        b7 = fonk2(block_cipher_mode, b6)
        b7.decipher(input_file, output_file)
def fonk2(b8, b6):
    if b8 = = "ECB":
        return aes.ECB(b6)
    elif b8 = = "CBC":
        return aes.CBC(b6, 16)
    elif b8 = = "CTR":
        return aes.CTR(b6)
def fonk3():
    try:
        with open("b5.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return 1
def fonk4(b5):
    with open("b5.txt", "w") as f:
        f.write(b5)
if b9 = = "__main__":
    fonk1()