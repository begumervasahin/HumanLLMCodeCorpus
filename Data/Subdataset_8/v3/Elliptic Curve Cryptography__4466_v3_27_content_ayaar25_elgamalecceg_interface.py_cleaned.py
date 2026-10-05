from ecceg import EllipticCurveCryptoElGamal
from elgamal import ElGamal
def print_blue(text):
    text = '\033[1;34m' + text + '\033[1;m'
    print(text)
def print_green(text):
    text = '\033[1;32m' + text + '\033[1;m'
    print(text)
def print_magenta(text):
    text = '\033[1;35m' + text + '\033[1;m'
    print(text)
def choose_algorithm():
    print("\n")
    print_green("- Choose algorithm -")
    print_magenta("[1] ElGamal \t [2] ECC")
    return input("Enter Choice: ")
def enter_constants():
    print("\n================")
    print_green("- Enter constants -")
    print_magenta("Formula: y^2 = ( x^3 + Ax + B ) mod P")
    print_magenta("K is used in encoding/decoding process")
    in_a = input("Enter A: ")
    in_b = input("Enter B: ")
    in_p = input("Enter P: ")
    in_k = input("Enter K: ")
    return in_a, in_b, in_p, in_k
def choose_operation():
    print("\n================")
    print_green("- Choose operation -")
    print_magenta("[1] Encrypt \t [2] Decrypt")
    return input("Enter Choice: ")
def choose_key():
    print("\n================")
    print_green("- Do you already have the key? -")
    print_magenta("[1] Yes \t [2] No, create new key")
    return input("Enter Choice: ")
def enter_new_key_seed(algo):
    print("\n================")
    print_green("- Enter new key seed -")
    in_key_seed = input("Enter seed: ")
    algo.key_gen(in_key_seed)
def enter_key_locations():
    print("\n================")
    print_green("- Enter public key location -")
    in_key_pub = input("Enter file location: ")
    print_green("\nPublic Key File:")
    with open(in_key_pub, 'rb') as file:
        file_data = file.read()
    for c in file_data:
        print(hex(c), end=' ')
    print()
    print("\n================")
    print_green("- Enter private key location -")
    in_key_pri = input("Enter file location: ")
    print_green("\nPrivate Key File:")
    with open(in_key_pri, 'rb') as file:
        file_data = file.read()
    for c in file_data:
        print(hex(c), end=' ')
    print()
    return in_key_pub, in_key_pri
def enter_target_file():
    print("\n================")
    print_green("- Enter target file -")
    return input("Enter file: ")
def read_input_file(file_name):
    print("\n================")
    print_green("- Input File: -")
    with open(file_name, 'r') as file:
        file_data = file.read()
    print(file_data)
    return file_data
def process_operation(op, algo, in_file, in_key_pub, in_key_pri, in_k=None):
    if op == '1':
        if algo == '1':
            algo.encrypt(in_file, in_key_pub, in_key_pri)
            out_file = 'cipher.txt'
        elif algo == '2':
            algo.encrypt(in_file, in_key_pub, in_key_pri, in_k)
            out_file = 'cipher_ecceg.txt'
    elif op == '2':
        algo.decrypt(in_file, in_key_pub, in_key_pri)
        out_file = 'out.txt'
    return out_file
def print_output_file(out_file):
    print("\n================")
    print_green("- Output File: -")
    with open(out_file, 'rb') as file:
        file_data = file.read()
    for c in file_data:
        print(hex(c), end=' ')
    print()
if __name__ == '__main__':
    algo_choice = choose_algorithm()
    algo = None
    if algo_choice == '1':
        algo = ElGamal()
    elif algo_choice == '2':
        in_a, in_b, in_p, in_k = enter_constants()
        algo = EllipticCurveCryptoElGamal(in_a, in_b, in_p, in_k)
    operation = choose_operation()
    key_choice = choose_key()
    if key_choice == '2':
        enter_new_key_seed(algo)
    elif key_choice == '1':
        in_key_pub, in_key_pri = enter_key_locations()
    target_file = enter_target_file()
    file_data = read_input_file(target_file)
    if operation == '1':
        out_file = process_operation(operation, algo_choice, target_file, in_key_pub, in_key_pri)
    elif operation == '2':
        out_file = process_operation(operation, algo_choice, target_file, in_key_pub, in_key_pri, in_k)
    print_output_file(out_file)