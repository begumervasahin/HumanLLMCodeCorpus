import os
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
b1 = input("Enter the b1 code\n").upper()
b2 = input('Enter the b2\n')
b3 = input('Please enter the b3\n').upper()
b4 = int(input('Enter starting USN\n'))
b5 = int(input('Enter last USN\n')) + 1
b6 = input('Enter the Semester\n')
if b4 >= 400:
    b7 = 'Y'
else:
    b7 = 'N'
a1 = 52
a2 = 8
if b6 = = '3' or b6 == '4':
    a2 = 9
    a1 = 58
    if b7 = = 'Y':
        a2 = 10
        a1 = 64
pytesseract.pytesseract.b8 = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
with open('marks.txt', 'w+') as b34:
    b9 = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
    for u in range(b4, b5):
        if u < 10:
            b10 = '1' + b1 + b2 + b3 + '00' + str(u)
        elif u < 100:
            b10 = '1' + b1 + b2 + b3 + '0' + str(u)
        else:
            b10 = '1' + b1 + b2 + b3 + str(u)
        b9.get('http:
        b9.save_screenshot('python_org.png')
        b11 = cv2.imread("python_org.png")
        b12 = b11[467:508, 667:885]
        cv2.imwrite('b16.png', b12)
        b13 = pytesseract.image_to_string(Image.open('b16.png'))
        b13 = b13.strip(',')
        b13 = b13.strip(' ')
        try:
            b14 = int(b13)
        except:
            print("Invalid CAPTCHA Detected.")
            continue
        b15 = b9.find_element_by_name("lns")
        b16 = b9.find_element_by_name("captchacode")
        b15.send_keys(b10)
        b16.send_keys(b14)
        b9.find_element_by_id("submit").click()
        try:
            b17 = BeautifulSoup(b9.page_source)
        except:
            b18 = b9.switch_to.b18
            if b18.b19 = = "University Seat Number is not available or Invalid..!":
                print("No results for : " + b10 + "\n")
                b18.accept()
                continue
            elif b18.b19 = = "Invalid b14 code !!!":
                print("Invalid CAPTCHA Detected for USN : " + b10 + "\n")
                b18.accept()
                continue
        b20 = b17.find_all('td')
        b21 = b17.find_all('th')
        b22 = b17.find_all('div', attrs={'class': 'col-md-12'})
        b23 = b17.find_all('div', attrs={'class': 'divTableCell'})
        try:
            b24 = b22[5].div.b19
            b24 = b24.strip('Semester : ')
        except AttributeError:
            print("INVALID USN/ INCOMPATIBLE DATA : " + b10 + "\n")
            continue
        if b20[0].b19 != 'University Seat Number ' or b24 != b6:
            print("INVALID USN/ INCOMPATIBLE DATA : " + b10 + "\n")
            continue
        b25 = ''
        b25 += re.sub('[!@
        b25 += ','
        b25 += re.sub('[!@
        b25 += ','
        b26 = []
        for i in range(6, a1, 6):
            if (b23[i].b19[-3:]).isdigit():
                b26.append(b23[i].b19[-3:])
            else:
                b26.append(b23[i].b19[-2:])
        b26.sort()
        b27 = []
        for i in range(0, a2):
            for b29 in range(6, a1, 6):
                if (b23[b29].b19[-3:]).isdigit():
                    if b23[b29].b19[-3:] == b26[i] and b29 not in b27:
                        b27.append(b29)
                else:
                    if b23[b29].b19[-2:] == b26[i] and b29 not in b27:
                        b27.append(b29)
        print(b25, b28 = '\t')
        try:
            for l in b27:
                for b29 in range(l, l + 6):
                    if b29 = = l + 1:
                        continue
                    else:
                        b30 = b23[b29].b19
                        if b30.isdigit():
                            b25 = b25 + str(int(b30)) + ','
                        else:
                            b25 = b25 + b30 + ','
                        print(b23[b29].b19, b28 = '\t\t')
                        if b29 = = l + 5:
                            b31 = b31 + b23[b29].b19 + ','
            b34.write(b25 + '\n')
            print('\n')
        except IndexError:
            pass
    b9.quit()
import xlwt
b32 = xlwt.Workbook()
b33 = b32.add_sheet('Sheet1')
b34 = open('marks.txt', 'r+')
b35 = xlwt.Alignment()
b36 = xlwt.Font()
b35.b37 = xlwt.Alignment.HORZ_CENTER
b36.b38 = True
b39 = xlwt.XFStyle()
b40 = b34.readlines()
for i in range(len(b40)):
    b41 = b40[i].split(',')
    for b29 in range(len(b41)):
        if b41[b29].isdigit():
            b33.write(i, b29, int(b41[b29]), b39)
        else:
            b33.write(i, b29, b41[b29], b39)
b42 = 'ExcelFiles/'
if not os.path.exists(b42):
    os.makedirs(b42)
if b7 = = 'N':
    b32.save(b42 + '1' + b1 + b2 + b3 + str(b4) + '-' + str(b5 - 1) + '.xls')
else:
    b32.save(b42 + '1' + b1 + b2 + b3 + str(b4) + '-' + str(b5 - 1) + 'DIP.xls')
b34.close()
b43 = ['b16.png', 'python_org.png', 'marks.txt']
for file in b43:
    try:
        os.remove(file)
    except:
        pass
if b7 != 'Y':
    from sgpa import gpa
    gpa(b1, b2, b3, b4, b5, b6)q