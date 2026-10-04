import itertools
def generate_binary_combinations(num_bits):
    tuples = itertools.product('01', repeat=num_bits)
    return [''.join(t) for t in tuples]
def compute_crc(message, divisor):
    pad = '0' * (len(divisor) - 1)
    message = message + pad
    message = list(message)
    divisor = list(divisor)
    for i in range(len(message) - len(pad)):
        if message[i] == '1':
            for j in range(len(divisor)):
                message[i + j] = str(int(message[i + j]) ^ int(divisor[j]))
    return ''.join(message[-len(pad):])
def find_crc_collisions(message, divisor, prefix_list=None):
    target_crc = compute_crc(message, divisor)
    candidate_combinations = generate_binary_combinations(len(divisor))
    collisions = []
    if prefix_list is None:
        prefix_list = generate_binary_combinations(len(message) - len(divisor))
    for prefix in prefix_list:
        for candidate in candidate_combinations:
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