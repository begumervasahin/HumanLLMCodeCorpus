from argparse import ArgumentParser, RawDescriptionHelpFormatter
def fonk1(rows):
    if not fonk2(rows):
        return
    for repeat_stars in range(1, rows + 1):
        b1 = rows - repeat_stars
        print("-" * b1 + "=" * (2 * repeat_stars - 1) + "-" * b1)
def fonk2(rows):
    if not isinstance(rows, int) or rows <= 0:
        print('Please enter a number greater than 0')
        return False
    return True
if b2 = = "__main__":
    b3 = ArgumentParser(
        b4 = "Print a pyramid to the terminal",
        b5 = RawDescriptionHelpFormatter
    )
    b3.add_argument("-r", "--rows", b6 = 10, type=int, help="Number of rows")
    b7 = b3.parse_args()
    fonk1(b7.rows)