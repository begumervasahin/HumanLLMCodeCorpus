import os
from ecdsa.curves import SECP256k1
import threshold_cryptosystem as threshold
def big_num(num):
    return f"new BigNumber('{num}')"
def stringify_point(point):
    return f"{big_num(point.x())},{big_num(point.y())}"
def main():
    num_keys = 50
    directory = 'keys/'
    if not os.path.exists(directory):
        os.makedirs(directory)
    s_keys = [threshold.generate_key() for _ in range(num_keys)]
    p_keys = [k * SECP256k1.generator for k in s_keys]
    with open(os.path.join(directory, 'private.js'), 'w') as private_js_file:
        private_js_content = 'var secKeys = [{}]'.format(''.join([big_num(k) + ',' for k in s_keys])[:-1])
        private_js_file.write(private_js_content)
    with open(os.path.join(directory, 'public.js'), 'w') as public_js_file:
        public_js_content = 'var pubKeys = [{}]'.format(''.join([f"[{stringify_point(k)}]," for k in p_keys])[:-1])
        public_js_file.write(public_js_content)
    with open(os.path.join(directory, 'private.txt'), 'w') as private_txt_file:
        private_txt_content = ''.join([str(k) + '\n' for k in s_keys])
        private_txt_file.write(private_txt_content)
    with open(os.path.join(directory, 'public.txt'), 'w') as public_txt_file:
        public_txt_content = ''.join([f"{k.x()},{k.y()}\n" for k in p_keys])
        public_txt_file.write(public_txt_content)
if __name__ == "__main__":
    main()