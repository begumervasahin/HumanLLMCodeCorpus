import argparse
def check_positive(value):
    try:
        value = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("%s is not an int value" % value)
    else:
        if value < 0:
            raise argparse.ArgumentTypeError("%s is not a positive int value" % value)
    return value
def main():
    parser = argparse.ArgumentParser(description="Example Argument Parser")
    parser.add_argument("integer", type=check_positive, help="A positive integer value")
    args = parser.parse_args()
    print("The provided positive integer value is:", args.integer)
if __name__ == "__main__":
    main()