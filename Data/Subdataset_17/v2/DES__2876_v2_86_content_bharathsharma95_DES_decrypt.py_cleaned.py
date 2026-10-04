
def DES_decryption(data_bytes, key_bytes):
    print("Decrypting file ...\n")
    print(f"Key bytes data: {key_bytes}\n")
    print(f"Cipher data bytes: {data_bytes}\n")
    out_data = data_bytes.copy()
    for round_number in range(8):
        for i in range(0, len(data_bytes), 2):
            data_pair = [data_bytes[i], data_bytes[i + 1]]
            key_byte = key_bytes[7 - round_number]
            out_data[i:i + 2] = iterate(data_pair, key_byte)
        data_bytes = out_data.copy()
    return out_data
def iterate(data_bytes, key_byte):
    data_left = data_bytes[0]
    data_right = data_bytes[1]
    data_left_dash = data_right ^ key_byte
    data_right_dash = data_left
    return [data_left_dash, data_right_dash]
if __name__ == "__main__":
    encrypted_data = [0x29, 0x38, 0xB4, 0xF9, 0xD2, 0xE4, 0xA1, 0xC3]
    decryption_key = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F, 0x7E, 0x8F]
    decrypted_data = DES_decryption(encrypted_data, decryption_key)
    print(f"Decrypted Data: {decrypted_data}")