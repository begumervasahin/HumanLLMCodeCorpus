import sys
import click
def vernam(text, key, return_str=False, alphanumerical=False):
    if alphanumerical:
        alphanumerics = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        to_num = lambda x: alphanumerics.index(x)
        to_char = lambda x: alphanumerics[x]
    else:
        to_num = ord
        to_char = chr
    bintext = [to_num(char) for char in text]
    binkey = [to_num(char) for char in key]
    binkey = (binkey * (len(bintext)
    vernamed = [bintext[i] ^ binkey[i] for i in range(len(bintext))]
    result = [to_char(num) for num in vernamed]
    return "".join(result) if return_str else result
@click.command()
@click.argument("text")
@click.argument("key")
@click.option('--string/--list', '-s/-l', "return_str", default=False, help="Return as string [default: list]")
@click.option('--alphanumerical/--unicode', '-a/-u', "alphanumerical", default=False, help="Encode alphanumerically [default: use Unicode points]")
def cli(text, key, return_str, alphanumerical):
    result = vernam(text, key, return_str, alphanumerical)
    click.echo(result)
if __name__ == "__main__":
    cli()