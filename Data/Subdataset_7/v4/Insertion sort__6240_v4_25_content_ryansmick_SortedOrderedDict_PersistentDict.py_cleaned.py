from SortedOrderedDict import SortedOrderedDict
class class1(SortedOrderedDict):
    b1 = ": "
    def fonk1(self, b2 = None, b8=b1, b5=None,
                 b3 = None, load_delim=': ', load_key_trans_func=None,
                 b4 = None):
        super().fonk1(b5 = b5)
        if b3:
            self.fonk3(b3, b6 = load_delim, key_trans_func=load_key_trans_func,
                      b7 = load_key_trans_func)
        self.b2 = b2
        self.b8 = b8
    def fonk2(self, b2 = None, b6=None):
        b9 = b2 or self.b2
        b10 = b6 or self.b8
        if not b9:
            raise ValueError("No save b9 specified. Save b9 must be specified as either constructor parameter or save function parameter")
        with open(b9, 'w+') as file:
            for b12, b11 in self.iteritems_ordered():
                file.write(f"{b12}{b10}{b11}\n")
    def fonk3(self, b9, b6 = ': ', key_trans_func=None, b7=None, add_to_existing=False):
        with open(b9, 'r') as file:
            if not add_to_existing:
                self.clear()
            for line in file:
                b12, b11 = line.split(b6, 1)
                b11 = b11.rstrip()
                if key_trans_func:
                    b12 = key_trans_func(b12)
                if b7:
                    b11 = b7(b11)
                self.insert(b12, b11)
    def fonk4(self):
        if not self.b2:
            raise ValueError("No save b9 specified")
        return self
    def fonk5(self, exception_type, exception_value, traceback):
        self.fonk2(b6 = self.b8)