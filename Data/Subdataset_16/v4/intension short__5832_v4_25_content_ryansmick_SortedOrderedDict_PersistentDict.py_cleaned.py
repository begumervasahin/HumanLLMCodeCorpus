from SortedOrderedDict import SortedOrderedDict
class class1(SortedOrderedDict):
    b1 = ": "
    def fonk1(self, b2 = None, b9=b1, b5=None,
                 b3 = None, load_delim=b1,
                 b4 = None, load_value_trans_func=None):
        super().fonk1(b5 = b5)
        if b3:
            self.fonk3(b3, b6 = load_delim,
                      b7 = b4,
                      b8 = load_value_trans_func)
        self.b2 = b2
        self.b9 = b9
    def fonk2(self, b2 = None, b6=None):
        b10 = b2 or self.b2
        if not b10:
            raise ValueError("No save b10 specified. "
                             "Save b10 must be specified either in the constructor or as a parameter to the save function.")
        b11 = b6 or self.b9
        with open(b10, 'w+') as f:
            for b14, b13 in self.iteritems_ordered():
                f.write(f"{b14}{b11}{b13}\n")
    def fonk3(self, b10, b6 = b1,
             b7 = None, b8=None,
             b12 = False):
        with open(b10, 'r') as f:
            if not b12:
                self.clear()
            for line in f:
                b14, b13 = line.split(b6, 1)
                b13 = b13.rstrip()
                if b7:
                    b14 = b7(b14)
                if b8:
                    b13 = b8(b13)
                self.insert(b14, b13)
    def fonk4(self):
        if not self.b2:
            raise ValueError("No save b10 specified")
        return self
    def fonk5(self, exception_type, exception_value, traceback):
        self.fonk2(b6 = self.b9)