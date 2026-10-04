import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
b1 = "C:\\Users\\raghu\\Desktop\\Chromedriver\\chromedriver.exe"
b2 = "http:
def fonk1():
    b3 = webdriver.Chrome(b1)
    b3.get(b2)
    b3.maximize_window()
    return b3
def fonk2(b3, district_value):
    b4 = Select(b3.find_element_by_class_name("selectdistrict"))
    b4.select_by_value(district_value)
def fonk3(b3):
    b3.find_element_by_xpath('
    time.sleep(3)
    b3.find_element_by_xpath('
    time.sleep(5)
def fonk4(b3):
    b3.switch_to.frame('data')
    b3.find_element_by_xpath('
    b5 = Select(b3.find_element_by_xpath('
    b5.select_by_visible_text("District and Sessions Court, Shivajinagar, Pune - 411 005")
def fonk5(b3, from_month_year, from_day, to_day):
    b3.find_element_by_xpath('
    b6 = Select(b3.find_element_by_class_name("datepick-month-year"))
    b6.select_by_value(from_month_year)
    b3.find_element_by_xpath(f'/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[{from_day}]/a').click()
    time.sleep(2)
    b3.find_element_by_xpath('
    time.sleep(2)
    b3.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/select[1]/option[1]').click()
    time.sleep(2)
    b3.find_element_by_xpath(f'/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[{to_day}]/a').click()
def fonk6(b3):
    print("ENTER CAPTCHA AND WAIT for 20 seconds")
    time.sleep(20)
    b3.find_element_by_xpath('
    time.sleep(10)
def fonk7(b3, start_index):
    for i in range(3, 7):
        b7 = f'
        b8 = b3.find_element_by_xpath(b7).text
        filename, b9 = b8.split(':')[0], int(b8.split(':')[1][1:])
        with open(f"{filename}.txt", "w") as file:
            b10 = "(Sr No, Case Type/Case Number/Case Year, Order Date, Order No.)\n"
            file.write(b10)
            for row in range(start_index, start_index + b9):
                b11 = [
                    b3.find_element_by_xpath(f'
                    for col in range(1, 5)
                ]
                file.write('\t'.join(b11) + '\n')
            start_index += b9
def fonk8():
    b3 = fonk1()
    fonk2(b3, "25")
    fonk3(b3)
    fonk4(b3)
    fonk5(b3, "1/2019", 3, 4)
    fonk6(b3)
    fonk7(b3, 2)
    b3.quit()
if b12 = = "__main__":
    fonk8()