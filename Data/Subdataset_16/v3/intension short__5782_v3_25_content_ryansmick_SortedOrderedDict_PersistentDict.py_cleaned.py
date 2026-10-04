from collections import OrderedDict
class class1(OrderedDict):
    b1 = ": "
    def fonk1(self, b2 = None, b5=b1,
                 b3 = None, load_delim=b1,
                 b4 = None, b7=None):
        super().fonk1()
        self.b2 = b2
        self.b5 = b5
        if b3:
            self.fonk3(b3, b6 = load_delim,
                      b4 = b4,
                      b7 = b7)
    def fonk2(self, b2 = None, b6=None):
        b8 = b2 or self.b2
        if not b8:
            raise ValueError("A save b8 must be provided either in the constructor or as a parameter to the save method.")
        b6 = b6 or self.b5
        with open(b8, 'w') as file:
            for b11, b10 in self.items():
                file.write(f"{b11}{b6}{b10}\n")
    def fonk3(self, b8, b6 = b1,
             b4 = None, b7=None,
             b9 = False):
        with open(b8, 'r') as file:
            if not b9:
                self.clear()
            for line in file:
                b11, b10 = line.split(b6, 1)
                b10 = b10.rstrip()
                if b4:
                    b11 = b4(b11)
                if b7:
                    b10 = b7(b10)
                self[b11] = b10
    def fonk4(self):
        if not self.b2:
            raise ValueError("A save b8 must be specified to use class1 in a 'with' statement.")
        return self
    def fonk5(self, exception_type, exception_value, traceback):
        self.fonk2()
