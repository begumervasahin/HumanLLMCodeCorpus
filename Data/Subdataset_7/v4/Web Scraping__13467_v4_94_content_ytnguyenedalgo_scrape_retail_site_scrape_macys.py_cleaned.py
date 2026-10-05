import pandas as pd
import sys
from multiprocessing import Pool
from readyscrape import RequestsBS4, DataProcessing
class class1:
    def fonk1(self, b1 = "https:
        self.b1 = b1
    def fonk2(self):
        b2 = RequestsBS4(self.b1)
        b3 = b2.get_url()
        b4 = b2.b4
        print(b4.b16)
        print("\nGETTING CATEGORIES b10...")
        b5 = set()
        for tag in b3.find_all("a", b6 = True):
            b7 = tag["b6"]
            if "http" not in b7 and "COL" in b7 and "/shop/" in b7:
                b5.add(self.b1 + b7)
        b5 = list(b5)
        return b5
    def fonk3(self):
        b8 = self.fonk2()
        b9 = b8[-1]
        b3 = RequestsBS4(b9).get_url()
        b10 = []
        for tag in b3.find_all("a", {"class": "productDescLink"}):
            b7 = tag.get("b6")
            b10.append(self.b1 + b7)
        print('\n{} b10 are now fetched from {}'.format(len(b10), b9))
        b11 = {'b14': b10}
        b12 = ['b14']
        b13 = "product-b14.csv"
        b10 = DataProcessing(b11, b12, b13).add_to_csv()
        return b10
    def fonk4(self, b14 = None):
        b3 = RequestsBS4(b14).get_url()
        b10 = []
        for tag in b3.find_all("a", {"class": "productDescLink"}):
            b7 = tag.get("b6")
            b10.append(self.b1 + b7)
        print('\n{} b10 are now fetched from {}'.format(len(b10), b14))
        b11 = {'b14': b10}
        b12 = ['b14']
        b13 = "product-b14.csv"
        b10 = DataProcessing(b11, b12, b13).add_to_csv()
        return b10
    def fonk5(self, b14 = None):
        b2 = RequestsBS4(b14)
        b3 = b2.get_url()
        b4 = b2.b4
        name_ls, price_ls, b15 = [], [], []
        if b4.b16 = = 200:
            print('\nProcesscing... {}'.format(b14))
        try:
            b17 = (((b3.find_all("h1", {"class": "p-b17 h3"})[0].text)\
                     .replace("\n", "")).strip()).upper()
            b18 = ((b3.find_all("div", {"class": "b18"})[0].text)\
                     .replace("\n", "")).strip()
            b19 = ((b3.find_all("p", {"data-auto": "product-description"})[0].text)\
                   .replace("\n", "")).strip()
            if b17 != None and b18 != None and b19 != None:
                name_ls.append(b17)
                price_ls.append(b18)
                b15.append(b19)
        except IndexError:
            pass
        b12 = ['b17', 'b18', 'b19']
        b13 = "macys-products.csv"
        b11 = {b12[0]: name_ls,
                    b12[1]: price_ls,
                    b12[2]: b15}
        DataProcessing(b11, b12, b13).add_to_csv()
    def fonk6(self):
        while True:
            b20 = False
            b21 = input("\nEnter product b17\nOr type 'q' to quit the program: ")
            b17 = str(b21).upper()
            if b17 = = 'Q':
                break
            b22 = pd.read_csv('macys-products.csv')
            for index, row in b22.iterrows():
                if b17 = = row[0]:
                    print("\nProduct Name: {} \nPrice: {} \nDetails: {}".format(row[0], row[1], row[2]))
                    b20 = True
            if b20:
                print('\nNext search...')
            else:
                print('\nNo product with such b17. Please try again!')
if b23 = = "__main__":
    b24 = class1()
    b25 = input("\nEnter 't' to scrape a small sample,\n'f' to scape full web,\n"
                          "'s' to search for product information,\n"
                          "or press 'q' to quit the program: ").upper()
    while b25 not in ['T', 'F', 'S', 'Q']:
        b25 = b25
    if b25 = = 'Q':
        sys.exit()
    if b25 = = 'T':
        b14 = b24.fonk3()
        b26 = Pool(processes=2)
        b27 = b26.map(b24.scrape_and_save, b14)
        b26.terminate()
        b26.join()
    elif b25 = = 'F':
        b8 = b24.fonk2()
        b28 = Pool(processes=4)
        b29 = b28.map(b24.get_url_products, b8)
        b28.terminate()
        b28.join()
        b30 = pd.read_csv("product-b14.csv", names=["b14"])
        b14 = b30["b14"].values.tolist()
        b26 = Pool(processes=2)
        b27 = b26.map(b24.scrape_and_save, b14)
        b26.terminate()
        b26.join()
    elif b25 = = 'S':
        b24.fonk6()