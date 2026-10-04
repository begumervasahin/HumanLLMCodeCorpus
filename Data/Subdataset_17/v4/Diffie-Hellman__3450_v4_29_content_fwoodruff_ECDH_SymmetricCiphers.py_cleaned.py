import TypeConversion as TC
def xor_encrypt(message, symmetric_key_b58):
    message_int = TC.string_to_big_int(message)
    symmetric_key_int = TC.b58_to_int(symmetric_key_b58)
    encrypted_message_int = message_int ^ symmetric_key_int
    encrypted_message_b58 = TC.int_to_b58(encrypted_message_int)
    return encrypted_message_b58
def xor_decrypt(encrypted_message_b58, symmetric_key_b58):
    encrypted_message_int = TC.b58_to_int(encrypted_message_b58)
    symmetric_key_int = TC.b58_to_int(symmetric_key_b58)
    decrypted_message_int = encrypted_message_int ^ symmetric_key_int
    decrypted_message = TC.big_int_to_string(decrypted_message_int)
    return decrypted_message