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
        print(b4.b14)
        print("\nGETTING CATEGORIES URLs...")
        b5 = set()
        for tag in b3.find_all("a", b6 = True):
            b7 = tag["b6"]
            if "http" not in b7 and "COL" in b7 and "/shop/" in b7:
                b5.add(self.b1 + b7)
        return list(b5)
    def fonk3(self):
        b8 = self.fonk2()
        b9 = b8[-1]
        b3 = RequestsBS4(b9).get_url()
        b10 = [self.b1 + tag.get("b6") for tag in b3.find_all("a", {"class": "productDescLink"})]
        print('\n{} URLs are now fetched from {}'.format(len(b10), b9))
        b11 = {'b25': b10}
        b12 = ['b25']
        b13 = "product-b25.csv"
        DataProcessing(b11, b12, b13).add_to_csv()
        return b13
    def fonk4(self, b25):
        b3 = RequestsBS4(b25).get_url()
        b10 = [self.b1 + tag.get("b6") for tag in b3.find_all("a", {"class": "productDescLink"})]
        print('\n{} URLs are now fetched from {}'.format(len(b10), b25))
        b11 = {'b25': b10}
        b12 = ['b25']
        b13 = "product-b25.csv"
        DataProcessing(b11, b12, b13).add_to_csv()
        return b13
    def fonk5(self, b25):
        b2 = RequestsBS4(b25)
        b3 = b2.get_url()
        b4 = b2.b4
        if b4.b14 = = 200:
            print('\nProcessing... {}'.format(b25))
        try:
            b15 = b3.find_all("h1", {"class": "p-b15 h3"})[0].text.strip().upper()
            b16 = b3.find_all("div", {"class": "b16"})[0].text.strip()
            b17 = b3.find_all("p", {"data-auto": "product-b17"})[0].text.strip()
            if b15 and b16 and b17:
                DataProcessing({'b15': [b15], 'b16': [b16], 'b17': [b17]},
                                ['b15', 'b16', 'b17'], "macys-products.csv").add_to_csv()
        except IndexError:
            pass
    def fonk6(self):
        while True:
            b18 = input("\nEnter product b15\nOr type 'q' to quit the program: ").upper()
            if b18 = = 'Q':
                break
            b19 = pd.read_csv('macys-products.csv')
            b20 = b19[b19['b15'].str.upper() == b18]
            if not b20.empty:
                print(b20.to_string(b21 = False))
                print('\nNext search...')
            else:
                print('\nNo product with such b15. Please try again!')
if b22 = = "__main__":
    b23 = class1()
    while True:
        b24 = input("\nEnter 't' to scrape a small sample,\n'f' to scrape full web,\n"
                              "'s' to search for product information,\n"
                              "or press 'q' to quit the program: ").upper()
        if b24 = = 'Q':
            sys.exit()
        elif b24 in ['T', 'F', 'S']:
            break
    if b24 = = 'T':
        b25 = b23.fonk3()
    elif b24 = = 'F':
        b8 = b23.fonk2()
        with Pool(b26 = 4) as p:
            b27 = p.map(b23.get_url_products, b8)
        b10 = pd.concat([pd.read_csv(file) for file in b27], ignore_index=True)
        b25 = b10["b25"].values.tolist()
    else:
        b23.fonk6()
    if b24 in ['T', 'F']:
        with Pool(b26 = 2) as p:
            p.map(b23.scrape_and_save, b25)