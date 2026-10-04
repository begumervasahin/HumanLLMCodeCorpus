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
    '--input-file',
    '-i',
    b3 = True,
    b4 = click.Path(exists=True),
    b2 = "Path to the input file."
)
@click.option(
    '--output-file',
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
    b2 = "Key length for b6 encryption."
)
def fonk1(encrypt, input_file, output_file, b7, b9):
    if encrypt:
        b5 = aes.random_key_generator(int(b9))
        b6 = aes.b6(b5, int(b9))
        if b7 = = "ECB":
            b8 = aes.ECB(b6)
        elif b7 = = "CBC":
            b8 = aes.CBC(b6, 16)
        elif b7 = = "CTR":
            b8 = aes.CTR(b6)
        b8.cipher(input_file, output_file)
        print("Cipher Key:", b5)
        fonk3(b5)
    else:
        b5 = fonk2()
        if b5 = = 1:
            print("File b5.txt doesn't exist! Can't decrypt without b5.")
            exit(1)
        b9 = len(b5) * 8
        b6 = aes.b6(b5, b9)
        if b7 = = "ECB":
            b8 = aes.ECB(b6)
        elif b7 = = "CBC":
            b8 = aes.CBC(b6, 16)
        elif b7 = = "CTR":
            b8 = aes.CTR(b6)
        b8.decipher(input_file, output_file)
def fonk2():
    try:
        with open("b5.txt", "r") as f:
            b5 = f.read()
        return b5
    except IOError:
        return 1
def fonk3(b5):
    with open("b5.txt", "w") as f:
        f.write(b5)
if b10 = = "__main__":
    fonk1()