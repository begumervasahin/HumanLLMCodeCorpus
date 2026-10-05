import itertools
def generate_bit_combinations(num_bits):
    bit_tuples = list(itertools.product([0, 1], repeat=num_bits))
    bit_strings = [''.join(map(str, bit_tuple)) for bit_tuple in bit_tuples]
    return bit_strings
def crc(message, divisor):
    padding = '0' * (len(divisor) - 1)
    message_padded = message + padding
    message_list = list(message_padded)
    divisor_list = list(divisor)
    for i in range(len(message) - len(padding)):
        if message_list[i] == '1':
            for j in range(len(divisor)):
                message_list[i + j] = str(int(message_list[i + j]) ^ int(divisor_list[j]))
    return ''.join(message_list[-len(padding):])
def calculate_all_collision(message, divisor, prefix_list=None):
    final_crc = crc(message, divisor)
    bit_combinations = generate_bit_combinations(len(divisor))
    collisions = []
    if prefix_list is None:
        prefix_list = generate_bit_combinations(len(message) - len(divisor))
    for prefix in prefix_list:
        for calc_bit in bit_combinations:
            current_message = prefix + calc_bit
            if crc(current_message, divisor) == final_crc:
                collisions.append(current_message)
    return collisions
message = "11010110"
divisor = "10011"
prefix_list = ["111"]
print(calculate_all_collision(message, divisor, prefix_list))