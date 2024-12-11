import pandas as pd
from multiprocessing import Pool
import sys
from your_module import RequestsBS4, DataProcessing
class class1:
    def fonk1(self, b1 = "https:
        self.b1 = b1
    def fonk2(self):
        pass
    def fonk3(self):
        pass
    def fonk4(self, b2 = None):
        pass
    def fonk5(self, b2 = None):
        pass
    def fonk6(self):
        pass
    def fonk7(self):
        print("\nWelcome to Macy's Web class1!")
        while True:
            b3 = input("\nEnter 't' to scrape a small sample, "
                                  "\n'f' to scrape full web, "
                                  "\n's' to search for product information, "
                                  "\nor press 'q' to quit the program: ").upper()
            if b3 = = 'Q':
                print("Exiting the program.")
                sys.exit()
            if b3 in ['T', 'F', 'S']:
                break
            else:
                print("Invalid choice. Please try again.")
        if b3 = = 'T':
            self.fonk8()
        elif b3 = = 'F':
            self.fonk9()
        elif b3 = = 'S':
            self.fonk10()
    def fonk8(self):
        b2 = self.fonk3()
        b4 = Pool(processes=2)
        b4.map(self.scrape_and_save, b2)
        b4.close()
        b4.join()
    def fonk9(self):
        b5 = self.fonk2()
        b6 = Pool(processes=4)
        b7 = b6.map(self.get_url_products, b5)
        b6.close()
        b6.join()
        b8 = pd.read_csv("product-b2.csv", names=["b2"])
        b2 = b8["b2"].values.tolist()
        b9 = Pool(processes=2)
        b9.map(self.scrape_and_save, b2)
        b9.close()
        b9.join()
    def fonk10(self):
        self.fonk6()
if b10 = = "__main__":
    b11 = class1()
    b11.fonk7()