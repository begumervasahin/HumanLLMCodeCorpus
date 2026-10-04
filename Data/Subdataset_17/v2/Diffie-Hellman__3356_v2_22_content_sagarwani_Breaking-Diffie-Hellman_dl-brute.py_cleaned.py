import sys
import re
def pow_x(g_base, a, p_mod):
    result = 1
    bits = bin(a)[2:]
    for bit in bits:
        result = (result ** 2) % p_mod
        if bit == '1':
            result = (result * g_base) % p_mod
    return result
def attack(p, g, ga):
    for possible_a in range(p):
        if pow_x(g, possible_a, p) == ga:
            return possible_a
    return 0
def parse_input_file(file_path):
    with open(file_path, 'r') as file:
        content = file.readline().strip()
        p_str, g_str, ga_str = content.split(',')
        p = int(re.findall(r'\d+', p_str)[0])
        g = int(re.findall(r'\d+', g_str)[0])
        ga = int(re.findall(r'\d+', ga_str)[0])
    return p, g, ga
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    p, g, ga = parse_input_file(input_file)
    secret_exponent = attack(p, g, ga)
    if secret_exponent:
        print(f"The secret exponent is: {secret_exponent}")
    else:
        print("Exponent not found.")
if __name__ == '__main__':
    main()