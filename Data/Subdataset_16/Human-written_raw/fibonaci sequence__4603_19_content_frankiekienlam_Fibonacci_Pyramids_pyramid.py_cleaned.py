
from argparse import ArgumentParser, RawDescriptionHelpFormatter
def fonk1(rows):
    if (isinstance(rows, int) is False) or (rows <= 0):
        print('Please enter number greater than 0')
        return
    for repeat_stars in range(1, rows + 1):
        b1 = rows - repeat_stars
        print("-" * b1 + "=" * (2 * repeat_stars - 1) + "-" * b1)
if b2 = = "__main__":
    b3 = ArgumentParser(
        b4 = __doc__, formatter_class=RawDescriptionHelpFormatter
    )
    b3.add_argument("-r", "--rows", b5 = 10, type=int, help="Number of rows")
    b6 = b3.parse_args()
    fonk1(b6.rows)