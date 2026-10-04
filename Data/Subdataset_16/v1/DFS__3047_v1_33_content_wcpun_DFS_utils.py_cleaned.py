class class1:
    def fonk1(self, b2, b3, b1 = None, b4=None):
        self.b2 = b2
        self.b3 = b3
        self.b1 = b1
        self.b4 = b4
    def fonk2(self):
        return (f"User ID: {self.b2}\n"
                f"File Name: {self.b3}\n"
                f"File Size: {self.b1}\n"
                f"IV: {self.b4}")
class class2:
    def fonk3(self, b5):
        self.b5 = b5
    def fonk4(self):
        return f"Key: {self.b5}"
class class3:
    def fonk5(self, b6):
        self.b6 = b6
    def fonk6(self):
        return f"class3: {self.b6}"
if b7 = = "__main__":
    b8 = class1(b2=123, b3="example.txt", b1=2048, b4="abcdef123456")
    b9 = class2(b5="mysecretkey")
    b6 = class3(b6="encryptedtext")
    print(b8)
    print(b9)
    print(b6)