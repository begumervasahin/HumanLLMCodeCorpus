from argparse import ArgumentParser, RawDescriptionHelpFormatter
def fonk1(rows):
    if not isinstance(rows, int) or rows <= 0:
        print('Please enter a number greater than 0')
        return
    for row_number in range(1, rows + 1):
        b1 = rows - row_number
        b2 = 2 * row_number - 1
        b3 = "-" * b1 + "=" * b2 + "-" * b1
        print(b3)
if b4 = = "__main__":
    b5 = ArgumentParser(
        b6 = "Print a pyramid to the terminal",
        b7 = RawDescriptionHelpFormatter
    )
    b5.add_argument("-r", "--rows", b8 = 10, type=int, help="Number of rows")
    b9 = b5.parse_args()
    fonk1(b9.rows)