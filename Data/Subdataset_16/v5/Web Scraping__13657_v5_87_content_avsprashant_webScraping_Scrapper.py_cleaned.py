import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
def fonk1(b11):
    b1 = webdriver.Chrome(b11)
    b1.maximize_window()
    return b1
def fonk2(b1, b12):
    b1.get(b12)
def fonk3(b1, b13):
    b2 = Select(b1.find_element_by_class_name("selectdistrict"))
    b2.select_by_value(b13)
def fonk4(b1):
    b1.find_element_by_xpath('
    time.sleep(3)
    b1.find_element_by_xpath('
    time.sleep(5)
def fonk5(b1, frame_name):
    b1.switch_to.frame(frame_name)
def fonk6(b1, b14):
    b1.find_element_by_xpath('
    b3 = Select(b1.find_element_by_xpath('
    b3.select_by_visible_text(b14)
def fonk7(b1, date_element_xpath, month_year_value, day_xpath):
    b1.find_element_by_xpath(date_element_xpath).click()
    b4 = Select(b1.find_element_by_class_name("datepick-month-year"))
    b4.select_by_value(month_year_value)
    b1.find_element_by_xpath(day_xpath).click()
    time.sleep(2)
def fonk8():
    print("ENTER CAPTCHA AND WAIT for 10 seconds\n")
    time.sleep(20)
def fonk9(b1):
    b1.find_element_by_xpath('
    time.sleep(10)
def fonk10(b1, b21, end_index):
    for i in range(b21, end_index):
        b5 = '
        b6 = b1.find_element_by_xpath(f"{b5}{i}]/a").text
        filename, b7 = b6.split(':')[0], int(b6.split(':')[1][1:])
        with open(f"{filename}.txt", "w") as file:
            b8 = "(Sr No, Case Type/Case Number/Case Year, Order Date, Order No.)\n"
            file.write(b8)
            for row_index in range(b21, b7 + b21):
                for column_index in range(1, 5):
                    b9 = f'
                    b10 = b1.find_element_by_xpath(b9).text
                    file.write(b10 + '\t')
                file.write('\n')
        b21 += 2
def fonk11():
    b11 = "C:\\Users\\raghu\\Desktop\\Chromedriver\\chromedriver.exe"
    b12 = "http:
    b13 = "25"
    b14 = "District and Sessions Court, Shivajinagar, Pune - 411 005"
    b15 = '
    b16 = "1/2019"
    b17 = '/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/a'
    b18 = '
    b19 = "1/2019"
    b20 = '/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]/a'
    b1 = fonk1(b11)
    fonk2(b1, b12)
    fonk3(b1, b13)
    fonk4(b1)
    fonk5(b1, 'data')
    fonk6(b1, b14)
    fonk7(b1, b15, b16, b17)
    fonk7(b1, b18, b19, b20)
    fonk8()
    fonk9(b1)
    fonk10(b1, b21 = 2, end_index=7)
    b1.quit()
if b22 = = "__main__":
    fonk11()