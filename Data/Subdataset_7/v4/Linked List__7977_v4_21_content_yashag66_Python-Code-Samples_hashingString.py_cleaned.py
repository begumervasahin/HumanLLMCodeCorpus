class class1:
    def fonk1(self):
        self.b1 = [None] * 10000
    def fonk2(self, string):
        b2 = self.fonk4(string)
        if self.b1[b2] is None:
            self.b1[b2] = [string]
        else:
            self.b1[b2].append(string)
    def fonk3(self, string):
        b2 = self.fonk4(string)
        if self.b1[b2]:
            return b2
        return -1
    def fonk4(self, string):
        if string:
            return ord(string[0]) * 100 + ord(string[1])
        return -1
b3 = class1()
print(b3.fonk4('UDACITY'))
print(b3.fonk3('UDACITY'))
b3.fonk2('UDACITY')
print(b3.fonk3('UDACITY'))
b3.fonk2('UDACIOUS')
print(b3.fonk3('UDACIOUS'))