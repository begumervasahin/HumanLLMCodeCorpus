import enum
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = {}
    def fonk2(self, b3):
        self.b2[b3.b4] = b3
    def fonk3(self, symbol):
        try:
            b3 = self.b2[symbol]
            return b3.b6, b3.b5, b3.b7
        except KeyError:
            return self, None, None
class class2:
    class class3(enum.Enum):
        a1 = 1
        a2 = 2
    def fonk4(self, b4, b5, b6, b7):
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
class class4:
    def fonk5(self, b8):
        self.b8 = b8
        self.a3 = 0
    def fonk6(self):
        return self.a3 < 0 or self.a3 >= len(self.b8)
    def fonk7(self):
        return -1 if self.fonk6() else self.b8[self.a3]
    def fonk8(self):
        self.a3 = 0
    def fonk9(self):
        return self.a3
    def fonk10(self, symbol):
        if not self.fonk6():
            self.b8 = self.b8[:self.a3] + symbol + self.b8[self.a3 + 1:]
    def fonk11(self, to_write, b7):
        if not self.fonk6():
            self.fonk10(to_write)
            self.a3 += 1 if b7 = = class2.class3.a1 else -1
class class5:
    def fonk12(self):
        self.b9 = {}
        self.b10 = None
        self.b11 = None
        self.b12 = True
        self.b13 = None
    def fonk13(self, state):
        self.b9[state.b1] = state
    def fonk14(self, source_state, b3):
        if source_state in self.b9:
            self.b9[source_state].fonk14(b3)
    def fonk15(self, state):
        if state in self.b9:
            self.b10 = self.b13 = self.b9[state]
    def fonk16(self, b11):
        self.b11 = b11
    def fonk17(self):
        if self.b13 and self.b11:
            self.b10 = self.b13
            self.b11.fonk8()
            b14 = f"class1: ({self.b10.b1}) {self.b11.b8}\n"
            b14 += " " * self.b11.fonk9() + "^\n"
            return b14
    def fonk18(self):
        if self.b12 and self.b10 and self.b11:
            b6, to_write, b7 = self.b10.fonk3(self.b11.fonk7())
            if to_write:
                self.b11.fonk11(to_write, b7)
            if to_write is None or self.b11.fonk6():
                self.b12 = False
                return "\nEnd of computation\n"
            else:
                b14 = f"class1: ({self.b10.b1}) {self.b11.b8}\n"
                b14 += " " * self.b11.fonk9() + "^\n"
                return b14
    def fonk19(self):
        if self.b13 and self.b11:
            with open("b14.txt", "a") as log_file:
                log_file.b5("Beginning computation\n\n")
                log_file.b5(self.fonk17() or "")
                while self.b12:
                    b15 = self.fonk18()
                    log_file.b5(b15 or "")
                log_file.b5("--------------------------------------\n")
if b16 = = "__main__":
    b17 = class5()
    b18 = class1(0)
    b19 = class1(1)
    b20 = class2(0, 1, b19, class2.class3.a1)
    b21 = class2(1, 0, b18, class2.class3.a1)
    b17.fonk13(b18)
    b17.fonk13(b19)
    b17.fonk14(0, b20)
    b17.fonk14(1, b21)
    b17.fonk15(0)
    b17.fonk16(class4("0101010101010101"))
    b17.fonk19()