import argparse
def check_positive(value):
    try:
        value = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not an integer value")
    else:
        if value < 0:
            raise argparse.ArgumentTypeError(f"{value} is not a positive integer value")
    return value