import re
from CurrencyExchange import CurrencyExchange
class class1:
    def fonk1(self, iFileName):
        self.b1 = iFileName
    def fonk2(self, iNameLine):
        b2 = iNameLine.split(" ", 1)
        assert len(b2) == 2
        return b2
    def fonk3(self, iRateLine):
        b3 = iRateLine.split(" ", 2)
        assert len(b3) == 3
        return CurrencyExchange(*b3)
    def fonk4(self):
        b4 = re.compile("[A-Z]{3} [A-Z\(\)\.& \-]+")
        b5 = re.compile("[A-Z]{3} [A-Z]{3} \d+(\.\d+)?")
        b6 = {}
        b7 = []
        try:
            b8 = open(self.b1, 'r')
            for b9 in b8.readlines():
                b9 = b9.rstrip("\n\r")
                if re.match(b5, b9):
                    b7.append(self.fonk3(b9))
                elif re.match(b4, b9):
                    currencyCode, b10 = self.fonk2(b9)
                    b6[currencyCode] = b10
                else:
                    raise Exception("Invalid b9 in file " + self.b1 + ": " + b9)
        except IOError as exception:
            print "Cannot open file " + self.b1 + ": " + str(exception)
        return b6, b7