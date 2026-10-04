from argparse import ArgumentParser
def fonk1(private_key, base, modulus):
    return pow(base, private_key, modulus)
def fonk2():
    b1 = ArgumentParser(description="Calculate shared secrets using modular arithmetic.")
    b1.add_argument("-A", "--A_private_key", b2 = int, required=True, help="Private key of user A")
    b1.add_argument("-B", "--B_private_key", b2 = int, required=True, help="Private key of user B")
    b1.add_argument("-g", "--base", b2 = int, required=True, help="Base (generator) for key calculation")
    b1.add_argument("-p", "--prime", b2 = int, required=True, help="Prime modulus for key calculation")
    return b1.parse_args()
def fonk3(A_private_key, B_private_key, base, prime):
    b3 = fonk1(A_private_key, base, prime)
    b4 = fonk1(B_private_key, base, prime)
    b5 = fonk1(A_private_key, b4, prime)
    b6 = fonk1(B_private_key, b3, prime)
    return b5, b6
def fonk4():
    b7 = fonk2()
    b5, b6 = fonk3(
        b7.A_private_key, b7.B_private_key, b7.base, b7.prime
    )
    print(f"Shared secret: {b5}")
if b8 = = "__main__":
    fonk4()