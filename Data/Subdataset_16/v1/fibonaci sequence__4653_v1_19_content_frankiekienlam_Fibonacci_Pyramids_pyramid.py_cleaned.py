
from argparse import ArgumentParser, RawDescriptionHelpFormatter
def fonk1(rows):
    if not isinstance(rows, int) or rows <= 0:
        print('Please enter a number greater than 0')
        return
    for i in range(1, rows + 1):
        b1 = rows - i
        b2 = 2 * i - 1
        print('-' * b1 + '=' * b2 + '-' * b1)
if b3 = = "__main__":
    b4 = ArgumentParser(
        b5 = __doc__, formatter_class=RawDescriptionHelpFormatter
    )
    b4.add_argument("-r", "--rows", b6 = 10, type=int, help="Number of rows")
    b7 = b4.parse_args()
    fonk1(b7.rows)