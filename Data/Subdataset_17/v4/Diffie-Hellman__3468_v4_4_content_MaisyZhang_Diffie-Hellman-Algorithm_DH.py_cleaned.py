from argparse import ArgumentParser
def calc_key(private_key, base, modulus):
    return pow(base, private_key, modulus)
def parse_arguments():
    parser = ArgumentParser(description="Calculate shared secrets using modular arithmetic.")
    parser.add_argument("-A", "--A_private_key", type=int, required=True, help="Private key A")
    parser.add_argument("-B", "--B_private_key", type=int, required=True, help="Private key B")
    parser.add_argument("-g", "--base", type=int, required=True, help="Base (generator) for key calculation")
    parser.add_argument("-p", "--prime", type=int, required=True, help="Prime modulus for key calculation")
    return parser.parse_args()
def main():
    args = parse_arguments()
    A_private_key = args.A_private_key
    B_private_key = args.B_private_key
    base = args.base
    prime = args.prime
    A_public_key = calc_key(A_private_key, base, prime)
    B_public_key = calc_key(B_private_key, base, prime)
    A_shared_key = calc_key(A_private_key, B_public_key, prime)
    B_shared_key = calc_key(B_private_key, A_public_key, prime)
    print(f"Shared secret: {A_shared_key}")
if __name__ == "__main__":
    main()