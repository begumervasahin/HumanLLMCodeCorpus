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