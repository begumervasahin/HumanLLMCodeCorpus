from ecceg import EllipticCurveCryptoElGamal
from elgamal import ElGamal
def print_colored(text, color_code):
    print(f'\033[1;{color_code}m{text}\033[1;m')
def print_blue(text):
    print_colored(text, '34')
def print_green(text):
    print_colored(text, '32')
def print_magenta(text):
    print_colored(text, '35')
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
    algo_choice = input("Enter Choice: ")
    if algo_choice == '1':
        algo = ElGamal()
    elif algo_choice == '2':
        print("\n================")
        print_green("- Enter constants -")
        print_magenta("Formula: y^2 = ( x^3 + Ax + B ) mod P")
        print_magenta("K is used in encoding/decoding process")
        a = int(input("Enter A: "))
        b = int(input("Enter B: "))
        p = int(input("Enter P: "))
        k = int(input("Enter K: "))
        algo = EllipticCurveCryptoElGamal(a, b, p, k)
    else:
        print("Invalid choice!")
        return
    print("\n================")
    print_green("- Choose operation -")
    print_magenta("[1] Encrypt \t [2] Decrypt")
    operation_choice = input("Enter Choice: ")
    print("\n================")
    print_green("- Do you already have the key? -")
    print_magenta("[1] Yes \t [2] No, create new key")
    key_choice = input("Enter Choice: ")
    if key_choice == '2':
        print("\n================")
        print_green("- Enter new key seed -")
        key_seed = input("Enter seed: ")
        algo.key_gen(key_seed)
        public_key_path = "key.pub"
        private_key_path = "key.pri"
    elif key_choice == '1':
        print("\n================")
        print_green("- Enter public key location -")
        public_key_path = input("Enter file location: ")
        print_green("\nPublic Key File:")
        display_file_content(public_key_path)
        print("\n================")
        print_green("- Enter private key location -")
        private_key_path = input("Enter file location: ")
        print_green("\nPrivate Key File:")
        display_file_content(private_key_path)
    else:
        print("Invalid choice!")
        return
    print("\n================")
    print_green("- Enter target file -")
    target_file = input("Enter file: ")
    print("\n================")
    print_green("- Input File: -")
    with open(target_file, 'r') as file:
        file_data = file.read()
    print(file_data)
    if operation_choice == '1':
        if algo_choice == '1':
            algo.encrypt(target_file, public_key_path, private_key_path)
            output_file = 'cipher.txt'
        elif algo_choice == '2':
            algo.encrypt(target_file, public_key_path, private_key_path, k)
            output_file = 'cipher_ecceg.txt'
    elif operation_choice == '2':
        algo.decrypt(target_file, public_key_path, private_key_path)
        output_file = 'out.txt'
    else:
        print("Invalid choice!")
        return
    print("\n================")
    print_green("- Output File: -")
    display_file_content(output_file)
if __name__ == '__main__':
    main()