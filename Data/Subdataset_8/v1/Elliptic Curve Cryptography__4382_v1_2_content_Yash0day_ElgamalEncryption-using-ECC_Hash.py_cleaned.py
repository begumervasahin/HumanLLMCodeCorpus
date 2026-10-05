def new_ascii(ch):
    ascii_value = ord(ch) + 100
    return ascii_value
def old_ascii(ascii_val):
    old_ascii = int(ascii_val) - 100
    return old_ascii
def encode(msg):
    string_ascii = ''
    for char in msg:
        string_ascii += str(new_ascii(char))
    return string_ascii
def decode(new_ascii_string):
    dec_message = ''
    i = 0
    while i < len(new_ascii_string):
        pack = new_ascii_string[i:i+3]
        dec_message += chr(old_ascii(pack))
        i += 3
    return dec_message
if __name__ == "__main__":
    message = "Hello, World!"
    encoded_message = encode(message)
    print("Encoded:", encoded_message)
    decoded_message = decode(encoded_message)
    print("Decoded:", decoded_message)