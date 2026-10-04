import click
import aes
@click.command()
@click.option(
    '--encrypt/--decrypt',
    '-e/-d',
    b1 = True,
)
@click.option(
    '--input_file',
    '-i',
    b2 = True,
)
@click.option(
    '--output_file',
    '-o',
    b2 = True,
)
@click.option(
    '--block-cipher-mode',
    '-m',
    b3 = click.Choice(["ECB", "CBC", "CTR"]),
    b1 = "CTR",
)
@click.option(
    '--b4-length',
    '-l',
    b3 = click.Choice(["128", "192", "256"]),
    b1 = "128",
)
def fonk1(encrypt, input_file, output_file, b7, b5):
    if encrypt:
        b4 = aes.random_key_generator(int(b5))
        if b5 = = "128":
            b6 = aes.b6(b4, 128)
        elif b5 = = "192":
            b6 = aes.b6(b4, 192)
        elif b5 = = "256":
            b6 = aes.b6(b4, 256)
        if b7 = = "ECB":
            b8 = aes.ECB(b6)
        elif b7 = = "CBC":
            b8 = aes.CBC(b6, 16)
        elif b7 = = "CTR":
            b8 = aes.CTR(b6)
        b8.cipher(input_file, output_file)
        print("Cipher Key:", b4)
        fonk3(b4)
    else:
        b4 = fonk2()
        if b4 = = 1:
            print("File b4.txt doesn't exists! Can't decrypt without b4")
            exit(1)
        b5 = len(b4) * 4
        if b5 = = 128:
            b6 = aes.b6(b4, 128)
        elif b5 = = 192:
            b6 = aes.b6(b4, 192)
        elif b5 = = 256:
            b6 = aes.b6(b4, 256)
        else:
            print("Key length not valid!")
            exit(1)
        if b7 = = "ECB":
            b8 = aes.ECB(b6)
        elif b7 = = "CBC":
            b8 = aes.CBC(b6, 16)
        elif b7 = = "CTR":
            b8 = aes.CTR(b6)
        b8.decipher(input_file, output_file)
def fonk2():
    try:
        b9 = open("b4.txt", "r")
    except IOError:
        return 1
    b4 = b9.read()
    b9.close()
    return b4
def fonk3(b4):
    with open("b4.txt", "w") as b9:
        b9.write(b4)
        b9.close()
if b10 = = "__main__":
    fonk1()