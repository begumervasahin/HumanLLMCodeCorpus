import argparse
def check_positive_integer(value):
    try:
        value = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid integer value: {value}")
    else:
        if value < 0:
            raise argparse.ArgumentTypeError(f"Negative integer value not allowed: {value}")
    return value