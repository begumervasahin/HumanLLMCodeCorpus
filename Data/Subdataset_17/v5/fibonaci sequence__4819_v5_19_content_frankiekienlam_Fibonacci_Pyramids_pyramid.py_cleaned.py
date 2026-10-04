
from argparse import ArgumentParser, RawDescriptionHelpFormatter
def print_pyramid(rows):
    if not isinstance(rows, int) or rows <= 0:
        print('Please enter a number greater than 0')
        return
    for i in range(1, rows + 1):
        dashes = rows - i
        equals = 2 * i - 1
        line = '-' * dashes + '=' * equals + '-' * dashes
        print(line)
def main():
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "-r", "--rows",
        default=10,
        type=int,
        help="Number of rows for the pyramid"
    )
    args = parser.parse_args()
    print_pyramid(args.rows)
if __name__ == "__main__":
    main()