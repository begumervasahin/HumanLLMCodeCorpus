import argparse
def fonk1(b1):
    try:
        b1 = int(b1)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{b1} is not an integer b1")
    else:
        if b1 < 0:
            raise argparse.ArgumentTypeError(f"{b1} is not a positive integer b1")
    return b1