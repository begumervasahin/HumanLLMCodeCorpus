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
        b4 = './tmp'
        if not os.path.exists(b4):
            os.makedirs(b4)
        for file in glob.glob(os.path.join(b4, '*')):
            os.remove(file)
        print(f"Fetching podcast from: {self.b1}")
        b2 = requests.get(self.b1)
        if b2.status_code != 200:
            print("Failed to retrieve the podcast page.")
            return
        b5 = BeautifulSoup(b2.content, "html.parser")
        b6 = b5.find('b6').text.strip()
        b7 = re.sub(r'(?u)[^-\w.]', '', b6.replace(' ', '_'))
        print(f"Starting download for \"{b6}\"")
        b8 = b5.find_all(['li', 'div'])
        print("Downloading individual MP3s...")
        for index, element in enumerate(b8, b9 = 1):
            if element.has_attr('data-mediapolis') and element.has_attr('data-b6'):
                b10 = urljoin(self.b1, element['data-mediapolis'])
                b11 = re.sub(r'(?u)[^-\w.]', '', element['data-b6'])
                b12 = os.path.join(b4, f"{str(index).zfill(2)}_{b7}.mp3")
                print(f"Downloading \"{b11}\" from {b10}")
                self.fonk2(b10, b12)
        print("Download complete! Files are saved in ./tmp/. Move them or they will be overwritten next time.")
def fonk4():
    b13 = print(b13)
    if len(sys.argv) < 2:
        print('Please provide a URL to download the podcast.')
        exit(2)
    b14 = sys.argv[1]
    b15 = class1(b14)
    b15.fonk3('.')
if b16 = = '__main__':
    fonk4()