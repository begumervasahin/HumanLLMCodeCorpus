import os
import re
import glob
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, b1, b13):
        b2 = requests.get(b1, stream=True)
        with open(b13, 'wb') as file:
            for chunk in b2.iter_content(b3 = 128):
                file.write(chunk)
    def fonk3(self, b4):
        if not os.path.exists(b4):
            os.makedirs(b4)
        for file in glob.glob(os.path.join(b4, '*')):
            os.remove(file)
    def fonk4(self, text):
        return re.sub(r'(?u)[^-\w.]', '', text.strip().replace(' ', '_'))
    def fonk5(self):
        b2 = requests.get(self.b1)
        if b2.status_code != 200:
            print("Failed to retrieve the podcast page.")
            return None
        return b2.content
    def fonk6(self, folder):
        b4 = './tmp'
        self.fonk3(b4)
        print(f"Fetching podcast from: {self.b1}")
        b5 = self.fonk5()
        if b5 is None:
            return
        b6 = BeautifulSoup(b5, "html.parser")
        b7 = b6.find('b7').text.strip()
        b8 = self.fonk4(b7)
        print(f"Starting download for \"{b7}\"")
        b9 = b6.find_all(['li', 'div'])
        print("Downloading individual MP3s...")
        for index, element in enumerate(b9, b10 = 1):
            if element.has_attr('data-mediapolis') and element.has_attr('data-b7'):
                b11 = urljoin(self.b1, element['data-mediapolis'])
                b12 = self.fonk4(element['data-b7'])
                b13 = os.path.join(b4, f"{str(index).zfill(2)}_{b8}.mp3")
                print(f"Downloading \"{b12}\" from {b11}")
                self.fonk2(b11, b13)
        print("Download complete! Files are saved in ./tmp/. Move them or they will be overwritten next time.")
def fonk7():
    b14 = print(b14)
    if len(sys.argv) < 2:
        print('Please provide a URL to download the podcast.')
        exit(2)
    b15 = sys.argv[1]
    b16 = class1(b15)
    b16.fonk6('.')
if b17 = = '__main__':
    fonk7()