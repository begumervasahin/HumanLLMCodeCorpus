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
from multiprocessing.b35 import ThreadPool as Pool
a1 = 128
a2 = 65536
class class1:
    def fonk1(self, b1, b2):
        self.b1 = b1
        self.b2 = b2
        self.a3 = 465
        self.b3 = "smtp.gmail.com"
    def fonk2(self, receiver_email, b18):
        b4 = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.b3, self.a3, b4 = b4) as server:
            server.login(self.b1, self.b2)
            server.sendmail(self.b1, receiver_email, b18)
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
    def fonk7(self, b10):
        b10.show()
class class3:
    def fonk8(self, chrome_driver, b36):
        self.b7 = chrome_driver
        self.b11 = b36
    def fonk9(self, b10):
        return imagehash.phash(b10, b12 = a1)
    def fonk10(self, b23, b24):
        b13 = self.fonk9(b23)
        b14 = self.fonk9(b24)
        b15 = b13 - b14
        b16 = (b15 / a2) * 100
        return b16
    def fonk11(self, b18, b23, b24, url):
        b17 = f"Change alert for {url}"
        b18["Subject"] = "Change alert!"
        b18["From"] = self.b11.b1
        b18["To"] = self.b11.b1
        b18.attach(MIMEText(b17, "plain"))
        b18 = self.fonk13(b18, b24, "b24.png")
        b18 = self.fonk13(b18, b23, "b23.png")
        return b18.as_string()
    def fonk12(self, url, b23, b24):
        b18 = self.fonk11(MIMEMultipart(), b23, b24, url)
        self.b11.fonk2(self.b11.b1, b18)
    def fonk13(self, b18, file, b22):
        b19 = BytesIO()
        file.save(b19, "PNG")
        b19.seek(0)
        b20 = b19.read()
        b21 = MIMEBase("application", "octet-b19")
        b21.set_payload(b20)
        encoders.encode_base64(b21)
        b21.add_header(
            "Content-Disposition",
            f"attachment; b22 = {b22}",
        )
        b18.attach(b21)
        return b18
    def fonk14(self, args):
        url, check_interval, b8 = args[0], args[1], args[2]
        b23 = None
        b24 = None
        while True:
            self.b7.fonk4(url, b8)
            if b23 is None:
                b23 = self.b7.fonk6()
            else:
                b24 = self.b7.fonk6()
                b25 = self.fonk10(b23, b24)
                b26 = datetime.datetime.now().strftime("%I:%M:%S %p")
                if b25 > 1:
                    self.fonk12(url, b23, b24)
                    print(f"\nChange detected at {b26}!\n")
                    print("The screenshots are different by: ", b25)
                else:
                    print(f"No change detected at {b26}.")
                b23 = b24
            b27 = int(check_interval * 0.7)
            time.sleep(randint(b27, check_interval))
    def fonk15(self, url, b31, b7, b37):
        b7.fonk4(url, 6)
        b23 = b7.fonk6()
        b7.fonk4(b31, 6)
        b24 = b7.fonk6()
        b37.fonk12(url, b23, b24)
def fonk16():
    if platform.system() == "Windows":
        b28 = "chromedriver_windows.exe"
    elif platform.system() == 'Linux':
        b28 = "chromedriver_linux"
    else:
        b28 = "chromedriver_mac"
    return b28
def fonk17():
    try:
        b29 = open("../b29.txt", "r").read().split(",")
        return b29[0], b29[1]
    except:
        return "some_email@domain.com", "some_password"
def fonk18():
    email, b2 = fonk17()
    b30 = [("https:
    b31 = "https:
    b32 = os.path.dirname(os.path.realpath(__file__))
    b33 = fonk16()
    b34 = os.path.join(b32, "bin", b33)
    b35 = Pool(len(b30))
    for url in b30:
        b7 = class2(b34)
        b36 = class1(email, b2)
        b37 = class3(b7, b36)
        b35.apply_async(b37.check_page_for_changes, (url,))
    b35.fonk5()
    b35.join()
if b38 = = '__main__':
    fonk18()