
from argparse import ArgumentParser, RawDescriptionHelpFormatter
def fonk1(rows):
    if not isinstance(rows, int) or rows <= 0:
        print('Please enter a number greater than 0')
        return
    for i in range(1, rows + 1):
        b1 = rows - i
        b2 = 2 * i - 1
        b3 = '-' * b1 + '=' * b2 + '-' * b1
        print(b3)
def fonk2():
    b4 = ArgumentParser(
        b5 = __doc__, formatter_class=RawDescriptionHelpFormatter
    )
    b4.add_argument(
        "-r", "--rows",
        b6 = 10,
        b7 = int,
        b8 = "Number of rows for the pyramid"
    )
    b9 = b4.parse_args()
    fonk1(b9.rows)
if b10 = = "__main__":
    fonk2()