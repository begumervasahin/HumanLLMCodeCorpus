import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
def generate_key_from_password(password):
    password_bytes = password.encode()
    salt = b'salt_'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
    return key
def encrypt_file(key, input_file):
    output_file = f'encrypted_{input_file}'
    with open(input_file, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(output_file, 'wb') as file:
        file.write(encrypted_data)
def decrypt_file(key, input_file):
    output_file = f'decrypted_{input_file}'
    with open(input_file, 'rb') as file:
        data = file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(data)
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)
def convert_to_binary(input_file):
    output_file = f'binary_{input_file}'
    with open(input_file, 'r') as file:
        data = file.read()
    binary_data = ''.join([bin(ord(c))[2:].zfill(8) for c in data])
    with open(output_file, 'w') as file:
        file.write(binary_data)
def convert_from_binary(input_file):
    output_file = f'debinary_{input_file}'
    with open(input_file, 'r') as file:
        data = file.read()
    n = int(data, 2)
    decoded_data = n.to_bytes((n.bit_length() + 7)
    with open(output_file, 'w') as file:
        file.write(decoded_data)
def main():
    menu = (
        "\nChoose an option:"
        "\n1. Encrypt a file"
        "\n2. Decrypt a file"
        "\n3. Convert file content to binary"
        "\n4. Convert binary content to text"
        "\n>> "
    )
    option = input(menu)
    if option == '1':
        password = input("Enter password >> ")
        file_name = input("Enter file name in current directory >> ")
        key = generate_key_from_password(password)
        encrypt_file(key, file_name)
        print(f"File '{file_name}' encrypted successfully.")
    elif option == '2':
        password = input("Enter password >> ")
        file_name = input("Enter file name in current directory >> ")
        key = generate_key_from_password(password)
        decrypt_file(key, file_name)
        print(f"File '{file_name}' decrypted successfully.")
    elif option == '3':
        file_name = input("Enter file name in current directory >> ")
        convert_to_binary(file_name)
        print(f"File '{file_name}' converted to binary successfully.")
    elif option == '4':
        file_name = input("Enter file name in current directory >> ")
        convert_from_binary(file_name)
        print(f"Binary file '{file_name}' converted to text successfully.")
    else:
        print("Invalid option. Please try again.")
if __name__ == "__main__":
    main()