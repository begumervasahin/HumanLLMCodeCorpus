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
college_prefixes = ["4AI", "1BG", "1CR", "1AM", "1BI"]
year = input('Enter the year: ')
branch = input('Please enter the branch: ').upper()
start_usn = int(input('Enter starting USN: '))
end_usn = int(input('Enter last USN: ')) + 1
semester = input('Enter the Semester: ')
is_diploma = 'Y' if start_usn >= 400 else 'N'
subject_code = 52
loop_iterations = 8
cycle = 'N'
if semester in ['1', '2']:
    cycle = input('Enter the Cycle: ').upper()
    if cycle == 'P':
        loop_iterations = 7
        subject_code = 46
elif semester in ['3', '4'] and is_diploma == 'Y':
    loop_iterations = 9
    subject_code = 58
with open('test2.txt', 'w+') as output_file:
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
    for prefix in college_prefixes:
        for usn_number in range(start_usn, end_usn):
            usn = f"{prefix}{year}{branch}{str(usn_number).zfill(3)}"
            driver.get('http:
            driver.save_screenshot('screenshot.png')
            img = cv2.imread("screenshot.png")
            cropped_img = img[467:508, 667:885]
            cv2.imwrite('cap.png', cropped_img)
            captcha_text = pytesseract.image_to_string(Image.open('cap.png')).strip(',').strip()
            captcha = int(captcha_text)
            usn_input = driver.find_element_by_name("lns")
            captcha_input = driver.find_element_by_name("captchacode")
            usn_input.send_keys(usn)
            captcha_input.send_keys(captcha)
            driver.find_element_by_id("submit").click()
            try:
                soup = BeautifulSoup(driver.page_source, 'html.parser')
            except:
                alert = driver.switch_to.alert
                alert.dismiss()
                continue
            div_cells = soup.find_all('div', class_='divTableCell')
            result_record = ''
            for i in range(6, subject_code, 6):
                if div_cells[i].text[-3:].isdigit():
                    result_record += div_cells[i].text[-3:]
                else:
                    result_record += div_cells[i].text[-2:]
                result_record += ','
            index_list = []
            for i in range(loop_iterations):
                for j in range(6, subject_code, 6):
                    if (div_cells[j].text[-3:].isdigit() and div_cells[j].text[-3:] == result_record[i]) or \
                            (not div_cells[j].text[-3:].isdigit() and div_cells[j].text[-2:] == result_record[i]):
                        index_list.append(j)
            for l in index_list:
                for j in range(l, l + 6):
                    if j == l + 1:
                        continue
                    else:
                        char = div_cells[j].text
                        if char.isdigit():
                            result_record += str(int(char))
                        else:
                            result_record += char
                        result_record += ','
                output_file.write(result_record + '\n')
if is_diploma != 'Y':
    from sgparank import gpa2
    gpa2(year, branch, start_usn, end_usn, semester, cycle)