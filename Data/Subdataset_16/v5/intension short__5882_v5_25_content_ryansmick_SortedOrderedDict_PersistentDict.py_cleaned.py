from SortedOrderedDict import SortedOrderedDict
class class1(SortedOrderedDict):
    b1 = ": "
    def fonk1(self, b2 = None, b6=b1, b5=None,
                 b3 = None, load_delim=b1,
                 b4 = None, load_value_trans_func=None):
        super().fonk1(b5 = b5)
        self.b2 = b2
        self.b6 = b6
        if b3:
            self.fonk3(b7 = b3, b10=load_delim,
                      b8 = b4,
                      b9 = load_value_trans_func)
    def fonk2(self, b2 = None, b10=None):
        b7 = b2 or self.b2
        if not b7:
            raise ValueError("No save b7 specified. "
                             "Specify it in the constructor or as a parameter to the save method.")
        b10 = b10 or self.b6
        with open(b7, 'w') as file:
            for b13, b12 in self.iteritems_ordered():
                file.write(f"{b13}{b10}{b12}\n")
    def fonk3(self, b7, b10 = b1,
             b8 = None, b9=None,
             b11 = False):
        if not b11:
            self.clear()
        with open(b7, 'r') as file:
            for line in file:
                b13, b12 = line.split(b10, 1)
                b12 = b12.rstrip()
                if b8:
                    b13 = b8(b13)
                if b9:
                    b12 = b9(b12)
                self.insert(b13, b12)
    def fonk4(self):
        if not self.b2:
            raise ValueError("No save b7 specified.")
        return self
    def fonk5(self, exception_type, exception_value, traceback):
        self.fonk2()