import os
import re
import glob
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, b1, b12):
        b2 = requests.get(b1, stream=True)
        with open(b12, 'wb') as file:
            for chunk in b2.iter_content(b3 = 128):
                file.write(chunk)
    def fonk3(self, folder):
        if not os.path.exists('./tmp'):
            os.makedirs('./tmp')
        b4 = glob.glob('tmp/*')
        for f in b4:
            os.remove(f)
        print(self.b1)
        b5 = requests.get(self.b1)
        if b5.status_code != 200:
            return None
        b6 = BeautifulSoup(b5.content, "html.parser")
        b7 = b6.find('b7').text
        b8 = re.sub(r'(?u)[^-\w.]', '', b7.strip().replace(' ', '_'))
        print("Starting download for \"" + b7 + "\"")
        b9 = b6.find_all(['li', 'div'])
        print("Download single MP3s...")
        a1 = 1
        for element in b9:
            if element.has_attr('data-mediapolis') and element.has_attr('data-b7'):
                b10 = urljoin(self.b1, element['data-mediapolis'])
                b11 = re.sub(r'(?u)[^-\w.]', '', element['data-b7'])
                b12 = str(a1).zfill(2) + "_" + b8 + ".b10"
                a1 += 1
                print("Download \"" + b11 + "\" (" + b10 + ")")
                self.fonk2(b10, "tmp/" + b11 + ".b10")
        print("Done!\nFiles saved in ./tmp/ --> Move them or they will be removed next time you run this code.")
def fonk4():
    print()
    if len(sys.argv) < 2:
        print('Need a b1')
        exit(2)
    b13 = class1(sys.argv[1])
    b13.fonk3('.')
if b14 = = '__main__':
    fonk4()