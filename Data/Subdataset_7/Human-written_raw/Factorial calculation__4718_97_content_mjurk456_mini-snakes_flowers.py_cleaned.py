
class class1():
    def fonk1(self, b1 = 0, b2 = 0):
        self.b1 = b1
        self.b2 = b2
        self.b3 = b1
        return None
    def fonk2(self, x):
        self.b1 = self.b1 - x
        return None
    def fonk3(self):
        return self.b1
    def fonk4(self, x):
        if self.b1 = = 0:
            self.b3 = x
        self.b1 = x
        return None
    def fonk5(self, x):
        self.b2 = x
        return None
    def fonk6(self):
        return self.b2
    def fonk7(self):
        return self.b1 * self.b2
    def fonk8(self):
        return self.b3 - self.b1
    def fonk9(self):
        return self.fonk8() * self.b2
def fonk10():
    b4 = class1(70, 5)
    b5 = class1(225, 0.75)
    b6 = class1(15, 5)
    print('{:*^80}'.format("DEMONSTRACJA KLASY UÅ»YTKOWNIKA Flowers"))
    print("\nW magazynie jest %d rÃ³Å¼, %d tulipanÃ³w i %d bzu." \
          % (b4.fonk3(), b5.fonk3(), b6.fonk3()))
    print("Razem kwiaty kosztujÄ
 %f zÅ." \
          % (b4.fonk7() + b5.fonk7() \
           + b6.fonk7()))
    print("W ciÄ
gu dnia sprzedano tylko 5 tulipanÃ³w i dlatego je przeceniono.")
    b5.fonk5(0.10)
    b5.fonk2(5)
    print("Nowa cena jest %f zÅ." % b5.b2)
    print("W magazynie zostaÅo %d tulipanÃ³w o ogÃ³lnej wartoÅci %f zÅ"\
          % (b5.b1, b5.fonk7()))
    b4.fonk2(56)
    b6.fonk2(5)
    b4.fonk2(5)
    print("W ciÄ
gu dnia sprzedano teÅ¼ %d rÃ³Å¼ i %d bzu." \
          % (b4.fonk8(), b6.fonk8()))
    print("Dzienny zysk dla wszystkich kwiatÃ³w wyniÃ³sÅ %f zÅ.\n" \
          % (b4.fonk9() + b5.fonk9() \
             + b6.fonk9()))
    print("{:*^80}".format("END"))
if b7 = = "__main__":
    fonk10()