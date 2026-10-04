import os
from ecdsa.curves import SECP256k1
import threshold_cryptosystem as threshold
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def generate_keys(num_keys):
    private_keys = [threshold.generate_key() for _ in range(num_keys)]
    public_keys = [key * SECP256k1.generator for key in private_keys]
    return private_keys, public_keys
def big_num(num):
    return f"new BigNumber('{num}')"
def stringify_point(point):
    return f"{big_num(point.x())},{big_num(point.y())}"
def write_to_file(filepath, content):
    with open(filepath, 'w') as file:
        file.write(content)
def prepare_js_content(private_keys, public_keys):
    private_js_content = 'var secKeys = [{}]'.format(','.join([big_num(key) for key in private_keys]))
    public_js_content = 'var pubKeys = [{}]'.format(','.join([f"[{stringify_point(key)}]" for key in public_keys]))
    return private_js_content, public_js_content
def prepare_txt_content(private_keys, public_keys):
    private_txt_content = '\n'.join(map(str, private_keys))
    public_txt_content = '\n'.join([f"{key.x()},{key.y()}" for key in public_keys])
    return private_txt_content, public_txt_content
def main():
    num_keys = 50
    directory = 'keys/'
    create_directory(directory)
    private_keys, public_keys = generate_keys(num_keys)
    private_js_content, public_js_content = prepare_js_content(private_keys, public_keys)
    private_txt_content, public_txt_content = prepare_txt_content(private_keys, public_keys)
    write_to_file(os.path.join(directory, 'private.js'), private_js_content)
    write_to_file(os.path.join(directory, 'public.js'), public_js_content)
    write_to_file(os.path.join(directory, 'private.txt'), private_txt_content)
    write_to_file(os.path.join(directory, 'public.txt'), public_txt_content)
if __name__ == "__main__":
    main()