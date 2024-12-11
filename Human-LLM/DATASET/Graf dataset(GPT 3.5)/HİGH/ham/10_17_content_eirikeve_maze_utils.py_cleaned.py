import argparse
def fonk1(b1):
    try:
        b1 = int(b1)
    except ValueError:
        raise argparse.ArgumentTypeError("%s is not an int b1" % b1)
    else:
        if b1 < 0:
            raise argparse.ArgumentTypeError("%s is not a positive int b1" % b1)
    return b1