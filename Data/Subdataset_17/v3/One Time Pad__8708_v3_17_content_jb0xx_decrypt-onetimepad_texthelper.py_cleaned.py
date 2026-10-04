def hex_to_nums(msg):
    len_msg = len(msg)
    return [16 * hex_num_helper(msg[2 * i]) + hex_num_helper(msg[2 * i + 1]) for i in range(len_msg)]
def nums_to_hex(nums):
    return [format(n, '02X') for n in nums]
def hex_num_helper(hex_val):
    return int(hex_val, 16)
def bytes_to_chars(bytes_array):
    return [chr(b) for b in bytes_array]
def xor_chrs(chrs):
    val = 0
    for c in chrs:
        val ^= ord(c)
    return chr(val)
if __name__ == "__main__":
    hex_message = "4A6F686E20446F65"
    nums = hex_to_nums(hex_message)
    print(f"Hex to Nums: {nums}")
    hex_vals = nums_to_hex(nums)
    print(f"Nums to Hex: {hex_vals}")
    chars = bytes_to_chars(nums)
    print(f"Bytes to Chars: {chars}")
    xor_result = xor_chrs(chars)
    print(f"XOR of Chars: {xor_result}")