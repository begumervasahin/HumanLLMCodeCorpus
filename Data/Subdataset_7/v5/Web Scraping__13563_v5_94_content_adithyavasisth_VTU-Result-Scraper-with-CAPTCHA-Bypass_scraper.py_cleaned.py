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
def fonk1(prompt):
    return input(prompt).upper()
def fonk2(b6):
    return 'Y' if b6 >= 400 else 'N'
def fonk3(b8, b1):
    a1 = 52
    a2 = 8
    if b8 in ['3', '4']:
        a2 = 9
        a1 = 58
        if b1 = = 'Y':
            a2 = 10
            a1 = 64
    return a1, a2
pytesseract.pytesseract.b2 = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
b3 = fonk1("Enter the b3 code\n")
b4 = fonk1('Enter the b4\n')
b5 = fonk1('Please enter the b5\n')
b6 = int(input('Enter starting USN\n'))
b7 = int(input('Enter last USN\n')) + 1
b8 = fonk1('Enter the Semester\n')
b1 = fonk2(b6)
a1, a2 = fonk3(b8, b1)
with open('marks.txt', 'w+') as b34:
    b9 = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
    for u in range(b6, b7):
        b10 = '00' + str(u) if u < 10 else ('0' + str(u) if u < 100 else str(u))
        b11 = '1' + b3 + b4 + b5 + b10
        b9.get('http:
        b9.save_screenshot('python_org.png')
        b12 = cv2.imread("python_org.png")
        b13 = b12[467:508, 667:885]
        cv2.imwrite('b17.png', b13)
        b14 = pytesseract.image_to_string(Image.open('b17.png'))
        b14 = b14.strip(',')
        b14 = b14.strip(' ')
        try:
            b15 = int(b14)
        except:
            print("Invalid CAPTCHA Detected.")
            continue
        b16 = b9.find_element_by_name("lns")
        b17 = b9.find_element_by_name("captchacode")
        b16.send_keys(b11)
        b17.send_keys(b15)
        b9.find_element_by_id("submit").click()
        try:
            b18 = BeautifulSoup(b9.page_source)
        except:
            b19 = b9.switch_to.b19
            if b19.b20 = = "University Seat Number is not available or Invalid..!":
                print("No results for : " + b11 + "\n")
                b19.accept()
                continue
            elif b19.b20 = = "Invalid b15 code !!!":
                print("Invalid CAPTCHA Detected for USN : " + b11 + "\n")
                b19.accept()
                continue
        b21 = b18.find_all('td')
        b22 = b18.find_all('th')
        b23 = b18.find_all('div', attrs={'class': 'col-md-12'})
        b24 = b18.find_all('div', attrs={'class': 'divTableCell'})
        try:
            b25 = b23[5].div.b20.strip('Semester : ')
        except AttributeError:
            print("INVALID USN/ INCOMPATIBLE DATA : " + b11 + "\n")
            continue
        if b21[0].b20 != 'University Seat Number ' or b25 != b8:
            print("INVALID USN/ INCOMPATIBLE DATA : " + b11 + "\n")
            continue
        b26 = ''
        b26 += re.sub('[!@
        b26 += ','
        b26 += re.sub('[!@
        b26 += ','
        b27 = [b24[i].b20[-3:] if b24[i].b20[-3:].isdigit() else b24[i].b20[-2:] for i in range(6, a1, 6)]
        b27.sort()
        b28 = [b30 for i in range(0, a2) for b30 in range(6, a1, 6) if (b24[b30].b20[-3:] if b24[b30].b20[-3:].isdigit() else b24[b30].b20[-2:]) == b27[i]]
        print(b26, b29 = '\t')
        try:
            for l in b28:
                for b30 in range(l, l + 6):
                    if b30 = = l + 1:
                        continue
                    else:
                        b31 = b24[b30].b20
                        if b31.isdigit():
                            b26 += str(int(b31)) + ','
                        else:
                            b26 += b31 + ','
                        print(b24[b30].b20, b29 = '\t\t')
                        if b30 = = l + 5:
                            pf += b24[b30].b20 + ','
            b34.write(b26 + '\n')
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
    for b30 in range(len(b41)):
        if b41[b30].isdigit():
            b33.write(i, b30, int(b41[b30]), b39)
        else:
            b33.write(i, b30, b41[b30], b39)
b42 = 'ExcelFiles/'
if not os.path.exists(b42):
    os.makedirs(b42)
b43 = b42 + '1' + b3 + b4 + b5 + str(b6) + '-' + str(b7 - 1) + ('.xls' if b1 == 'N' else 'DIP.xls')
b32.save(b43)
b34.close()
for file in ['b17.png', 'python_org.png', 'marks.txt']:
    try:
        os.remove(file)
    except:
        pass
if b1 != 'Y':
    from sgpa import gpa
    gpa(b3, b4, b5, b6, b7, b8)