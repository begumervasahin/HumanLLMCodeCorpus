def hex_to_nums(hex_string):
    num_bytes = len(hex_string)
    byte_array = []
    for i in range(num_bytes):
        digit1 = hex_digit_to_num(hex_string[2 * i])
        digit2 = hex_digit_to_num(hex_string[2 * i + 1])
        byte_array.append(16 * digit1 + digit2)
    return byte_array
def nums_to_hex(numbers):
    return [format(n, '02X') for n in numbers]
def hex_digit_to_num(hex_val):
    if ord(hex_val) < 65:
        value = int(hex_val)
    else:
        value = ord(hex_val.upper()) - 55
    return value
def bytes_to_chars(byte_array):
    return [chr(b) for b in byte_array]
def xor_characters(characters):
    xor_value = 0
    for c in characters:
        xor_value ^= ord(c)
    return chr(xor_value)
hex_message = "48656C6C6F20576F726C64"
numbers = hex_to_nums(hex_message)
print("Numbers:", numbers)
hexadecimal_rep = nums_to_hex(numbers)
print("Hexadecimal representation:", hexadecimal_rep)
characters = bytes_to_chars(numbers)
print("Characters:", characters)
xor_result = xor_characters(characters)
print("XOR result:", xor_result)