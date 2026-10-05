import math
def encrypt_message(msg, key):
    cipher = ""
    k_index = 0
    msg_length = float(len(msg))
    msg_list = list(msg)
    key_list = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_length / col))
    fill_null = int((row * col) - msg_length)
    msg_list.extend('_' * fill_null)
    matrix = [msg_list[i: i + col] for i in range(0, len(msg_list), col)]
    for _ in range(col):
        curr_index = key.index(key_list[k_index])
        cipher += ''.join([row[curr_index] for row in matrix])
        k_index += 1
    return cipher
def decrypt_message(cipher, key):
    msg = ""
    k_index = 0
    msg_index = 0
    msg_length = float(len(cipher))
    msg_list = list(cipher)
    col = len(key)
    row = int(math.ceil(msg_length / col))
    key_list = sorted(list(key))
    dec_cipher = [[] for _ in range(row)]
    for _ in range(col):
        curr_index = key.index(key_list[k_index])
        for j in range(row):
            dec_cipher[j].append(msg_list[msg_index])
            msg_index += 1
        k_index += 1
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")
    null_count = msg.count('_')
    if null_count > 0:
        return msg[:-null_count]
    return msg
def main():
    key = "HACK"
    msg = "HelloWorld Nice"
    cipher = encrypt_message(msg, key)
    print("Encrypted Message: {}".format(cipher))
    decrypted_msg = decrypt_message(cipher, key)
    print("Decrypted Message: {}".format(decrypted_msg))
if __name__ == "__main__":
    main()