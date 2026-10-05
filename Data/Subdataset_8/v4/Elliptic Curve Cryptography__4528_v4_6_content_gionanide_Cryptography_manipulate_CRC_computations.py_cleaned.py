import itertools
def generate_bit_combinations(num_bits):
    bit_tuples = list(itertools.product([0, 1], repeat=num_bits))
    bit_strings = [''.join(map(str, bit_tuple)) for bit_tuple in bit_tuples]
    return bit_strings
def crc(message, divisor):
    padding = '0' * (len(divisor) - 1)
    message += padding
    message = list(message)
    divisor = list(divisor)
    for i in range(len(message) - len(padding)):
        if message[i] == '1':
            for j in range(len(divisor)):
                message[i + j] = str(int(message[i + j]) ^ int(divisor[j]))
    return ''.join(message[-len(padding):])
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
print(calculate_all_collision("11010110", "10011", ["111"]))