import os
import cv2
import pytesseract
from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
import xlwt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
def input_user_details():
    college = input("Enter the college code: ").upper()
    year = input('Enter the year: ')
    branch = input('Please enter the branch: ').upper()
    low = int(input('Enter starting USN: '))
    high = int(input('Enter last USN: ')) + 1
    semc = input('Enter the Semester: ')
    return college, year, branch, low, high, semc
def is_diploma(low):
    return 'Y' if low >= 400 else 'N'
def get_usn(college, year, branch, u):
    if u < 10:
        return '1' + college + year + branch + '00' + str(u)
    elif u < 100:
        return '1' + college + year + branch + '0' + str(u)
    else:
        return '1' + college + year + branch + str(u)
def retrieve_captcha(driver):
    driver.save_screenshot('python_org.png')
    img = cv2.imread("python_org.png")
    crop_img = img[467:508, 667:885]
    cv2.imwrite('cap.png', crop_img)
    cv2.waitKey(0)
    captcha_text = pytesseract.image_to_string(Image.open('cap.png')).strip(',').strip(' ')
    try:
        captcha = int(captcha_text)
    except ValueError:
        print("Invalid CAPTCHA Detected.")
        return retrieve_captcha(driver)
    return captcha
def scrape_results(driver, low, high, semc, subcode, iloop):
    with open('marks.txt', 'w+') as f:
        for u in range(low, high):
            retry = True
            while retry:
                retry = False
                usn = get_usn(college, year, branch, u)
                driver.get('http:
                captcha = retrieve_captcha(driver)
                usn_input = driver.find_element_by_name("lns")
                captcha_input = driver.find_element_by_name("captchacode")
                usn_input.send_keys(usn)
                captcha_input.send_keys(captcha)
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
                        retry = True
                        continue
        driver.quit()
def write_to_excel():
    book = xlwt.Workbook()
    ws = book.add_sheet('Sheet1')
    with open('marks.txt', 'r+') as f:
        for i, line in enumerate(f.readlines()):
            row = line.split(',')
            for j, item in enumerate(row):
                if item.isdigit():
                    ws.write(i, j, int(item))
                else:
                    ws.write(i, j, item)
    pth = 'ExcelFiles/'
    if not os.path.exists(pth):
        os.makedirs(pth)
    file_name = '1' + college + year + branch + str(low) + '-' + str(high - 1)
    if dip == 'Y':
        file_name += 'DIP'
    file_name += '.xls'
    book.save(os.path.join(pth, file_name))
def clean_up_temp_files():
    files = ['cap.png', 'python_org.png', 'marks.txt']
    for file in files:
        try:
            os.remove(file)
        except FileNotFoundError:
            pass
def main():
    college, year, branch, low, high, semc = input_user_details()
    dip = is_diploma(low)
    subcode = 52
    iloop = 8
    if semc == '3' or semc == '4':
        iloop = 9
        subcode = 58
        if dip == 'Y':
            iloop = 10
            subcode = 64
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver_win32\chromedriver.exe')
    scrape_results(driver, low, high, semc, subcode, iloop)
    write_to_excel()
    clean_up_temp_files()
    if dip != 'Y':
        from sgpa import gpa
        gpa(college, year, branch, low, high, semc)
if __name__ == "__main__":
    main()