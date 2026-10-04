import os
import re
import glob
import sys
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self, b1, b10):
        os.system(f'wget -O {b10} {b1}')
    def fonk3(self, directory):
        if not os.path.exists(directory):
            os.makedirs(directory)
        for file in glob.glob(f'{directory}/*'):
            os.remove(file)
    def fonk4(self, b4):
        return re.sub(r'(?u)[^-\w.]', '', b4.strip())
    def fonk5(self, folder):
        self.fonk3('./tmp')
        print(f"Processing URL: {self.b1}")
        b2 = requests.get(self.b1)
        if b2.status_code != 200:
            print(f"Failed to retrieve the URL: {self.b1}")
            return
        b3 = BeautifulSoup(b2.content, "html.parser")
        b4 = b3.find('b4').text
        b5 = self.fonk4(b4)
        print(f"Starting download for \"{b4}\"")
        b6 = b3.find_all(['li', 'div'])
        print("Downloading individual MP3s...")
        for element_id, element in enumerate(b6, b7 = 1):
            if element.has_attr('data-mediapolis') and element.has_attr('data-b4'):
                b8 = urljoin(self.b1, element['data-mediapolis'])
                b9 = self.fonk4(element['data-b4'])
                b10 = f"tmp/{str(element_id).zfill(2)}_{b5}.mp3"
                print(f"Downloading \"{b9}\" ({b8})")
                self.fonk2(b8, b10)
        print("Download complete! Files are saved in ./tmp/. Move them to avoid deletion next time the script runs.")
def fonk6():
    print()
    if len(sys.argv) < 2:
        print('A URL is required to proceed.')
        sys.exit(2)
    b11 = class1(sys.argv[1])
    b11.fonk5('.')
if b12 = = '__main__':
    fonk6()