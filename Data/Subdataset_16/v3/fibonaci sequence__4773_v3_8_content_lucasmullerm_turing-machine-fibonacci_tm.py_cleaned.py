import enum
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = {}
    def fonk2(self, b3):
        self.b2[b3.b4] = b3
    def fonk3(self, symbol):
        b3 = self.b2.get(symbol, None)
        if b3:
            return b3.b6, b3.b5, b3.b7
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
        return self.b8[self.a3] if not self.fonk6() else -1
    def fonk8(self):
        self.a3 = 0
    def fonk9(self):
        return self.a3
    def fonk10(self, symbol):
        self.b8 = self.b8[:self.a3] + symbol + self.b8[self.a3 + 1:]
    def fonk11(self, to_write, b7):
        if self.fonk6():
            raise Exception('End of computation.')
        self.fonk10(to_write)
        if b7 = = class2.class3.a1:
            self.a3 += 1
        elif b7 = = class2.class3.a2:
            self.a3 -= 1
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
        self.b9[source_state].fonk14(b3)
    def fonk15(self, state_value):
        self.b10 = self.b9[state_value]
        self.b13 = self.b9[state_value]
    def fonk16(self, b11):
        self.b11 = b11
    def fonk17(self):
        self.b10 = self.b13
        self.b11.fonk8()
        self.b12 = True
        b14 = self.fonk18()
        return b14
    def fonk18(self):
        b14 = f"class1: ({self.b10.b1}) {self.b11.b8}\n"
        b14 += f"{' ' * (12 + self.b11.fonk9())}^\n"
        return b14
    def fonk19(self):
        if not self.b12:
            return "Computation has stopped.\n"
        self.b10, to_write, b7 = self.b10.fonk3(self.b11.fonk7())
        if to_write:
            self.b11.fonk11(to_write, b7)
        if to_write is None or self.b11.fonk6():
            self.b12 = False
            return "\nEnd of computation\n"
        else:
            return self.fonk18()
    def fonk20(self):
        with open("b14.txt", "a") as log_file:
            log_file.b5("Beginning computation\n\n")
            log_file.b5(self.fonk17())
            while self.b12:
                b15 = self.fonk19()
                log_file.b5(b15)
            log_file.b5("--------------------------------------\n")
if b16 = = "__main__":
    pass