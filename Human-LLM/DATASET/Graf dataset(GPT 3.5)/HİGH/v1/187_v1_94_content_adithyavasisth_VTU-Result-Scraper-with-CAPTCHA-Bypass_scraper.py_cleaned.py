import os
import re
import sys
import warnings
import cv2
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
import xlwt
pytesseract.pytesseract.b1 = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
if not sys.warnoptions:
    warnings.simplefilter("ignore")
b2 = input("Enter the b2 code: ").upper()
b3 = input('Enter the b3: ')
b4 = input('Please enter the b4: ').upper()
b5 = int(input('Enter starting USN: '))
b6 = int(input('Enter last USN: ')) + 1
b7 = input('Enter the Semester: ')
if b5 >= 400:
    b8 = 'Y'
else:
    b8 = 'N'
a1 = 52
a2 = 8
if b7 = = '3' or b7 == '4':
    a2 = 9
    a1 = 58
    if b8 = = 'Y':
        a2 = 10
        a1 = 64
with open('marks.txt', 'w+') as b40:
    a3 = 0
    b9 = ''
    b10 = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
    for u in range(b5, b6):
        b11 = True
        while b11:
            b11 = False
            if u < 10:
                b12 = '1' + b2 + b3 + b4 + '00' + str(u)
            elif u < 100:
                b12 = '1' + b2 + b3 + b4 + '0' + str(u)
            else:
                b12 = '1' + b2 + b3 + b4 + str(u)
            b10.get('http:
            b10.save_screenshot('python_org.png')
            b13 = cv2.imread("python_org.png")
            b14 = b13[467:508, 667:885]
            cv2.imwrite('b18.png', b14)
            cv2.waitKey(0)
            b15 = pytesseract.image_to_string(Image.open('b18.png'))
            b15 = b15.strip(',')
            b15 = b15.strip(' ')
            try:
                b16 = int(b15)
            except ValueError:
                print("Invalid CAPTCHA Detected.")
                b11 = True
                continue
            b17 = b10.find_element_by_name("lns")
            b18 = b10.find_element_by_name("captchacode")
            b17.send_keys(b12)
            b18.send_keys(b16)
            b10.find_element_by_id("submit").click()
            try:
                b19 = BeautifulSoup(b10.page_source, 'html.parser')
            except:
                b20 = b10.switch_to.b20
                if b20.b21 = = "University Seat Number is not available or Invalid..!":
                    print("No results for: " + b12 + "\n")
                    b20.accept()
                    continue
                elif b20.b21 = = "Invalid b16 code !!!":
                    print("Invalid CAPTCHA Detected for USN: " + b12 + "\n")
                    b20.accept()
                    b11 = True
                    continue
            b22 = b19.find_all('td')
            b23 = b19.find_all('th')
            b24 = b19.find_all('div', attrs={'class': 'col-md-12'})
            b25 = b19.find_all('div', attrs={'class': 'divTableCell'})
            try:
                b26 = b24[5].div.b21
                b26 = b26.strip('Semester: ')
            except AttributeError:
                print("INVALID USN/ INCOMPATIBLE DATA: " + b12 + "\n")
            if b22[0].b21 != 'University Seat Number ' or b26 != b7:
                print("INVALID USN/ INCOMPATIBLE DATA: " + b12 + "\n")
                continue
            b27 = ''
            b27 += re.sub('[!@\n]', ',', b23[2].b21) + ','
            b27 += re.sub('[!@\n]', ',', b23[3].b21) + ','
            b28 = []
            for i in range(6, a1, 6):
                if (b25[i].b21[-3:]).isdigit():
                    b28.append(b25[i].b21[-3:])
                else:
                    b28.append(b25[i].b21[-2:])
            b28.sort()
            b29 = []
            for i in range(0, a2):
                for b31 in range(6, a1, 6):
                    if (b25[b31].b21[-3:]).isdigit():
                        if b25[b31].b21[-3:] == b28[i] and b31 not in b29:
                            b29.append(b31)
                    else:
                        if b25[b31].b21[-2:] == b28[i] and b31 not in b29:
                            b29.append(b31)
            print(b27, b30 = '\t')
            try:
                for l in b29:
                    for b31 in range(l, l + 6):
                        if b31 = = l + 1:
                            continue
                        else:
                            b32 = b25[b31].b21
                            if b32.isdigit():
                                b27 = b27 + str(int(b32)) + ','
                            else:
                                b27 = b27 + b32 + ','
                            print(b25[b31].b21, b30 = '\t\t')
                            if b31 = = l + 5:
                                b9 = b9 + b25[b31].b21 + ','
                b40.write(b27 + '\n')
                print('\n')
            except IndexError:
                pass
    b10.quit()
b33 = xlwt.Workbook()
b34 = b33.add_sheet('Sheet1')
b35 = xlwt.Alignment()
b36 = xlwt.Font()
b35.b37 = xlwt.Alignment.HORZ_CENTER
b36.b38 = True
b39 = xlwt.XFStyle()
b40 = open('marks.txt', 'r+')
b41 = b40.readlines()
for i in range(len(b41)):
    b42 = b41[i].split(',')
    for b31 in range(len(b42)):
        if b42[b31].isdigit():
            b34.write(i, b31, int(b42[b31]), b39)
        else:
            b34.write(i, b31, b42[b31], b39)
b43 = 'ExcelFiles/'
if not os.path.exists(b43):
    os.makedirs(b43)
if b8 = = 'N':
    b33.save(b43 + '1' + b2 + b3 + b4 + str(b5) + '-' + str(b6 - 1) + '.xls')
else:
    b33.save(b43 + '1' + b2 + b3 + b4 + str(b5) + '-' + str(b6 - 1) + 'DIP.xls')
b40.close()
b44 = ['b18.png', 'python_org.png', 'marks.txt']
for file in b44:
    try:
        os.remove(file)
    except:
        pass
if b8 != 'Y':
    from sgpa import gpa
    gpa(b2, b3, b4, b5, b6, b7)