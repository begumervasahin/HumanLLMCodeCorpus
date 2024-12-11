import pickle
import sys
class class1:
    def fonk1(self, b1, b2, b3, b4, b5):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
    def fonk2(self):
        return self.b1
    def fonk3(self):
        return self.b2
    def fonk4(self):
        return self.b3
    def fonk5(self):
        return self.b4
    def fonk6(self):
        return self.b5
    def fonk7(self, output_file):
        pickle.dump(self, output_file)
    @staticmethod
    def fonk8(input_file):
        try:
            b6 = pickle.load(input_file)
            if isinstance(b6, class1):
                return b6
        except Exception as e:
            print("Error occurred while loading from file:", e)
            sys.exit()
b7 = class1("b1", "b2", "b3", "b4", "b5")
with open("cipher_file.pickle", "wb") as file:
    b7.fonk7(file)
with open("cipher_file.pickle", "rb") as file:
    b8 = class1.fonk8(file)
print("Loaded b1:", b8.fonk2())
print("Loaded b2:", b8.fonk3())
print("Loaded b3:", b8.fonk4())
print("Loaded b4:", b8.fonk5())
print("Loaded b5:", b8.fonk6())