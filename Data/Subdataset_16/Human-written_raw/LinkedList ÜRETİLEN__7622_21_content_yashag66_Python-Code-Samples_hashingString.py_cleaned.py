
class class1(object):
    def fonk1(self):
        self.b1 = [None]*10000
    def fonk2(self, string):
        if self.b1[self.fonk4(string)] == None:
            self.b1[self.fonk4(string)] = [string]
        else:
            self.b1[self.fonk4(string)].append(string)
    def fonk3(self, string):
        if self.b1[self.fonk4(string)]:
            return self.fonk4(string)
        return -1
    def fonk4(self, string):
        if string:
            return ord(string[0]) * 100 + ord(string[1])
        return -1
b2 = class1()
print b2.fonk4('UDACITY')
print b2.fonk3('UDACITY')
b2.fonk2('UDACITY')
print b2.fonk3('UDACITY')
b2.fonk2('UDACIOUS')
print b2.fonk3('UDACIOUS')