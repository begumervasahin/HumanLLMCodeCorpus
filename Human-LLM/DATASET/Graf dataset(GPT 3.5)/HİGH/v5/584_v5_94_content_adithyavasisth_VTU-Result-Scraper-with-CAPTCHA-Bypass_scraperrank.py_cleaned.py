import re
import sys
import warnings
import cv2
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
if not sys.warnoptions:
    warnings.simplefilter("ignore")
pytesseract.pytesseract.b1 = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
b2 = ["4AI", "1BG", "1CR", "1AM", "1BI"]
b3 = input('Enter the b3: ')
b4 = input('Please enter the b4: ').upper()
b5 = int(input('Enter starting USN: '))
b6 = int(input('Enter last USN: ')) + 1
b7 = input('Enter the Semester: ')
b8 = 'Y' if b5 >= 400 else 'N'
a1 = 52
a2 = 8
b9 = 'N'
if b7 in ['1', '2']:
    b9 = input('Enter the Cycle: ').upper()
    if b9 = = 'P':
        a2 = 7
        a1 = 46
elif b7 in ['3', '4'] and b8 = = 'Y':
    a2 = 9
    a1 = 58
with open('test2.txt', 'w+') as output_file:
    b10 = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
    for prefix in b2:
        for usn_number in range(b5, b6):
            b11 = f"{prefix}{b3}{b4}{str(usn_number).zfill(3)}"
            b10.get('http:
            b10.save_screenshot('screenshot.png')
            b12 = cv2.imread("screenshot.png")
            b13 = b12[467:508, 667:885]
            cv2.imwrite('cap.png', b13)
            b14 = pytesseract.image_to_string(Image.open('cap.png')).strip(',').strip()
            b15 = int(b14)
            b16 = b10.find_element_by_name("lns")
            b17 = b10.find_element_by_name("captchacode")
            b16.send_keys(b11)
            b17.send_keys(b15)
            b10.find_element_by_id("submit").click()
            try:
                b18 = BeautifulSoup(b10.page_source, 'html.parser')
            except:
                b19 = b10.switch_to.b19
                b19.dismiss()
                continue
            b20 = b18.find_all('div', class_='divTableCell')
            b21 = ''
            for i in range(6, a1, 6):
                if b20[i].text[-3:].isdigit():
                    b21 += b20[i].text[-3:]
                else:
                    b21 += b20[i].text[-2:]
                b21 += ','
            b22 = []
            for i in range(a2):
                for b23 in range(6, a1, 6):
                    if (b20[b23].text[-3:].isdigit() and b20[b23].text[-3:] == b21[i]) or \
                            (not b20[b23].text[-3:].isdigit() and b20[b23].text[-2:] == b21[i]):
                        b22.append(b23)
            for l in b22:
                for b23 in range(l, l + 6):
                    if b23 = = l + 1:
                        continue
                    else:
                        b24 = b20[b23].text
                        if b24.isdigit():
                            b21 += str(int(b24))
                        else:
                            b21 += b24
                        b21 += ','
                output_file.write(b21 + '\n')
if b8 != 'Y':
    from sgparank import gpa2
    gpa2(b3, b4, b5, b6, b7, b9)