import rsa
import gmpy2
class RSA:
    def get_prime_pair(self, bits):
        p = rsa.prime.getprime(bits)
        q = rsa.prime.getprime(bits)
        return p, q
    def calculate_public_exponent(self, phi):
        return phi - 1
    def generate_keys(self, bits):
        p, q = self.get_prime_pair(bits)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = self.calculate_public_exponent(phi)
        d = int(gmpy2.invert(e, phi).digits())
        return d, (n, e)
    def encrypt(self, e, n, message):
        encoded_message = int.from_bytes(bytes(message.encode()), byteorder='little')
        encrypted_message = pow(encoded_message, e, n)
        return encrypted_message
    def decrypt(self, d, n, message):
        decrypted_message = pow(message, d, n)
        decoded_message = decrypted_message.to_bytes((decrypted_message.bit_length()
        return decoded_message
if __name__ == "__main__":
    bits = int(input('Enter the number of bits in the keys: '))
    rsa_instance = RSA()
    private_key, public_key = rsa_instance.generate_keys(bits)
    message = input('Write your message here: ')
    encrypted_message = rsa_instance.encrypt(public_key[1], public_key[0], message)
    print("Encrypted message:", encrypted_message)
    decrypted_message = rsa_instance.decrypt(private_key, public_key[0], encrypted_message)
    print('The decrypted message is:', decrypted_message)