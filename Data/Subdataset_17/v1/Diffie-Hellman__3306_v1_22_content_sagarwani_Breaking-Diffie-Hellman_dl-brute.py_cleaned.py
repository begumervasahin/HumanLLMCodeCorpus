import sys
import re
def pow_x(g_base, a, p_mod):
    x = 1
    bits = "{0:b}".format(a)
    for bit in bits:
        x = (x ** 2) % p_mod
        if bit == '1':
            x = (x * g_base) % p_mod
    return x
def attack(p, g, ga):
    for mystry_a in range(p):
        if pow_x(g, mystry_a, p) == ga:
            return mystry_a
    return 0
def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)
    input_file = sys.argv[1]
    with open(input_file, 'r') as my_file1:
        content = my_file1.readline()
        x, y, z = content.split(',')
        p = int(re.findall('\d+', x)[0])
        g = int(re.findall('\d+', y)[0])
        ga = int(re.findall('\d+', z)[0])
    a = attack(p, g, ga)
    if a:
        print(a)
    else:
        print("Exponent not found.")
if __name__ == '__main__':
    main()