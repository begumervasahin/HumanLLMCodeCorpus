from argparse import ArgumentParser, RawDescriptionHelpFormatter
def print_pyramid(rows):
    if not isinstance(rows, int) or rows <= 0:
        print('Please enter a number greater than 0')
        return
    for row_number in range(1, rows + 1):
        dashes_count = rows - row_number
        stars_count = 2 * row_number - 1
        row_content = "-" * dashes_count + "=" * stars_count + "-" * dashes_count
        print(row_content)
if __name__ == "__main__":
    parser = ArgumentParser(
        description="Print a pyramid to the terminal",
        formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", default=10, type=int, help="Number of rows")
    args = parser.parse_args()
    print_pyramid(args.rows)