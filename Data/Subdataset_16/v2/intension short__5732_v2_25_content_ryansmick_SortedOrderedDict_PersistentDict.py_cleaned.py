from collections import OrderedDict
class class1(OrderedDict):
    b1 = ": "
    def fonk1(self, b2 = None, b5=b1,
                 b3 = None, load_delim=b1,
                 b4 = None, load_value_trans_func=None):
        super().fonk1()
        self.b2 = b2
        self.b5 = b5
        if b3:
            self.fonk3(b3, b6 = load_delim,
                      b7 = b4,
                      b8 = load_value_trans_func)
    def fonk2(self, b2 = None, b6=None):
        b9 = b2 or self.b2
        if not b9:
            raise ValueError("A save b9 must be provided either in the constructor or as a parameter to the save method.")
        b6 = b6 or self.b5
        with open(b9, 'w') as file:
            for b12, b11 in self.items():
                file.write(f"{b12}{b6}{b11}\n")
    def fonk3(self, b9, b6 = b1,
             b7 = None, b8=None,
             b10 = False):
        with open(b9, 'r') as file:
            if not b10:
                self.clear()
            for line in file:
                b12, b11 = line.split(b6, 1)
                b11 = b11.rstrip()
                if b7:
                    b12 = b7(b12)
                if b8:
                    b11 = b8(b11)
                self[b12] = b11
    def fonk4(self):
        if not self.b2:
            raise ValueError("A save b9 must be specified to use class1 in a 'with' statement.")
        return self
    def fonk5(self, exception_type, exception_value, traceback):
        self.fonk2()
