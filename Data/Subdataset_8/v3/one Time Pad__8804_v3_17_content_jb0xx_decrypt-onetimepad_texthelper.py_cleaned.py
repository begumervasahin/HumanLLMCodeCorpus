def hex_to_dec(hex_string):
    num_bytes = len(hex_string)
    dec_list = []
    for i in range(num_bytes):
        digit1 = hex_digit_to_dec(hex_string[2 * i])
        digit2 = hex_digit_to_dec(hex_string[2 * i + 1])
        dec_list.append(16 * digit1 + digit2)
    return dec_list
def dec_to_hex(dec_list):
    return [format(n, '02X') for n in dec_list]
def hex_digit_to_dec(hex_val):
    if ord(hex_val) < 65:
        value = int(hex_val)
    else:
        value = ord(hex_val.upper()) - 55
    return value
def bytes_to_chars(byte_list):
    return [chr(byte) for byte in byte_list]
def xor_characters(char_list):
    xor_value = 0
    for char in char_list:
        xor_value ^= ord(char)
    return chr(xor_value)
hex_message = "48656C6C6F20576F726C64"
decimal_list = hex_to_dec(hex_message)
print("Decimal List:", decimal_list)
hex_representation = dec_to_hex(decimal_list)
print("Hexadecimal Representation:", hex_representation)
character_list = bytes_to_chars(decimal_list)
print("Character List:", character_list)
xor_result = xor_characters(character_list)
print("XOR Result:", xor_result)