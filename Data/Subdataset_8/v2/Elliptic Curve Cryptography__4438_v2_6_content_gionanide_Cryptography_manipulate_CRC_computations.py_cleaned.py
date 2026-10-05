import itertools
def generate_bit_combinations(length):
    bit_tuples = list(itertools.product([0, 1], repeat=length))
    bit_strings = []
    for bit_tuple in bit_tuples:
        bit_string = "".join(map(str, bit_tuple))
        bit_strings.append(bit_string)
    return bit_strings
def crc(message, divisor):
    padding = '0' * (len(divisor) - 1)
    padded_message = message + padding
    padded_message_list = list(padded_message)
    divisor_list = list(divisor)
    for i in range(len(padded_message) - len(padding)):
        if padded_message_list[i] == '1':
            for j in range(len(divisor)):
                padded_message_list[i + j] = str(int(padded_message_list[i + j]) ^ int(divisor_list[j]))
    return ''.join(padded_message_list[-len(padding):])
def find_collision(message, divisor, prefix_list=None):
    final_crc = crc(message, divisor)
    possible_bit_combinations = generate_bit_combinations(len(divisor))
    collisions = []
    if prefix_list is None:
        prefix_list = generate_bit_combinations(len(message) - len(divisor))
    for prefix in prefix_list:
        for bit_combination in possible_bit_combinations:
            current_message = prefix + bit_combination
            if crc(current_message, divisor) == final_crc:
                collisions.append(current_message)
    return collisions
message = "11010110"
divisor = "10011"
prefix_list = ["111"]
print(find_collision(message, divisor, prefix_list))