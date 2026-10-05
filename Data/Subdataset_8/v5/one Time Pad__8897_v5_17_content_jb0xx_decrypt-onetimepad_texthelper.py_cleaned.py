def hex_to_nums(hex_msg):
    num_bytes = len(hex_msg)
    nums = []
    for i in range(num_bytes):
        digit1 = hex_digit_to_decimal(hex_msg[2 * i])
        digit2 = hex_digit_to_decimal(hex_msg[2 * i + 1])
        nums.append(16 * digit1 + digit2)
    return nums
def nums_to_hex(nums):
    return [hex(n)[2:].upper().zfill(2) for n in nums]
def hex_digit_to_decimal(hex_digit):
    if ord(hex_digit) < 65:
        return int(hex_digit)
    else:
        return ord(hex_digit.upper()) - 55
def bytes_to_chars(byte_list):
    return [chr(b) for b in byte_list]
def xor_chars(char_list):
    xor_result = 0
    for char in char_list:
        xor_result ^= ord(char)
    return chr(xor_result)