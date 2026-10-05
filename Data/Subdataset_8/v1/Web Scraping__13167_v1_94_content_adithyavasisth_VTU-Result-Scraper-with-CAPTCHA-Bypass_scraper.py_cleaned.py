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
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
if not sys.warnoptions:
    warnings.simplefilter("ignore")
college = input("Enter the college code: ").upper()
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
if semc == '3' or semc == '4':
    iloop = 9
    subcode = 58
    if dip == 'Y':
        iloop = 10
        subcode = 64
with open('marks.txt', 'w+') as f:
    c = 0
    pf = ''
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
    for u in range(low, high):
        redo = True
        while redo:
            redo = False
            if u < 10:
                usn = '1' + college + year + branch + '00' + str(u)
            elif u < 100:
                usn = '1' + college + year + branch + '0' + str(u)
            else:
                usn = '1' + college + year + branch + str(u)
            driver.get('http:
            driver.save_screenshot('python_org.png')
            img = cv2.imread("python_org.png")
            crop_img = img[467:508, 667:885]
            cv2.imwrite('cap.png', crop_img)
            cv2.waitKey(0)
            tex = pytesseract.image_to_string(Image.open('cap.png'))
            tex = tex.strip(',')
            tex = tex.strip(' ')
            try:
                captcha = int(tex)
            except ValueError:
                print("Invalid CAPTCHA Detected.")
                redo = True
                continue
            us = driver.find_element_by_name("lns")
            cap = driver.find_element_by_name("captchacode")
            us.send_keys(usn)
            cap.send_keys(captcha)
            driver.find_element_by_id("submit").click()
            try:
                soup = BeautifulSoup(driver.page_source, 'html.parser')
            except:
                alert = driver.switch_to.alert
                if alert.text == "University Seat Number is not available or Invalid..!":
                    print("No results for: " + usn + "\n")
                    alert.accept()
                    continue
                elif alert.text == "Invalid captcha code !!!":
                    print("Invalid CAPTCHA Detected for USN: " + usn + "\n")
                    alert.accept()
                    redo = True
                    continue
            tds = soup.find_all('td')
            ths = soup.find_all('th')
            divs = soup.find_all('div', attrs={'class': 'col-md-12'})
            divCell = soup.find_all('div', attrs={'class': 'divTableCell'})
            try:
                sem = divs[5].div.text
                sem = sem.strip('Semester: ')
            except AttributeError:
                print("INVALID USN/ INCOMPATIBLE DATA: " + usn + "\n")
            if tds[0].text != 'University Seat Number ' or sem != semc:
                print("INVALID USN/ INCOMPATIBLE DATA: " + usn + "\n")
                continue
            record = ''
            record += re.sub('[!@\n]', ',', ths[2].text) + ','
            record += re.sub('[!@\n]', ',', ths[3].text) + ','
            sortList1 = []
            for i in range(6, subcode, 6):
                if (divCell[i].text[-3:]).isdigit():
                    sortList1.append(divCell[i].text[-3:])
                else:
                    sortList1.append(divCell[i].text[-2:])
            sortList1.sort()
            ilist = []
            for i in range(0, iloop):
                for j in range(6, subcode, 6):
                    if (divCell[j].text[-3:]).isdigit():
                        if divCell[j].text[-3:] == sortList1[i] and j not in ilist:
                            ilist.append(j)
                    else:
                        if divCell[j].text[-2:] == sortList1[i] and j not in ilist:
                            ilist.append(j)
            print(record, end='\t')
            try:
                for l in ilist:
                    for j in range(l, l + 6):
                        if j == l + 1:
                            continue
                        else:
                            char = divCell[j].text
                            if char.isdigit():
                                record = record + str(int(char)) + ','
                            else:
                                record = record + char + ','
                            print(divCell[j].text, end='\t\t')
                            if j == l + 5:
                                pf = pf + divCell[j].text + ','
                f.write(record + '\n')
                print('\n')
            except IndexError:
                pass
    driver.quit()
book = xlwt.Workbook()
ws = book.add_sheet('Sheet1')
alignment = xlwt.Alignment()
font = xlwt.Font()
alignment.horz = xlwt.Alignment.HORZ_CENTER
font.bold = True
style = xlwt.XFStyle()
f = open('marks.txt', 'r+')
data = f.readlines()
for i in range(len(data)):
    row = data[i].split(',')
    for j in range(len(row)):
        if row[j].isdigit():
            ws.write(i, j, int(row[j]), style)
        else:
            ws.write(i, j, row[j], style)
pth = 'ExcelFiles/'
if not os.path.exists(pth):
    os.makedirs(pth)
if dip == 'N':
    book.save(pth + '1' + college + year + branch + str(low) + '-' + str(high - 1) + '.xls')
else:
    book.save(pth + '1' + college + year + branch + str(low) + '-' + str(high - 1) + 'DIP.xls')
f.close()
files = ['cap.png', 'python_org.png', 'marks.txt']
for file in files:
    try:
        os.remove(file)
    except:
        pass
if dip != 'Y':
    from sgpa import gpa
    gpa(college, year, branch, low, high, semc)