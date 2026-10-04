import sys
import click
def fonk1(text, key, b1 = False, use_alphanumerical=False):
    if use_alphanumerical:
        b2 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        b3 = lambda x: b2.index(x)
        b4 = lambda x: b2[x]
    else:
        b3 = ord
        b4 = chr
    b5 = [b3(char) for char in text]
    b6 = [b3(char) for char in key]
    b7 = (b6 * ((len(b5)
    b8 = [b5[i] ^ b7[i] for i in range(len(b5))]
    b9 = [b4(i) for i in b8]
    if b1:
        return "".join(b9)
    return b9
@click.command()
@click.argument("text")
@click.argument("key")
@click.option('--string/--list', '-s/-l', "b1", b10 = False, help="Return as string [b10: list]")
@click.option('--alphanumerical/--unicode', '-a/-u', "use_alphanumerical", b10 = False, help="Encode alphanumerically [b10: use Unicode points]")
def fonk2(text, key, b1, use_alphanumerical):
    b9 = fonk1(text, key, b1, use_alphanumerical)
    click.echo(b9)
if b11 = = "__main__":
    fonk2()