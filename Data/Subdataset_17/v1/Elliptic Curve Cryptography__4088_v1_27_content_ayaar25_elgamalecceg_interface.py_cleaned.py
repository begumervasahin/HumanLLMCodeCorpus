from ecceg import EllipticCurveCryptoElGamal
from elgamal import ElGamal
def print_blue(text):
    print('\033[1;34m' + text + '\033[1;m')
def print_green(text):
    print('\033[1;32m' + text + '\033[1;m')
def print_magenta(text):
    print('\033[1;35m' + text + '\033[1;m')
def display_file_content(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    for c in file_data:
        print(hex(c), end=' ')
    print()
def main():
    print("\n")
    print_green("- Choose algorithm -")
    print_magenta("[1] ElGamal \t [2] ECC")
    in_algo = input("Enter Choice: ")
    if in_algo == '1':
        algo = ElGamal()
    elif in_algo == '2':
        print("\n================")
        print_green("- Enter constants -")
        print_magenta("Formula: y^2 = ( x^3 + Ax + B ) mod P")
        print_magenta("K is used in encoding/decoding process")
        in_a = int(input("Enter A: "))
        in_b = int(input("Enter B: "))
        in_p = int(input("Enter P: "))
        in_k = int(input("Enter K: "))
        algo = EllipticCurveCryptoElGamal(in_a, in_b, in_p, in_k)
    else:
        print("Invalid choice!")
        return
    print("\n================")
    print_green("- Choose operation -")
    print_magenta("[1] Encrypt \t [2] Decrypt")
    in_op = input("Enter Choice: ")
    print("\n================")
    print_green("- Do you already have the key? -")
    print_magenta("[1] Yes \t [2] No, create new key")
    in_new_key = input("Enter Choice: ")
    if in_new_key == '2':
        print("\n================")
        print_green("- Enter new key seed -")
        in_key_seed = input("Enter seed: ")
        algo.key_gen(in_key_seed)
        in_key_pub = "key.pub"
        in_key_pri = "key.pri"
    elif in_new_key == '1':
        print("\n================")
        print_green("- Enter public key location -")
        in_key_pub = input("Enter file location: ")
        print_green("\nPublic Key File:")
        display_file_content(in_key_pub)
        print("\n================")
        print_green("- Enter private key location -")
        in_key_pri = input("Enter file location: ")
        print_green("\nPrivate Key File:")
        display_file_content(in_key_pri)
    else:
        print("Invalid choice!")
        return
    print("\n================")
    print_green("- Enter target file -")
    in_file = input("Enter file: ")
    print("\n================")
    print_green("- Input File: -")
    with open(in_file, 'r') as file:
        file_data = file.read()
    print(file_data)
    if in_op == '1':
        if in_algo == '1':
            algo.encrypt(in_file, in_key_pub, in_key_pri)
            out_file = 'cipher.txt'
        elif in_algo == '2':
            algo.encrypt(in_file, in_key_pub, in_key_pri, in_k)
            out_file = 'cipher_ecceg.txt'
    elif in_op == '2':
        algo.decrypt(in_file, in_key_pub, in_key_pri)
        out_file = 'out.txt'
    else:
        print("Invalid choice!")
        return
    print("\n================")
    print_green("- Output File: -")
    display_file_content(out_file)
if __name__ == '__main__':
    main()