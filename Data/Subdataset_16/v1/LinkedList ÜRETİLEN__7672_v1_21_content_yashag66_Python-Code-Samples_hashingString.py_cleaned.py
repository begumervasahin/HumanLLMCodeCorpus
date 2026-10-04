class class1(object):
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
        if self.b1[b2] is not None and string in self.b1[b2]:
            return b2
        return -1
    def fonk4(self, string):
        if string:
            return ord(string[0]) * 100 + ord(string[1])
        return -1
if b3 = = "__main__":
    b4 = class1()
    print(b4.fonk4('UDACITY'))
    print(b4.fonk3('UDACITY'))
    b4.fonk2('UDACITY')
    print(b4.fonk3('UDACITY'))
    b4.fonk2('UDACIOUS')
    print(b4.fonk3('UDACIOUS'))
