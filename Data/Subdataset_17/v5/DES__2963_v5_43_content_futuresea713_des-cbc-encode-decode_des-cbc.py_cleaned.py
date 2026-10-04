import pyDes
import base64
def encrypt_data(data, key, iv):
    cipher = pyDes.des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)
    encrypted_data = cipher.encrypt(data)
    encoded_encrypted_data = base64.b64encode(encrypted_data)
    return encoded_encrypted_data
def decrypt_data(encoded_encrypted_data, key, iv):
    decoded_encrypted_data = base64.b64decode(encoded_encrypted_data)
    cipher = pyDes.des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)
    decrypted_data = cipher.decrypt(decoded_encrypted_data)
    return decrypted_data
def main():
    data = "abc123"
    key = 'g9G16nTs'
    iv = 'g9G16nTs'
    encoded_encrypted_data = encrypt_data(data, key, iv)
    decrypted_data = decrypt_data(encoded_encrypted_data, key, iv)
    print("Encrypted (base64 encoded):", encoded_encrypted_data.decode())
    print("Decrypted Data:", decrypted_data.decode())
if __name__ == "__main__":
    main()