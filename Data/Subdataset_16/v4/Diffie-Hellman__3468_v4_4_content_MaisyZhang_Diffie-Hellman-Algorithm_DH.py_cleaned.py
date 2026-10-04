from argparse import ArgumentParser
def fonk1(private_key, b6, modulus):
    return pow(b6, private_key, modulus)
def fonk2():
    b1 = ArgumentParser(description="Calculate shared secrets using modular arithmetic.")
    b1.add_argument("-A", "--b4", b2 = int, required=True, help="Private key A")
    b1.add_argument("-B", "--b5", b2 = int, required=True, help="Private key B")
    b1.add_argument("-g", "--b6", b2 = int, required=True, help="Base (generator) for key calculation")
    b1.add_argument("-p", "--b7", b2 = int, required=True, help="Prime modulus for key calculation")
    return b1.parse_args()
def fonk3():
    b3 = fonk2()
    b4 = b3.b4
    b5 = b3.b5
    b6 = b3.b6
    b7 = b3.b7
    b8 = fonk1(b4, b6, b7)
    b9 = fonk1(b5, b6, b7)
    b10 = fonk1(b4, b9, b7)
    b11 = fonk1(b5, b8, b7)
    print(f"Shared secret: {b10}")
if b12 = = "__main__":
    fonk3()