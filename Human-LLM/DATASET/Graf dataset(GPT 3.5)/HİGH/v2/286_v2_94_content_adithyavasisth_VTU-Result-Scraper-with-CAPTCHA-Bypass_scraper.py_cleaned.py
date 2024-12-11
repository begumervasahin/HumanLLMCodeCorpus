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
with open('marks.txt', 'w+') as b34:
    b9 = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
    for u in range(b5, b6):
        b10 = True
        while b10:
            b10 = False
            if u < 10:
                b11 = '1' + b2 + b3 + b4 + '00' + str(u)
            elif u < 100:
                b11 = '1' + b2 + b3 + b4 + '0' + str(u)
            else:
                b11 = '1' + b2 + b3 + b4 + str(u)
            b9.get('http:
            b9.save_screenshot('python_org.png')
            b12 = cv2.imread("python_org.png")
            b13 = b12[467:508, 667:885]
            cv2.imwrite('cap.png', b13)
            cv2.waitKey(0)
            b14 = pytesseract.image_to_string(Image.open('cap.png'))
            b14 = b14.strip(',').strip(' ')
            try:
                b15 = int(b14)
            except ValueError:
                print("Invalid CAPTCHA Detected.")
                b10 = True
                continue
            b16 = b9.find_element_by_name("lns")
            b17 = b9.find_element_by_name("captchacode")
            b16.send_keys(b11)
            b17.send_keys(b15)
            b9.find_element_by_id("submit").click()
            try:
                b18 = BeautifulSoup(b9.page_source, 'html.parser')
            except:
                b19 = b9.switch_to.b19
                if b19.b20 = = "University Seat Number is not available or Invalid..!":
                    print("No results for: " + b11 + "\n")
                    b19.accept()
                    continue
                elif b19.b20 = = "Invalid b15 code !!!":
                    print("Invalid CAPTCHA Detected for USN: " + b11 + "\n")
                    b19.accept()
                    b10 = True
                    continue
            b21 = b18.find_all('td')
            b22 = b18.find_all('th')
            b23 = b18.find_all('div', attrs={'class': 'col-md-12'})
            b24 = b18.find_all('div', attrs={'class': 'divTableCell'})
            try:
                b25 = b23[5].div.b20.strip('Semester: ')
            except AttributeError:
                print("INVALID USN/ INCOMPATIBLE DATA: " + b11 + "\n")
                continue
            if b21[0].b20 != 'University Seat Number ' or b25 != b7:
                print("INVALID USN/ INCOMPATIBLE DATA: " + b11 + "\n")
                continue
            b26 = b22[2].b20 + ',' + b22[3].b20 + ','
            b27 = [b24[i].b20[-3:] if b24[i].b20[-3:].isdigit() else b24[i].b20[-2:] for i in range(6, a1, 6)]
            b27.sort()
            b28 = []
            for i in range(0, a2):
                for b30 in range(6, a1, 6):
                    if (b24[b30].b20[-3:] if b24[b30].b20[-3:].isdigit() else b24[b30].b20[-2:]) == b27[i] and b30 not in b28:
                        b28.append(b30)
            print(b26, b29 = '\t')
            try:
                for l in b28:
                    for b30 in range(l, l + 6):
                        if b30 = = l + 1:
                            continue
                        else:
                            b31 = b24[b30].b20
                            b26 += str(int(b31)) + ',' if b31.isdigit() else b31 + ','
                            print(b24[b30].b20, b29 = '\t\t')
                            if b30 = = l + 5:
                                pf += b24[b30].b20 + ','
                b34.write(b26 + '\n')
                print('\n')
            except IndexError:
                pass
    b9.quit()
b32 = xlwt.Workbook()
b33 = b32.add_sheet('Sheet1')
b34 = open('marks.txt', 'r+')
for i, line in enumerate(b34.readlines()):
    b35 = line.split(',')
    for b30, item in enumerate(b35):
        if item.isdigit():
            b33.write(i, b30, int(item))
        else:
            b33.write(i, b30, item)
b36 = 'ExcelFiles/'
if not os.path.exists(b36):
    os.makedirs(b36)
b37 = '1' + b2 + b3 + b4 + str(b5) + '-' + str(b6 - 1)
if b8 = = 'Y':
    b37 += 'DIP'
b37 += '.xls'
b32.save(os.path.join(b36, b37))
b34.close()
b38 = ['cap.png', 'python_org.png', 'marks.txt']
for file in b38:
    try:
        os.remove(file)
    except FileNotFoundError:
        pass
if b8 != 'Y':
    from sgpa import gpa
    gpa(b2, b3, b4, b5, b6, b7)