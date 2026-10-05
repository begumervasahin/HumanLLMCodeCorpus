import argparse
def check_positive_integer(value):
    try:
        int_value = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid integer: {value}")
    else:
        if int_value < 0:
            raise argparse.ArgumentTypeError(f"Negative integer not allowed: {int_value}")
    return int_value
def parse_arguments():
    parser = argparse.ArgumentParser(description="Example Argument Parser")
    parser.add_argument("integer", type=check_positive_integer, help="A positive integer value")
    return parser.parse_args()
def main():
    args = parse_arguments()
    print("The provided positive integer value is:", args.integer)
if __name__ == "__main__":
    main()