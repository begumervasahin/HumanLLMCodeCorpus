import sys
import re
def pow_x(g_base, exponent, modulus):
    result = 1
    bits = bin(exponent)[2:]
    for bit in bits:
        result = (result ** 2) % modulus
        if bit == '1':
            result = (result * g_base) % modulus
    return result
def attack(modulus, base, ga_value):
    for possible_a in range(modulus):
        if pow_x(base, possible_a, modulus) == ga_value:
            return possible_a
    return 0
def parse_input_file(file_path):
    with open(file_path, 'r') as file:
        content = file.readline().strip()
        p_str, g_str, ga_str = content.split(',')
        modulus = int(re.findall(r'\d+', p_str)[0])
        base = int(re.findall(r'\d+', g_str)[0])
        ga_value = int(re.findall(r'\d+', ga_str)[0])
    return modulus, base, ga_value
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    modulus, base, ga_value = parse_input_file(input_file)
    secret_exponent = attack(modulus, base, ga_value)
    if secret_exponent:
        print(f"The secret exponent is: {secret_exponent}")
    else:
        print("Exponent not found.")
if __name__ == '__main__':
    main()