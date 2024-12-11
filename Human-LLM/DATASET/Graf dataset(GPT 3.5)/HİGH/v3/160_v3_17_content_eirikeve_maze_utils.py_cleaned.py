import argparse
def fonk1(value):
    try:
        b1 = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid integer: {value}")
    else:
        if b1 < 0:
            raise argparse.ArgumentTypeError(f"Negative integer not allowed: {b1}")
    return b1
def fonk2():
    b2 = argparse.ArgumentParser(description="Example Argument Parser")
    b2.add_argument("integer", b3 = check_positive_integer, help="A positive integer value")
    return b2.parse_args()
def fonk3():
    b4 = fonk2()
    print("The provided positive integer value is:", b4.integer)
if b5 = = "__main__":
    fonk3()