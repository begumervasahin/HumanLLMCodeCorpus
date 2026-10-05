def hex_to_nums(msg):
    len_msg = int(len(msg) / 2)
    bytes_array = [0] * len_msg
    for i in range(len_msg):
        digit1 = hex_num_helper(msg[2 * i])
        digit2 = hex_num_helper(msg[2 * i + 1])
        bytes_array[i] = 16 * digit1 + digit2
    return bytes_array
def nums_to_hex(nums):
    return [hex(n).upper()[2:].zfill(2) for n in nums]
def hex_num_helper(hex_val):
    if ord(hex_val) < 65:
        val = int(hex_val)
    else:
        val = ord(hex_val.upper()) - 55
    return val
def bytes_to_chars(bytes_array):
    return [chr(b) for b in bytes_array]
def xor_chars(chars):
    val = 0
    for c in chars:
        val ^= ord(c)
    return chr(val)