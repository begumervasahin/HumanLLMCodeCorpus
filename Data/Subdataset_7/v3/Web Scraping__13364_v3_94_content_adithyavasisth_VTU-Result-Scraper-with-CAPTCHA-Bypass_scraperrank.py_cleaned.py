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
def fonk1(college_code, b18, b19, usn_number):
    b2 = str(usn_number).zfill(3)
    return f"{college_code}{b18}{b19}{b2}"
def fonk2():
    b3 = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
    b3.get('http:
    b3.save_screenshot('python_org.png')
    b4 = cv2.imread("python_org.png")
    b5 = b4[467:508, 667:885]
    cv2.imwrite('cap.png', b5)
    b6 = pytesseract.image_to_string(Image.open('cap.png')).strip().replace(',', '').strip()
    b3.quit()
    return int(b6)
def fonk3(b25):
    b3 = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
    b3.get('http:
    b3.find_element_by_name("lns").send_keys(b25)
    b3.find_element_by_name("captchacode").send_keys(fonk2())
    b3.find_element_by_id("submit").click()
    try:
        b7 = BeautifulSoup(b3.page_source, 'html.parser')
    except:
        b8 = b3.switch_to.b8
        b8.dismiss()
        b3.quit()
        return None
    finally:
        b3.quit()
    return b7
def fonk4(b7, a1, a2):
    b9 = b7.find_all('th')
    b10 = b7.find_all('div', attrs={'class': 'divTableCell'})
    b11 = ','.join(re.sub('[!@
    b12 = [b10[i].text[-3:] if b10[i].text[-3:].isdigit() else b10[i].text[-2:] for i in range(6, a1, 6)]
    b12.sort()
    b13 = []
    for i in range(a2):
        for j in range(6, a1, 6):
            b14 = b10[j].text[-3:]
            if b14.isdigit():
                if b14 = = b12[i] and j not in b13:
                    b13.append(j)
            elif b10[j].text[-2:] == b12[i] and j not in b13:
                b13.append(j)
    b15 = []
    for l in b13:
        b16 = ','.join(b10[j].text if j != l + 1 else '' for j in range(l, l + 6))
        b15.append(b16)
    return b11, b15
b17 = ["4AI", "1BG", "1CR", "1AM", "1BI"]
b18 = input('Enter the b18: ')
b19 = input('Please enter the b19: ').upper()
b20 = int(input('Enter starting USN: '))
b21 = int(input('Enter last USN: ')) + 1
b22 = input('Enter the Semester: ')
b23 = 'N'
b24 = 'Y' if b20 >= 400 else 'N'
a1 = 52
a2 = 8
if b22 in ['1', '2']:
    b23 = input('Enter the Cycle: ').upper()
    if b23 = = 'P':
        a2 = 7
        a1 = 46
elif b22 in ['3', '4'] and b24 = = 'Y':
    a2 = 9
    a1 = 58
with open('test2.txt', 'w+') as output_file:
    for college_code in b17:
        for usn_number in range(b20, b21):
            b25 = fonk1(college_code, b18, b19, usn_number)
            b7 = fonk3(b25)
            if b7:
                b11, b15 = fonk4(b7, a1, a2)
                output_file.write(f"{b11}\n")
                for b16 in b15:
                    output_file.write(f"{b16}\n")
if b24 != 'Y':
    from sgparank import gpa2
    gpa2(b18, b19, b20, b21, b22, b23)