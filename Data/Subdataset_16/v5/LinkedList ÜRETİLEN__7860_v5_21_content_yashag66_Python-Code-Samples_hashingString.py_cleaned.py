class class1:
    def fonk1(self, b1 = 10000):
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
    @staticmethod
    def fonk4(string):
        if len(string) < 2:
            raise ValueError("String must have at least two characters")
        return ord(string[0]) * 100 + ord(string[1])
if b4 = = "__main__":
    b5 = class1()
    print("Hash value for 'UDACITY':", b5.fonk4('UDACITY'))
    print("Lookup 'UDACITY' before storing:", b5.fonk3('UDACITY'))
    b5.fonk2('UDACITY')
    print("Lookup 'UDACITY' after storing:", b5.fonk3('UDACITY'))
    b5.fonk2('UDACIOUS')
    print("Lookup 'UDACIOUS' after storing:", b5.fonk3('UDACIOUS'))