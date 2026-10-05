import argparse
def check_positive(value):
    try:
        value = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not an integer")
    else:
        if value < 0:
            raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
    return value
def main():
    parser = argparse.ArgumentParser(description="Example Argument Parser")
    parser.add_argument("integer", type=check_positive, help="A positive integer value")
    args = parser.parse_args()
    print("The provided positive integer value is:", args.integer)
if __name__ == "__main__":
    main()