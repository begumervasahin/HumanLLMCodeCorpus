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
b8 = 'N'
b9 = 'Y' if b5 >= 400 else 'N'
a1 = 52
a2 = 8
if b7 in ['1', '2']:
    b8 = input('Enter the Cycle: ').upper()
    if b8 = = 'P':
        a2 = 7
        a1 = 46
elif b7 in ['3', '4'] and b9 = = 'Y':
    a2 = 9
    a1 = 58
with open('test2.txt', 'w+') as output_file:
    for college_code in b2:
        for usn_number in range(b5, b6):
            if usn_number < 10:
                b10 = college_code + b3 + b4 + '00' + str(usn_number)
            elif usn_number < 100:
                b10 = college_code + b3 + b4 + '0' + str(usn_number)
            else:
                b10 = college_code + b3 + b4 + str(usn_number)
            b11 = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
            b11.get('http:
            b11.save_screenshot('python_org.png')
            b12 = cv2.imread("python_org.png")
            b13 = b12[467:508, 667:885]
            cv2.imwrite('cap.png', b13)
            b14 = pytesseract.image_to_string(Image.open('cap.png'))
            b15 = int(b14.strip().replace(',', '').strip())
            b11.find_element_by_name("lns").send_keys(b10)
            b11.find_element_by_name("captchacode").send_keys(b15)
            b11.find_element_by_id("submit").click()
            try:
                b16 = BeautifulSoup(b11.page_source, 'html.parser')
            except:
                b17 = b11.switch_to.b17
                b17.dismiss()
                continue
            b18 = b16.find_all('th')
            b19 = b16.find_all('div', attrs={'class': 'divTableCell'})
            b20 = re.sub('[!@
            b21 = []
            for i in range(6, a1, 6):
                b22 = b19[i].text[-3:]
                b21.append(b22 if b22.isdigit() else b19[i].text[-2:])
            b21.sort()
            b23 = []
            for i in range(0, a2):
                for b24 in range(6, a1, 6):
                    b22 = b19[b24].text[-3:]
                    if b22.isdigit():
                        if b22 = = b21[i] and b24 not in b23:
                            b23.append(b24)
                    else:
                        if b19[b24].text[-2:] == b21[i] and b24 not in b23:
                            b23.append(b24)
            for l in b23:
                for b24 in range(l, l + 6):
                    if b24 = = l + 1:
                        continue
                    else:
                        b25 = b19[b24].text
                        b20 += str(int(b25)) + ',' if b25.isdigit() else b25 + ','
                output_file.write(b20 + '\n')
            b11.quit()
if b9 != 'Y':
    from sgparank import gpa2
    gpa2(b3, b4, b5, b6, b7, b8)