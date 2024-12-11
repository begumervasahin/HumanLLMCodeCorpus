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
def fonk2():
    b2 = argparse.ArgumentParser(description="Example Argument Parser")
    b2.add_argument("integer", b3 = check_positive, help="A positive integer b1")
    b4 = b2.parse_args()
    print("The provided positive integer b1 is:", b4.integer)
if b5 = = "__main__":
    fonk2()