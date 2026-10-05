import rsa
import gmpy2
class RSA(object):
    def get_p_q(self, bits):
        p = rsa.prime.getprime(bits)
        q = rsa.prime.getprime(bits)
        return p, q
    def get_e(self, phi):
        return phi - 1
    def get_keys(self, bits):
        p, q = self.get_p_q(bits)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = self.get_e(phi)
        d = int(gmpy2.invert(e, phi).digits())
        return d, (n, e)
    def crypt(self, e, n, message):
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
    d, (n, e) = rsa_instance.get_keys(bits)
    message = input('Write your message here: ')
    encrypted_message = rsa_instance.crypt(e, n, message)
    print("Encrypted message:", encrypted_message)
    decrypted_message = rsa_instance.decrypt(d, n, encrypted_message)
    print('The decrypted message is:', decrypted_message)