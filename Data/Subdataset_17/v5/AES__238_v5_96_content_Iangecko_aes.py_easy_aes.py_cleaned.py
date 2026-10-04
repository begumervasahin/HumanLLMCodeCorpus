import aes
class EasyAES:
    def __init__(self):
        self.CIPHER = aes.AES(256)
    def encrypt(self, text, key):
        blocks = self._sub_divide(text, 16)
        if not blocks:
            return None
        padding = 16 - len(blocks[-1])
        blocks[-1] += padding * "="
        padding_info = format(padding, "x") * 16
        blocks.append(padding_info)
        key_hash = self._expand_key(key)
        encrypted_blocks = ""
        for block in blocks:
            encrypted_block = self.CIPHER.encrypt(str(key_hash), block)
            encrypted_blocks += ''.join(f'{i:02x}' for i in encrypted_block)
        return encrypted_blocks
    def decrypt(self, cipher_text, key):
        blocks = self._sub_divide(cipher_text, 32)
        if not blocks:
            return None
        key_hash = self._expand_key(key)
        plain_text = ""
        for block in blocks:
            cipher_block = [int(h, 16) for h in self._sub_divide(block, 2)]
            decrypted_block = self.CIPHER.decrypt(str(key_hash), cipher_block)
            plain_text += self.CIPHER.to_plain(decrypted_block)
        padding_length = int(plain_text[-1], 16)
        return plain_text[:-16 - padding_length]
    def _sub_divide(self, data, chunk_size):
        return [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    def _expand_key(self, key):
        key_hash = 1
        for i, char in enumerate(key):
            key_hash += ord(char) << (8 * i)
        while key_hash < 0xfffffffffffff:
            key_hash *= key_hash
        key_hash &= 0xfffffffffffff
        return key_hash
if __name__ == "__main__":
    cipher = EasyAES()
    KEY = "Tis but a scratch!"
    DATA = "A scratch?! your arm's off!"
    encrypted_text = cipher.encrypt(DATA, KEY)
    if encrypted_text:
        print("CIPHER TEXT: " + encrypted_text)
    decrypted_text = cipher.decrypt(encrypted_text, KEY)
    if decrypted_text:
        print("\nPLAIN TEXT: " + decrypted_text)