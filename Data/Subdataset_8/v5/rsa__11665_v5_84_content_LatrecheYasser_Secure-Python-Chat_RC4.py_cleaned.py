class RC4:
    def __init__(self):
        self.state = list(range(256))
    def shuffle(self, key):
        j = 0
        key_length = len(key)
        for i in range(256):
            j = (j + self.state[i] + ord(key[i % key_length])) % 256
            self.state[i], self.state[j] = self.state[j], self.state[i]
    def crypt(self, text):
        output = []
        i = j = 0
        for char in text:
            i = (i + 1) % 256
            j = (self.state[i] + j) % 256
            self.state[i], self.state[j] = self.state[j], self.state[i]
            keystream = self.state[(self.state[i] + self.state[j]) % 256]
            output.append(chr(ord(char) ^ keystream))
        return ''.join(output)
if __name__ == "__main__":
    rc4 = RC4()
    key = input('Enter your key: ')
    rc4.shuffle(key)
    rc4_decryptor = RC4()
    rc4_decryptor.shuffle(key)
    while True:
        message = input('Enter your message: ')
        encrypted_message = rc4.crypt(message)
        print('Encrypted message: ', encrypted_message)
        decrypted_message = rc4_decryptor.crypt(encrypted_message)
        print('Decrypted message: ', decrypted_message)