
from argparse import ArgumentParser, RawDescriptionHelpFormatter
def fonk1(rows):
    if not isinstance(rows, int) or rows <= 0:
        print('Please enter a number greater than 0')
        return
    for i in range(1, rows + 1):
        b1 = rows - i
        b2 = 2 * i - 1
        print('-' * b1 + '=' * b2 + '-' * b1)
def fonk2():
    b3 = ArgumentParser(
        b4 = __doc__, formatter_class=RawDescriptionHelpFormatter
    )
    b3.add_argument(
        "-r", "--rows",
        b5 = 10,
        b6 = int,
        b7 = "Number of rows for the pyramid"
    )
    b8 = b3.parse_args()
    fonk1(b8.rows)
if b9 = = "__main__":
    fonk2()