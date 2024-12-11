class class1:
    def fonk1(self, b1 = 10000):
        self.b1 = b1
        self.b2 = [None] * b1
    def fonk2(self, string):
        b3 = self.fonk4(string)
        if self.b2[b3] is None:
            self.b2[b3] = [string]
        else:
            self.b2[b3].append(string)
    def fonk3(self, string):
        b3 = self.fonk4(string)
        if self.b2[b3] and string in self.b2[b3]:
            return b3
        return -1
    def fonk4(self, string):
        if len(string) < 2:
            return -1
        return ord(string[0]) * 100 + ord(string[1])
b4 = class1()
print(b4.fonk4('UDACITY'))
print(b4.fonk3('UDACITY'))
b4.fonk2('UDACITY')
print(b4.fonk3('UDACITY'))
b4.fonk2('UDACIOUS')
print(b4.fonk3('UDACIOUS'))