
Sbox = [
]
Rcon = [0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a]
def format_hex(hex_str):
    return hex_str[2:]
def sbox_substitute(message):
    substituted = []
    for char in message:
        hex_value = format_hex(hex(ord(char)))
        sbox_value = Sbox[int(hex_value, 16)]
        substituted.append(format_hex(hex(sbox_value)))
    return substituted
def main():
    key = 'Thats my Kung Fu'
    print(f"Key length: {len(key.encode('utf-8'))} bytes")
    msg = 'Two One Nine Two'
    print(f"Message: {msg}")
    print(f"Message length: {len(msg.encode('utf-8'))} bytes")
    substituted_msg = sbox_substitute(msg)
    print("S-box substituted values:", substituted_msg)
    blocks = [substituted_msg[i:i+4] for i in range(0, len(substituted_msg), 4)]
    for i, block in enumerate(blocks):
        print(f"Block {i+1}: {block}")
if __name__ == "__main__":
    main()