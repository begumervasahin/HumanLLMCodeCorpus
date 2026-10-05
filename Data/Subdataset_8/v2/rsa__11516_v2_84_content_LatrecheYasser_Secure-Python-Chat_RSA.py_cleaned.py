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
        E = int.from_bytes(bytes(message.encode()), byteorder='little')
        return pow(E, e, n)
    def decrypt(self, d, n, message):
        msg = pow(message, d, n)
        msg = msg.to_bytes((msg.bit_length()
        return msg
if __name__ == "__main__":
    bits = int(input('Enter the number of bits in the keys: '))
    Rsa = RSA()
    d, (n, e) = Rsa.get_keys(bits)
    message = input('Write your message here: ')
    encrypted_message = Rsa.crypt(e, n, message)
    print('Encrypted message:', encrypted_message)
    decrypted_message = Rsa.decrypt(d, n, encrypted_message)
    print('The decrypted message is:', decrypted_message)