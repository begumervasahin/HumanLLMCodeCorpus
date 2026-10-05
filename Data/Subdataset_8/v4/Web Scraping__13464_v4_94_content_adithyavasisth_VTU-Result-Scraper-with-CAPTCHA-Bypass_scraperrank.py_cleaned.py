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
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
college = ["4AI", "1BG", "1CR", "1AM", "1BI"]
year = input('Enter the year: ')
branch = input('Please enter the branch: ').upper()
low = int(input('Enter starting USN: '))
high = int(input('Enter last USN: ')) + 1
semc = input('Enter the Semester: ')
if low >= 400:
    dip = 'Y'
else:
    dip = 'N'
subcode = 52
iloop = 8
cycle = 'N'
if semc in ['1', '2']:
    cycle = input('Enter the Cycle: ').upper()
    if cycle == 'P':
        iloop = 7
        subcode = 46
elif semc in ['3', '4'] and dip == 'Y':
    iloop = 9
    subcode = 58
with open('test2.txt', 'w+') as f:
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
    for x in college:
        for u in range(low, high):
            usn = f"{x}{year}{branch}{str(u).zfill(3)}"
            driver.get('http:
            driver.save_screenshot('python_org.png')
            img = cv2.imread("python_org.png")
            crop_img = img[467:508, 667:885]
            cv2.imwrite('cap.png', crop_img)
            tex = pytesseract.image_to_string(Image.open('cap.png'))
            captcha = int(tex.strip(',').strip())
            us = driver.find_element_by_name("lns")
            cap = driver.find_element_by_name("captchacode")
            us.send_keys(usn)
            cap.send_keys(captcha)
            driver.find_element_by_id("submit").click()
            try:
                soup = BeautifulSoup(driver.page_source)
            except:
                alert = driver.switch_to.alert
                alert.dismiss()
                continue
            divCell = soup.find_all('div', attrs={'class': 'divTableCell'})
            record = ''
            for i in range(6, subcode, 6):
                if divCell[i].text[-3:].isdigit():
                    record += divCell[i].text[-3:]
                else:
                    record += divCell[i].text[-2:]
                record += ','
            ilist = []
            for i in range(0, iloop):
                for j in range(6, subcode, 6):
                    if (divCell[j].text[-3:].isdigit() and divCell[j].text[-3:] == record[i]) or \
                            (not divCell[j].text[-3:].isdigit() and divCell[j].text[-2:] == record[i]):
                        ilist.append(j)
            for l in ilist:
                for j in range(l, l + 6):
                    if j == l + 1:
                        continue
                    else:
                        char = divCell[j].text
                        if char.isdigit():
                            record += str(int(char))
                        else:
                            record += char
                        record += ','
                f.write(record + '\n')
if dip != 'Y':
    from sgparank import gpa2
    gpa2(year, branch, low, high, semc, cycle)