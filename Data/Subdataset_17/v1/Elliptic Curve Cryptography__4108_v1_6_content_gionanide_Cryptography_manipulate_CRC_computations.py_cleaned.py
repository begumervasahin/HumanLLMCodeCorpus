import itertools
def generate_combinations(num):
    tuples = list(itertools.product([0, 1], repeat=num))
    combinations = [''.join(map(str, tpl)) for tpl in tuples]
    return combinations
def crc(message, divisor):
    pad = '0' * (len(divisor) - 1)
    message = list(message + pad)
    divisor = list(divisor)
    for i in range(len(message) - len(pad)):
        if message[i] == '1':
            for j in range(len(divisor)):
                message[i + j] = str(int(message[i + j]) ^ int(divisor[j]))
    return ''.join(message[-len(pad):])
def calculate_all_collisions(message, divisor, prefix_list=None):
    final_crc = crc(message, divisor)
    combinations = generate_combinations(len(divisor))
    results = []
    if prefix_list is None:
        prefix_list = generate_combinations(len(message) - len(divisor))
    for prefix in prefix_list:
        for calc_bit in combinations:
            curr_msg = prefix + calc_bit
            if crc(curr_msg, divisor) == final_crc:
                results.append(curr_msg)
    return results
if __name__ == "__main__":
    message = "11010110"
    divisor = "10011"
    prefixes = ["111"]
    collisions = calculate_all_collisions(message, divisor, prefixes)
    print("Collisions:")
    for collision in collisions:
        print(collision)