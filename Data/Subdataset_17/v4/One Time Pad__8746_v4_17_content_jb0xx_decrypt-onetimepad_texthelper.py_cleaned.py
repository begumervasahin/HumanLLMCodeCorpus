def hex_to_nums(msg):
    len_msg = len(msg)
    bytes_array = [0] * len_msg
    for i in range(len_msg):
        digit1 = hex_num_helper(msg[2 * i])
        digit2 = hex_num_helper(msg[2 * i + 1])
        bytes_array[i] = 16 * digit1 + digit2
    return bytes_array
def nums_to_hex(nums):
    return [hex(n)[2:].upper().zfill(2) for n in nums]
def hex_num_helper(hex_val):
    if hex_val.isdigit():
        return int(hex_val)
    return ord(hex_val.upper()) - 55
def bytes_to_chars(bytes_array):
    return [chr(b) for b in bytes_array]
def xor_chrs(chrs):
    xor_result = 0
    for c in chrs:
        xor_result ^= ord(c)
    return chr(xor_result)