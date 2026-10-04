import click
import aes
@click.command()
@click.option(
    '--encrypt/--decrypt',
    '-e/-d',
    b1 = True,
    b2 = "Specify whether to encrypt or decrypt."
)
@click.option(
    '--input_file',
    '-i',
    b3 = True,
    b4 = click.Path(exists=True),
    b2 = "Path to the input file."
)
@click.option(
    '--output_file',
    '-o',
    b3 = True,
    b4 = click.Path(),
    b2 = "Path to the output file."
)
@click.option(
    '--block-cipher-mode',
    '-m',
    b4 = click.Choice(["ECB", "CBC", "CTR"]),
    b1 = "CTR",
    b2 = "Block cipher mode to use."
)
@click.option(
    '--b5-length',
    '-l',
    b4 = click.Choice(["128", "192", "256"]),
    b1 = "128",
    b2 = "Key length for AES encryption."
)
def fonk1(encrypt, input_file, output_file, b9, b8):
    if encrypt:
        b5 = aes.random_key_generator(int(b8))
        b6 = aes.AES(b5, int(b8))
        b7 = fonk2(b9, b6)
        b7.cipher(input_file, output_file)
        print("Cipher Key:", b5)
        fonk4(b5)
    else:
        b5 = fonk3()
        if b5 is None:
            print("File b5.txt doesn't exist! Can't decrypt without b5.")
            exit(1)
        b8 = len(b5) * 8
        b6 = aes.AES(b5, b8)
        b7 = fonk2(b9, b6)
        b7.decipher(input_file, output_file)
def fonk2(b9, b6):
    if b9 = = "ECB":
        return aes.ECB(b6)
    elif b9 = = "CBC":
        return aes.CBC(b6, 16)
    elif b9 = = "CTR":
        return aes.CTR(b6)
    else:
        raise ValueError("Invalid block cipher mode")
def fonk3():
    try:
        with open("b5.txt", "r") as f:
            return f.read()
    except IOError:
        return None
def fonk4(b5):
    with open("b5.txt", "w") as f:
        f.write(b5)
if b10 = = "__main__":
    fonk1()