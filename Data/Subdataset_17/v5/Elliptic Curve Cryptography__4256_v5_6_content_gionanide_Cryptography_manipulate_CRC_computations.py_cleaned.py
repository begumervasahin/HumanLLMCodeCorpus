import itertools
def generate_binary_combinations(length):
    return [''.join(map(str, bits)) for bits in itertools.product('01', repeat=length)]
def compute_crc(message, divisor):
    padding = '0' * (len(divisor) - 1)
    padded_message = list(message + padding)
    divisor = list(divisor)
    for i in range(len(padded_message) - len(padding)):
        if padded_message[i] == '1':
            for j in range(len(divisor)):
                padded_message[i + j] = str(int(padded_message[i + j]) ^ int(divisor[j]))
    return ''.join(padded_message[-(len(divisor) - 1):])
def find_crc_collisions(message, divisor, prefix_list=None):
    target_crc = compute_crc(message, divisor)
    combination_length = len(divisor)
    all_combinations = generate_binary_combinations(combination_length)
    collisions = []
    if prefix_list is None:
        prefix_length = len(message) - combination_length
        prefix_list = generate_binary_combinations(prefix_length)
    for prefix in prefix_list:
        for combination in all_combinations:
            test_message = prefix + combination
            if compute_crc(test_message, divisor) == target_crc:
                collisions.append(test_message)
    return collisions
if __name__ == "__main__":
    message = "11010110"
    divisor = "10011"
    prefixes = ["111"]
    collisions = find_crc_collisions(message, divisor, prefixes)
    print("Collisions:")
    for collision in collisions:
        print(collision)