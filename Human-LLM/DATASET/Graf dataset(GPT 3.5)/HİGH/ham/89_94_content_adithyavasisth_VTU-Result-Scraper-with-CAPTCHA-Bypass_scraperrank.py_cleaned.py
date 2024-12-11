import re
import sys
import warnings
import cv2
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
pytesseract.pytesseract.b1 = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
if not sys.warnoptions:
    warnings.simplefilter("ignore")
b2 = ["4AI", "1BG", "1CR", "1AM", "1BI"]
b3 = input('Enter the b3\n')
b4 = input('Please enter the b4\n').upper()
b5 = int(input('Enter starting USN\n'))
if b5 >= 400:
    b6 = 'Y'
else:
    b6 = 'N'
b7 = int(input('Enter last USN\n')) + 1
b8 = input('Enter the Semester\n')
b9 = 'N'
if b5 >= 400:
    b6 = 'Y'
else:
    b6 = 'N'
a1 = 52
a2 = 8
if b8 = = '1' or b8 == '2':
    b9 = input('Enter the Cycle\n').upper()
    if b9 = = 'P':
        a2 = 7
        a1 = 46
if b8 = = '3' or b8 == '4':
    if b6 = = 'Y':
        a2 = 9
        a1 = 58
with open('test2.txt', 'w+') as f:
    a3 = 0
    b10 = ''
    b11 = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
    for x in b2:
        for u in range(b5, b7):
            if u < 10:
                b12 = x + b3 + b4 + '00' + str(u)
            elif u < 100:
                b12 = x + b3 + b4 + '0' + str(u)
            else:
                b12 = x + b3 + b4 + str(u)
            b11.get('http:
            b11.save_screenshot('python_org.png')
            b13 = cv2.imread("python_org.png")
            b14 = b13[467:508, 667:885]
            cv2.imwrite('b18.png', b14)
            cv2.waitKey(0)
            b15 = pytesseract.image_to_string(Image.open('b18.png'))
            b15 = b15.strip(',')
            b15 = b15.strip(' ')
            b16 = int(b15)
            b17 = b11.find_element_by_name("lns")
            b18 = b11.find_element_by_name("captchacode")
            b17.send_keys(b12)
            b18.send_keys(b16)
            b11.find_element_by_id("submit").click()
            try:
                b19 = BeautifulSoup(b11.page_source)
            except:
                b20 = b11.switch_to.b20
                b20.dismiss()
                continue
            b21 = b19.find_all('td')
            b22 = b19.find_all('th')
            b23 = b19.find_all('div', attrs={'class': 'col-md-12'})
            b24 = b19.find_all('div', attrs={'class': 'divTableCell'})
            b25 = ''
            b25 += re.sub('[!@
            b25 += ','
            b25 += re.sub('[!@
            b25 += ','
            b26 = []
            for i in range(6, a1, 6):
                if (b24[i].text[-3:]).isdigit():
                    b26.append(b24[i].text[-3:])
                else:
                    b26.append(b24[i].text[-2:])
            b26.sort()
            b27 = []
            for i in range(0, a2):
                for b29 in range(6, a1, 6):
                    if (b24[b29].text[-3:]).isdigit():
                        if b24[b29].text[-3:] == b26[i] and b29 not in b27:
                            b27.append(b29)
                    else:
                        if b24[b29].text[-2:] == b26[i] and b29 not in b27:
                            b27.append(b29)
            print(b25, b28 = '\t')
            try:
                for l in b27:
                    for b29 in range(l, l + 6):
                        if b29 = = l + 1:
                            continue
                        else:
                            b30 = b24[b29].text
                            if b30.isdigit():
                                b25 = b25 + str(int(b30)) + ','
                            else:
                                b25 = b25 + b30 + ','
                            print(b24[b29].text, b28 = '\t\t')
                            if b29 = = l + 5:
                                b10 = b10 + b24[b29].text + ','
                f.write(b25 + '\n')
                print('\n')
            except IndexError:
                pass
if b6 != 'Y':
    from sgparank import gpa2
    gpa2(b3, b4, b5, b7, b8, b9)