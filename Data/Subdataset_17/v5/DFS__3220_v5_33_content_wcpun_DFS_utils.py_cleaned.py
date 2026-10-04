class Meta:
    def __init__(self, user_id, file_name, file_size=None, iv=None):
        self.user_id = user_id
        self.file_name = file_name
        self.file_size = file_size
        self.iv = iv
    def __str__(self):
        return (
            f"User ID: {self.user_id}\n"
            f"File Name: {self.file_name}\n"
            f"File Size: {self.file_size}\n"
            f"IV: {self.iv}"
        )
class Code:
    def __init__(self, key):
        self.key = key
    def __str__(self):
        return f"Key: {self.key}"
class Cipher:
    def __init__(self, cipher):
        self.cipher = cipher
    def __str__(self):
        return f"Cipher: {self.cipher}"
def main():
    meta = Meta(user_id=123, file_name="example.txt", file_size=2048, iv="abcdef123456")
    code = Code(key="mysecretkey")
    cipher = Cipher(cipher="encryptedtext")
    print(meta)
    print(code)
    print(cipher)
if __name__ == "__main__":
    main()