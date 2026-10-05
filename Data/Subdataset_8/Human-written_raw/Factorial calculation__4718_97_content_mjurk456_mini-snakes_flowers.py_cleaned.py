
class Flower():
    def __init__(self, num = 0, price = 0):
        self.num = num
        self.price = price
        self.start = num
        return None
    def sell(self, x):
        self.num = self.num - x
        return None
    def get_items(self):
        return self.num
    def set_items(self, x):
        if self.num == 0:
            self.start = x
        self.num = x
        return None
    def set_price(self, x):
        self.price = x
        return None
    def get_price(self):
        return self.price
    def total_store_price(self):
        return self.num * self.price
    def total_sold(self):
        return self.start - self.num
    def total_receipts(self):
        return self.total_sold() * self.price
def main():
    roza = Flower(70, 5)
    tulipan = Flower(225, 0.75)
    bez = Flower(15, 5)
    print('{:*^80}'.format("DEMONSTRACJA KLASY UÅ»YTKOWNIKA Flowers"))
    print("\nW magazynie jest %d rÃ³Å¼, %d tulipanÃ³w i %d bzu." \
          % (roza.get_items(), tulipan.get_items(), bez.get_items()))
    print("Razem kwiaty kosztujÄ
 %f zÅ." \
          % (roza.total_store_price() + tulipan.total_store_price() \
           + bez.total_store_price()))
    print("W ciÄ
gu dnia sprzedano tylko 5 tulipanÃ³w i dlatego je przeceniono.")
    tulipan.set_price(0.10)
    tulipan.sell(5)
    print("Nowa cena jest %f zÅ." % tulipan.price)
    print("W magazynie zostaÅo %d tulipanÃ³w o ogÃ³lnej wartoÅci %f zÅ"\
          % (tulipan.num, tulipan.total_store_price()))
    roza.sell(56)
    bez.sell(5)
    roza.sell(5)
    print("W ciÄ
gu dnia sprzedano teÅ¼ %d rÃ³Å¼ i %d bzu." \
          % (roza.total_sold(), bez.total_sold()))
    print("Dzienny zysk dla wszystkich kwiatÃ³w wyniÃ³sÅ %f zÅ.\n" \
          % (roza.total_receipts() + tulipan.total_receipts() \
             + bez.total_receipts()))
    print("{:*^80}".format("END"))
if __name__ == "__main__":
    main()