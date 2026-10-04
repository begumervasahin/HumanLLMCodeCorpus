from collections import OrderedDict
class class1(OrderedDict):
    b1 = ": "
    def fonk1(self, b2 = None, b4=b1, load_filepath=None, load_delim=b1,
                 b3 = None, load_value_trans_func=None):
        super().fonk1()
        self.b2 = b2
        self.b4 = b4
        if load_filepath:
            self.fonk3(load_filepath, b5 = load_delim, key_trans_func=b3, value_trans_func=load_value_trans_func)
    def fonk2(self, b2 = None, b5=None):
        b6 = b2 or self.b2
        if not b6:
            raise ValueError("No save b6 specified. Save b6 must be specified as either constructor parameter or save function parameter")
        b7 = b5 or self.b4
        with open(b6, 'w') as f:
            for b9, b8 in self.items():
                f.write(f"{b9}{b7}{b8}\n")
    def fonk3(self, b6, b5 = b1, key_trans_func=None, value_trans_func=None, add_to_existing=False):
        with open(b6, 'r') as f:
            if not add_to_existing:
                self.clear()
            for line in f:
                b9, b8 = line.split(b5, 1)
                b8 = b8.rstrip()
                if key_trans_func:
                    b9 = key_trans_func(b9)
                if value_trans_func:
                    b8 = value_trans_func(b8)
                self[b9] = b8
    def fonk4(self):
        if not self.b2:
            raise ValueError("No save b6 specified")
        return self
    def fonk5(self, exception_type, exception_value, traceback):
        self.fonk2(b5 = self.b4)
