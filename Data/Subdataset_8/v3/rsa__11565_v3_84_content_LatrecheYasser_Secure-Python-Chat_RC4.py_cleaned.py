class RC4:
    def __init__(self):
        self.state = list(range(256))
    def initialize_state(self, key):
        j = 0
        for i in range(256):
            j = (j + self.state[i] + ord(key[i % len(key)])) % 256
            self.state[i], self.state[j] = self.state[j], self.state[i]
    def generate_keystream(self, text):
        i = j = 0
        keystream = []
        for _ in range(len(text)):
            i = (i + 1) % 256
            j = (self.state[i] + j) % 256
            self.state[i], self.state[j] = self.state[j], self.state[i]
            keystream.append(self.state[(self.state[i] + self.state[j]) % 256])
        return keystream
    def crypt(self, text, keystream):
        output = []
        for char, keystream_byte in zip(text, keystream):
            output.append(chr(ord(char) ^ keystream_byte))
        return ''.join(output)
if __name__ == "__main__":
    rc4 = RC4()
    rc4_decrypt = RC4()
    key = input('Enter your key: ')
    rc4.initialize_state(key)
    rc4_decrypt.initialize_state(key)
    while True:
        message = input('Enter your message: ')
        keystream = rc4.generate_keystream(message)
        encrypted_message = rc4.crypt(message, keystream)
        print('Encrypted message:', encrypted_message)
        decrypted_message = rc4_decrypt.crypt(encrypted_message, keystream)
        print('Decrypted message:', decrypted_message)