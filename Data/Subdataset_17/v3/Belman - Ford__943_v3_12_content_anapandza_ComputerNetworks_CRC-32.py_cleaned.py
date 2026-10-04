import codecs
def create_crc_table():
    crc_table = []
    polynomial = 0xEDB88320
    for byte in range(256):
        remainder = byte
        for bit in range(8):
            if remainder & 1:
                remainder = (remainder >> 1) ^ polynomial
            else:
                remainder >>= 1
        crc_table.append(remainder)
    return crc_table
def calculate_crc_checksum(data, crc_table):
    crc = 0xFFFFFFFF
    for byte in data:
        crc = (crc >> 8) ^ crc_table[(crc & 0xFF) ^ byte]
    return crc ^ 0xFFFFFFFF
def main():
    message_hex = 'FAFAFA'
    message_bin = bin(int(message_hex, 16))[2:]
    print(f"Input message: {message_bin} (0x{message_hex})")
    crc_table = create_crc_table()
    message_bytes = codecs.decode(message_hex, 'hex')
    checksum = calculate_crc_checksum(message_bytes, crc_table)
    checksum_bin = bin(checksum)[2:].zfill(32)
    print(f"Checksum: {checksum_bin} ({hex(checksum)})")
    send_message = message_bin + checksum_bin
    print("Message to be sent:")
    print(send_message)
if __name__ == "__main__":
    main()