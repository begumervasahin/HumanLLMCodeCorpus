def hex_to_nums(hex_string):
    num_bytes = len(hex_string)
    decimal_values = [0] * num_bytes
    for i in range(num_bytes):
        digit1 = hex_digit_to_decimal(hex_string[2 * i])
        digit2 = hex_digit_to_decimal(hex_string[2 * i + 1])
        decimal_values[i] = 16 * digit1 + digit2
    return decimal_values
def nums_to_hex(decimal_values):
    return [hex(n)[2:].upper().zfill(2) for n in decimal_values]
def hex_digit_to_decimal(hex_digit):
    if hex_digit.isdigit():
        return int(hex_digit)
    return ord(hex_digit.upper()) - 55
def bytes_to_chars(byte_values):
    return [chr(b) for b in byte_values]
def xor_chars(chars):
    xor_result = 0
    for char in chars:
        xor_result ^= ord(char)
    return chr(xor_result)
hex_message = "48656C6C6F"
decimal_values = hex_to_nums(hex_message)
hex_values = nums_to_hex(decimal_values)
char_values = bytes_to_chars(decimal_values)
xor_result = xor_chars(char_values)
print(f"Hex Message: {hex_message}")
print(f"Decimal Values: {decimal_values}")
print(f"Hex Values: {hex_values}")
print(f"Character Values: {char_values}")
print(f"XOR Result: {xor_result}")