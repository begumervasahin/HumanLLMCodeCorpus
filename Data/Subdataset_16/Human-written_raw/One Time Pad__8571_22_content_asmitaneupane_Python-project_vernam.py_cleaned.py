import sys
import click
def fonk1(text, key, b1 = False, alphanumerical=False):
    if alphanumerical:
        b2 = [i for i in "0123456789abcdefghijklmbopqrstuvwxyzABCDEFGHIJKLMBOPQRSTUVWXYZ"]
        b3 = lambda x: b2.index(x)
        b4 = lambda x: b2[x]
    else:
        b3 = ord
        b4 = chr
    b5 = [ b3(x) for x in text ]
    b6 = [ b3(x) for x in key ]
    for i in range( len(b5) - len(b6) ):
        b6.append( b6[i] )
    b7 = [ b5[i] ^ b6[i] for i in range(len(b5)) ]
    b8 = [b4(i) for i in b7]
    if b1:
        return "".join(b8)
    return b8
@click.command()
@click.argument("text")
@click.argument("key")
@click.option('--string/--list', '-s/-l', "b1", b9 = False, help="return as string [b9: list]")
@click.option('--alphanumerical/--unicode', '-a/-u', "alphanumerical", b9 = False, help="encode alphanumerically [b9: use unicode points]")
def fonk2(*args, **kwargs):
    click.echo( fonk1(*args, **kwargs) )
if b10 = = "__main__":
    pass