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
        except:
            print ">> ERROR corrupted ciphered file "
            sys.exit()