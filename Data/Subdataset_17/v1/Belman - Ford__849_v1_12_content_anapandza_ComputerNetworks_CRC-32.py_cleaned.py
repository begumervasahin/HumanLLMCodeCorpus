import codecs
def create_table():
    table = []
    for i in range(256):
        rem = i
        for _ in range(8):
            if rem & 1:
                rem = (rem >> 1) ^ 0xEDB88320
            else:
                rem >>= 1
        table.append(rem)
    return table
def crc_update(buf, crc_table):
    crc = 0xffffffff
    for k in buf:
        crc = (crc >> 8) ^ crc_table[(crc & 0xff) ^ k]
    return crc ^ 0xffffffff
def main():
    message = 'FAFAFA'
    message_bin = bin(int(message, 16))[2:]
    print(f"Ulazna poruka je: {message_bin} (0x{message})")
    crc_table = create_table()
    checksum = crc_update(codecs.decode(message, 'hex'), crc_table)
    checksum_bin = bin(checksum)[2:]
    print(f"Rezultat je: {checksum_bin} ({hex(checksum)})")
    send_message = message_bin + checksum_bin
    print("Poruka koja se salje je:")
    print(send_message)
if __name__ == "__main__":
    main()