import os
import cv2
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
import xlwt
pytesseract.pytesseract.b1 = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
def fonk1():
    b2 = input("Enter the b2 code: ").upper()
    b3 = input('Enter the b3: ')
    b4 = input('Please enter the b4: ').upper()
    b5 = int(input('Enter starting USN: '))
    b6 = int(input('Enter last USN: ')) + 1
    b7 = input('Enter the Semester: ')
    return b2, b3, b4, b5, b6, b7
def fonk2(b5):
    return 'Y' if b5 >= 400 else 'N'
def fonk3(b2, b3, b4, u):
    if u < 10:
        return '1' + b2 + b3 + b4 + '00' + str(u)
    elif u < 100:
        return '1' + b2 + b3 + b4 + '0' + str(u)
    else:
        return '1' + b2 + b3 + b4 + str(u)
def fonk4(b26):
    b26.save_screenshot('python_org.png')
    b8 = cv2.imread("python_org.png")
    b9 = b8[467:508, 667:885]
    cv2.imwrite('cap.png', b9)
    cv2.waitKey(0)
    b10 = pytesseract.image_to_string(Image.open('cap.png')).strip(',').strip(' ')
    try:
        b11 = int(b10)
    except ValueError:
        print("Invalid CAPTCHA Detected.")
        return fonk4(b26)
    return b11
def fonk5(b26, b5, b6, b7, a1, a2):
    with open('marks.txt', 'w+') as f:
        for u in range(b5, b6):
            b12 = True
            while b12:
                b12 = False
                b13 = fonk3(b2, b3, b4, u)
                b26.get('http:
                b11 = fonk4(b26)
                b14 = b26.find_element_by_name("lns")
                b15 = b26.find_element_by_name("captchacode")
                b14.send_keys(b13)
                b15.send_keys(b11)
                b26.find_element_by_id("submit").click()
                try:
                    b16 = BeautifulSoup(b26.page_source, 'html.parser')
                except:
                    b17 = b26.switch_to.b17
                    if b17.b18 = = "University Seat Number is not available or Invalid..!":
                        print("No results for: " + b13 + "\n")
                        b17.accept()
                        continue
                    elif b17.b18 = = "Invalid b11 code !!!":
                        print("Invalid CAPTCHA Detected for USN: " + b13 + "\n")
                        b17.accept()
                        b12 = True
                        continue
        b26.quit()
def fonk6():
    b19 = xlwt.Workbook()
    b20 = b19.add_sheet('Sheet1')
    with open('marks.txt', 'r+') as f:
        for i, line in enumerate(f.readlines()):
            b21 = line.split(',')
            for j, item in enumerate(b21):
                if item.isdigit():
                    b20.write(i, j, int(item))
                else:
                    b20.write(i, j, item)
    b22 = 'ExcelFiles/'
    if not os.path.exists(b22):
        os.makedirs(b22)
    b23 = '1' + b2 + b3 + b4 + str(b5) + '-' + str(b6 - 1)
    if b24 = = 'Y':
        b23 += 'DIP'
    b23 += '.xls'
    b19.save(os.path.join(b22, b23))
def fonk7():
    b25 = ['cap.png', 'python_org.png', 'marks.txt']
    for file in b25:
        try:
            os.remove(file)
        except FileNotFoundError:
            pass
def fonk8():
    b2, b3, b4, b5, b6, b7 = fonk1()
    b24 = fonk2(b5)
    a1 = 52
    a2 = 8
    if b7 = = '3' or b7 == '4':
        a2 = 9
        a1 = 58
        if b24 = = 'Y':
            a2 = 10
            a1 = 64
    b26 = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
    fonk5(b26, b5, b6, b7, a1, a2)
    fonk6()
    fonk7()
    if b24 != 'Y':
        from sgpa import gpa
        gpa(b2, b3, b4, b5, b6, b7)
if b27 = = "__main__":
    fonk8()