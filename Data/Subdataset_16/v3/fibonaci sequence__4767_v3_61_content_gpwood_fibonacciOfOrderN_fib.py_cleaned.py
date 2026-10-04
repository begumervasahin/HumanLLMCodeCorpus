class class1:
    def fonk1(self, b1 = 2, b2=10):
        self.a1 = 0
        self.a2 = 0
        self.b1 = b1
        self.b2 = b2
        self.b3 = [1] * b1
    def fonk2(self):
        if self.a1 = = self.b2:
            print(f"Ratio {self.b1}: {self.a2}")
            return
        b4 = sum(self.b3)
        self.a2 = b4 / self.b3[-1]
        self.a1 += 1
        if len(self.b3) >= self.b1:
            self.b3 = self.b3[1:] + [b4]
        else:
            self.b3.append(b4)
        self.fonk2()
def fonk3():
    print("class1 Ratios (Ctrl-C to Exit):")
    try:
        for i in range(2, 56):
            b5 = class1(i, 54)
            b5.fonk2()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
if b6 = = "__main__":
    fonk3()