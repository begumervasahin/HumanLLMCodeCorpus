class Meta:
    def __init__(self, user_id, fileName, fileSize=None, iv=None):
        self.user_id = user_id
        self.fileName = fileName
        self.fileSize = fileSize
        self.iv = iv
    def __str__(self):
        return (f"User ID: {self.user_id}\n"
                f"File Name: {self.fileName}\n"
                f"File Size: {self.fileSize}\n"
                f"IV: {self.iv}")
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
if __name__ == "__main__":
    meta = Meta(user_id=123, fileName="example.txt", fileSize=2048, iv="abcdef123456")
    code = Code(key="mysecretkey")
    cipher = Cipher(cipher="encryptedtext")
    print(meta)
    print(code)
    print(cipher)