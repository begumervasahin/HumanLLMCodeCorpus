import sys
import click
def vernam_cipher(text, key, return_as_string=False, use_alphanumerical=False):
    if use_alphanumerical:
        alphanumerics = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        to_num = lambda x: alphanumerics.index(x)
        to_char = lambda x: alphanumerics[x]
    else:
        to_num = ord
        to_char = chr
    bintext = [to_num(char) for char in text]
    binkey = [to_num(char) for char in key]
    repeated_key = (binkey * ((len(bintext)
    vernam_result = [bintext[i] ^ repeated_key[i] for i in range(len(bintext))]
    result = [to_char(i) for i in vernam_result]
    if return_as_string:
        return "".join(result)
    return result
@click.command()
@click.argument("text")
@click.argument("key")
@click.option('--string/--list', '-s/-l', "return_as_string", default=False, help="Return as string [default: list]")
@click.option('--alphanumerical/--unicode', '-a/-u', "use_alphanumerical", default=False, help="Encode alphanumerically [default: use Unicode points]")
def cli(text, key, return_as_string, use_alphanumerical):
    result = vernam_cipher(text, key, return_as_string, use_alphanumerical)
    click.echo(result)
if __name__ == "__main__":
    cli()