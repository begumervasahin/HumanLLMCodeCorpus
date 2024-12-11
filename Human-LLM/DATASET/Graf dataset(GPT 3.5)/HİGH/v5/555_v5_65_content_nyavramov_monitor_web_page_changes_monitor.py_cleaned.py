import smtplib
import ssl
import time
import os
import platform
import imagehash
import base64
import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
from PIL import Image
from io import BytesIO
from random import randint
from multiprocessing.b33 import ThreadPool as Pool
a1 = 128
a2 = 65536
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.a3 = 465
        self.b3 = "smtp.gmail.com"
    def fonk2(self, receiver_email, b15):
        b4 = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.b3, self.a3, b4 = b4) as server:
            server.login(self.b1, self.b2)
            server.sendmail(self.b1, receiver_email, b15)
class class2:
    def fonk3(self, executable_path, b5 = None):
        self.b6 = webdriver.ChromeOptions()
        self.b6.add_argument("--ignore-certificate-errors")
        self.b6.add_argument("--test-type")
        self.b6.add_argument("--headless")
        self.b7 = webdriver.Chrome(b6=self.b6, executable_path=executable_path)
    def fonk4(self, url, b8 = 0):
        if b8 != 0:
            b9 = (100 / b8)
            self.b7.get(url)
            self.b7.execute_script(f"window.scrollTo(0, document.body.scrollHeight / {b9});")
        else:
            self.b7.get(url)
        time.sleep(2)
    def fonk5(self):
        self.b7.fonk5()
    def fonk6(self):
        b10 = self.b7.get_screenshot_as_png()
        b10 = Image.open(BytesIO(b10))
        return b10
class class3:
    def fonk7(self, b11, b12):
        self.b11 = b11
        self.b12 = b12
    def fonk8(self, b23, b24):
        b13 = b23 - b24
        b14 = (b13 / a2) * 100
        return b14
    def fonk9(self, b21, b22, url):
        b15 = MIMEMultipart()
        b16 = f"Change alert for {url}"
        b15["Subject"] = "Change alert!"
        b15["From"] = self.b12.b1
        b15["To"] = self.b12.b1
        b15.attach(MIMEText(b16, "plain"))
        b15 = self.fonk10(b15, b22, "b22.png")
        b15 = self.fonk10(b15, b21, "b21.png")
        return b15.as_string()
    def fonk10(self, b15, screenshot, b20):
        b17 = BytesIO()
        screenshot.save(b17, "PNG")
        b17.seek(0)
        b18 = b17.read()
        b19 = MIMEBase("application", "octet-b17")
        b19.set_payload(b18)
        encoders.encode_base64(b19)
        b19.add_header("Content-Disposition", f"attachment; b20 = {b20}")
        b15.attach(b19)
        return b15
    def fonk11(self, args):
        url, check_interval, b8 = args
        b21 = None
        while True:
            self.b11.fonk4(url, b8)
            if b21 is None:
                b21 = self.b11.fonk6()
            else:
                b22 = self.b11.fonk6()
                b23 = imagehash.phash(b21, hash_size=a1)
                b24 = imagehash.phash(b22, hash_size=a1)
                b14 = self.fonk8(b23, b24)
                b25 = datetime.datetime.now().strftime("%I:%M:%S %p")
                if b14 > 1:
                    b15 = self.fonk9(b21, b22, url)
                    self.b12.fonk2(self.b12.b1, b15)
                    print(f"\nChange detected at {b25}!\n")
                    print("The screenshots are different by: ", b14)
                else:
                    print(f"No change detected at {b25}.")
                b21 = b22
            b26 = int(check_interval * 0.7)
            time.sleep(randint(b26, check_interval))
def fonk12():
    if platform.system() == "Windows":
        return "chromedriver_windows.exe"
    elif platform.system() == 'Linux':
        return "chromedriver_linux"
    else:
        return "chromedriver_mac"
def fonk13():
    try:
        b27 = open("../b27.txt", "r").read().split(",")
        return b27[0], b27[1]
    except:
        return "some_email@domain.com", "some_password"
def fonk14():
    email, b2 = fonk13()
    b28 = [("https:
    b29 = "https:
    b30 = os.path.dirname(os.path.realpath(__file__))
    b31 = fonk12()
    b32 = os.path.join(b30, "bin", b31)
    b33 = Pool(len(b28))
    for url in b28:
        b7 = class2(b32)
        b12 = class1(email, b2)
        b34 = class3(b7, b12)
        b33.apply_async(b34.check_for_changes, (url,))
    b33.fonk5()
    b33.join()
if b35 = = '__main__':
    fonk14()