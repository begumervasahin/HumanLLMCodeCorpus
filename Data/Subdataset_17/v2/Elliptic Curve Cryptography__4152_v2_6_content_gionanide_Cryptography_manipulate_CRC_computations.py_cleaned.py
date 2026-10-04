import itertools
def generate_combinations(length):
    combinations = [''.join(map(str, bits)) for bits in itertools.product([0, 1], repeat=length)]
    return combinations
def calculate_crc(message, divisor):
    padding = '0' * (len(divisor) - 1)
    padded_message = list(message + padding)
    divisor = list(divisor)
    for i in range(len(padded_message) - len(padding)):
        if padded_message[i] == '1':
            for j in range(len(divisor)):
                padded_message[i + j] = str(int(padded_message[i + j]) ^ int(divisor[j]))
    return ''.join(padded_message[-(len(divisor) - 1):])
def find_crc_collisions(message, divisor, prefix_list=None):
    target_crc = calculate_crc(message, divisor)
    all_combinations = generate_combinations(len(divisor))
    collisions = []
    if prefix_list is None:
        prefix_list = generate_combinations(len(message) - len(divisor))
    for prefix in prefix_list:
        for combination in all_combinations:
            test_message = prefix + combination
            if calculate_crc(test_message, divisor) == target_crc:
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