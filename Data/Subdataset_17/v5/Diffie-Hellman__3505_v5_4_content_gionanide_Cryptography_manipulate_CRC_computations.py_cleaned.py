import itertools
def generate_binary_combinations(length):
    return [''.join(bits) for bits in itertools.product('01', repeat=length)]
def compute_crc(message, divisor):
    padded_message = message + '0' * (len(divisor) - 1)
    message_bits = list(padded_message)
    divisor_bits = list(divisor)
    for i in range(len(message_bits) - len(divisor_bits) + 1):
        if message_bits[i] == '1':
            for j in range(len(divisor_bits)):
                message_bits[i + j] = str(int(message_bits[i + j]) ^ int(divisor_bits[j]))
    return ''.join(message_bits[-(len(divisor_bits) - 1):])
def find_crc_collisions(message, divisor, prefix_list=None):
    target_crc = compute_crc(message, divisor)
    collision_candidates = generate_binary_combinations(len(divisor))
    if prefix_list is None:
        prefix_list = generate_binary_combinations(len(message) - len(divisor))
    collisions = []
    for prefix in prefix_list:
        for candidate in collision_candidates:
            combined_message = prefix + candidate
            if compute_crc(combined_message, divisor) == target_crc:
                collisions.append(combined_message)
    return collisions
if __name__ == "__main__":
    original_message = "11010110"
    crc_divisor = "10011"
    prefixes = ["111"]
    collision_results = find_crc_collisions(original_message, crc_divisor, prefixes)
    print("Collisions found:")
    for collision in collision_results:
        print(collision)