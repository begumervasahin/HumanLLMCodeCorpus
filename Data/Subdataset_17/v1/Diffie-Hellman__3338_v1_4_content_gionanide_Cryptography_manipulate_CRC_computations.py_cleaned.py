import itertools
def generate_binary_combinations(num_bits):
    tuples = list(itertools.product([0, 1], repeat=num_bits))
    return [''.join(map(str, t)) for t in tuples]
def crc(message, divisor):
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
    final_crc = crc(message, divisor)
    collision_candidates = generate_binary_combinations(len(divisor))
    result = []
    if prefix_list is None:
        prefix_list = generate_binary_combinations(len(message) - len(divisor))
    for prefix in prefix_list:
        for candidate in collision_candidates:
            combined_message = prefix + candidate
            if crc(combined_message, divisor) == final_crc:
                result.append(combined_message)
    return result
if __name__ == "__main__":
    message = "11010110"
    divisor = "10011"
    prefix_list = ["111"]
    collisions = find_crc_collisions(message, divisor, prefix_list)
    print("Collisions found:")
    for collision in collisions:
        print(collision)