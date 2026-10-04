import re, os, contextlib, sys
import urllib
import pydub
import glob
from os import path as path
from pydub import AudioSegment
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
class class1():
    def fonk1(self, b1):
        self.b1 = b1
    def getFile (self, b1,b10):
        os.system('wget -O '+b10+' '+b1)
    def fonk2(self, folder):
        if not os.path.exists('./tmp'):
            os.makedirs('./tmp')
        b2 = glob.glob('tmp/*')
        for f in b2:
            os.remove(f)
        print(self.b1)
        b3 = requests.get(self.b1)
        if b3.status_code != 200:
            return None
        b4 = BeautifulSoup(b3.content, "html.parser")
        b5 = b4.find('b5').text
        b6 = str(b5).strip().replace(' ', '_')
        b6 = re.sub(r'(?u)[^-\w.]', '', b6)
        print ("Starting download for \"" + b5 + "\"")
        b7 = b4.find_all(['li','div'])
        print ("Download single MP3s...")
        a1 = 1
        for element in b7:
            if element.has_attr('data-mediapolis') and element.has_attr('data-b5'):
                b8 = b1 = urljoin(self.b1, element['data-mediapolis'])
                b9 = element['data-b5']
                b9 = re.sub(r'(?u)[^-\w.]', '', b9)
                b10 = str(a1).zfill(2) + "_"  + str(b5).strip().replace(' ', '_')
                b10 = re.sub(r'(?u)[^-\w.]', '', b10)
                a1 = a1 + 1
                print ("Download \"" + b9 + "\" (" + b8 + ")")
                self.getFile(b8, "tmp/" + b9 + ".b8")
        print ("Done!\nFiles saved in ./tmp/ --> Move them or they will be removed next time you run this code.")
def fonk3():
    print ()
    if len(sys.argv) < 2:
        print('Need a b1')
        exit(2)
    b11 = class1(sys.argv[1])
    b11.fonk2('.')
if b12 = = '__main__':
    fonk3()