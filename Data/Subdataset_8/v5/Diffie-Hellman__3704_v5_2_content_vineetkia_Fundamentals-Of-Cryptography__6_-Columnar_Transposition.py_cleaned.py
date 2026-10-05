import math
KEY = "HACK"
def encrypt_message(message):
    cipher = ""
    key_index = 0
    message_length = len(message)
    message_list = list(message)
    key_list = sorted(list(KEY))
    column_count = len(KEY)
    row_count = int(math.ceil(message_length / column_count))
    fill_null = int((row_count * column_count) - message_length)
    message_list.extend('_' * fill_null)
    matrix = [message_list[i: i + column_count] for i in range(0, len(message_list), column_count)]
    for _ in range(column_count):
        curr_index = KEY.index(key_list[key_index])
        cipher += ''.join([row[curr_index] for row in matrix])
        key_index += 1
    return cipher
def decrypt_message(cipher):
    message = ""
    key_index = 0
    message_index = 0
    message_length = len(cipher)
    cipher_list = list(cipher)
    column_count = len(KEY)
    row_count = int(math.ceil(message_length / column_count))
    key_list = sorted(list(KEY))
    dec_cipher = [[] for _ in range(row_count)]
    for _ in range(column_count):
        curr_index = KEY.index(key_list[key_index])
        for j in range(row_count):
            dec_cipher[j].append(cipher_list[message_index])
            message_index += 1
        key_index += 1
    try:
        message = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")
    null_count = message.count('_')
    if null_count > 0:
        return message[:-null_count]
    return message
message = "HelloWorld Nice"
encrypted_message = encrypt_message(message)
print("Encrypted Message: {}".format(encrypted_message))
decrypted_message = decrypt_message(encrypted_message)
print("Decrypted Message: {}".format(decrypted_message))