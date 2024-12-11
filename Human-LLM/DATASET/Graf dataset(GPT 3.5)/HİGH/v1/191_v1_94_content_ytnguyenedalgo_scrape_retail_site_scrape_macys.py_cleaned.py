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
if b3 = = "__main__":
    b4 = class1()
    b5 = input("\nEnter 't' to scrape a small sample,\
                          \n'f' to scape full web,\
                          \n's' to search for product information,\
                          \nor press 'q' to quit the program: ").upper()
    while b5 not in ['T', 'F', 'S', 'Q']:
        b5 = input("Invalid choice. Enter 't', 'f', 's', or 'q': ").upper()
    if b5 = = 'Q':
        sys.exit()
    if b5 = = 'T':
        b2 = b4.fonk3()
        b6 = Pool(processes=2)
        b7 = b6.map(b4.scrape_and_save, b2)
        b6.terminate()
        b6.join()
    elif b5 = = 'F':
        b8 = b4.fonk2()
        b9 = Pool(processes=4)
        b10 = b9.map(b4.get_url_products, b8)
        b9.terminate()
        b9.join()
        b11 = pd.read_csv("product-b2.csv", names=["b2"])
        b2 = b11["b2"].values.tolist()
        b6 = Pool(processes=2)
        b7 = b6.map(b4.scrape_and_save, b2)
        b6.terminate()
        b6.join()
    elif b5 = = 'S':
        b4.fonk6()