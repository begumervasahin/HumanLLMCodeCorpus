import random
PRIME = 26994308385016394749558484505346578147056894665639
BASE = 2
def generate_private_key(filename):
    private_key = str(random.randint(1000, 10000))
    with open(filename, 'w') as outfile:
        outfile.write(private_key)
def generate_public_key(private_filename, public_filename):
    with open(private_filename, 'r') as infile:
        private_key = int(infile.read())
    public_key = pow(BASE, private_key, PRIME)
    with open(public_filename, 'w') as outfile:
        outfile.write(str(public_key))
def generate_shared_secret(private_filename, public_filename):
    with open(private_filename, 'r') as infile:
        private_key = int(infile.read())
    with open(public_filename, 'r') as infile:
        public_key = int(infile.read())
    shared_secret = pow(public_key, private_key, PRIME)
    return shared_secret
def main():
    private_file = 'private_key.txt'
    public_file = 'public_key.txt'
    generate_private_key(private_file)
    generate_public_key(private_file, public_file)
    shared_secret = generate_shared_secret(private_file, public_file)
    print(f'Shared Secret: {shared_secret}')
if __name__ == '__main__':
    main()