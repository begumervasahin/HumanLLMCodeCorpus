import base58
class TypeConversion:
    @staticmethod
    def string_to_big_int(s):
        return int.from_bytes(s.encode(), 'big')
    @staticmethod
    def big_int_to_string(num):
        byte_length = (num.bit_length() + 7)
        return num.to_bytes(byte_length, 'big').decode()
    @staticmethod
    def int_to_b58(number):
        return base58.b58encode_int(number).decode()
    @staticmethod
    def b58_to_int(b58_string):
        return base58.b58decode_int(b58_string)
def xor_encrypt(message, symmetric_key_b58):
    message_id = TypeConversion.string_to_big_int(message)
    symmetric_key_id = TypeConversion.b58_to_int(symmetric_key_b58)
    encrypted_message_id = message_id ^ symmetric_key_id
    encrypted_message_b58 = TypeConversion.int_to_b58(encrypted_message_id)
    return encrypted_message_b58
def xor_decrypt(encrypted_message_b58, symmetric_key_b58):
    message_int = TypeConversion.b58_to_int(encrypted_message_b58)
    symmetric_key_int = TypeConversion.b58_to_int(symmetric_key_b58)
    decrypted_message_int = message_int ^ symmetric_key_int
    decrypted_message = TypeConversion.big_int_to_string(decrypted_message_int)
    return decrypted_message
if __name__ == "__main__":
    message = "Hello, World!"
    symmetric_key = "5HueCGU8rMjxEXxQk6t6v4F5FzbgQqTjZKLRkxakj89vC"
    encrypted_message_b58 = xor_encrypt(message, symmetric_key)
    print(f"Encrypted message (base-58): {encrypted_message_b58}")
    decrypted_message = xor_decrypt(encrypted_message_b58, symmetric_key)
    print(f"Decrypted message: {decrypted_message}")