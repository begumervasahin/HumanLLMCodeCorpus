
def DES_decryption(data_bytes, key_bytes):
    print("Decrypting file ...")
    print("")
    print("Key bytes data: " + str(key_bytes))
    print("")
    print("Cipher data bytes: " + str(data_bytes))
    print("")
    out_data = data_bytes.copy()
    for rounds in range(8):
        for i in range(0, len(data_bytes), 2):
            data_pair = [data_bytes[i], data_bytes[i + 1]]
            key_byte = key_bytes[7 - rounds]
            out_data[i:i + 2] = iteration(data_pair, key_byte)
        data_bytes = out_data.copy()
    return out_data
def iteration(data_bytes, key_byte):
    data_L = data_bytes[0]
    data_R = data_bytes[1]
    data_L_dash = data_R ^ key_byte
    data_R_dash = data_L
    return [data_L_dash, data_R_dash]
if __name__ == "__main__":
    encrypted_data = [0x29, 0x38, 0xB4, 0xF9, 0xD2, 0xE4, 0xA1, 0xC3]
    decryption_key = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F, 0x7G, 0x8H]
    decrypted_data = DES_decryption(encrypted_data, decryption_key)
    print("Decrypted Data: " + str(decrypted_data))