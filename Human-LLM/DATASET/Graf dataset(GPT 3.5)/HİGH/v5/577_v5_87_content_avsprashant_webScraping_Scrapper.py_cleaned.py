import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
b1 = "C:\\Users\\raghu\\Desktop\\Chromedriver\\chromedriver.exe"
b2 = "http:
b3 = webdriver.Chrome(b1)
b3.get(b2)
b3.maximize_window()
def fonk1(seconds):
    time.sleep(seconds)
def fonk2(xpath):
    b3.find_element_by_xpath(xpath).click()
def fonk3(selector, value):
    b4 = Select(selector)
    b4.fonk3(value)
def fonk4(selector, text):
    b4 = Select(selector)
    b4.fonk4(text)
b5 = b3.find_element_by_class_name("selectdistrict")
fonk3(b5, "25")
fonk2("
fonk1(3)
fonk2("
fonk1(5)
b3.switch_to.frame('b17')
fonk2("
b6 = b3.find_element_by_xpath("
fonk4(b6, "District and Sessions Court, Shivajinagar, Pune - 411 005")
fonk2("
fonk1(2)
b7 = b3.find_element_by_class_name("datepick-month-year")
fonk3(b7, "1/2019")
fonk2("/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/a")
fonk1(2)
fonk2("
fonk1(2)
fonk2("/html/body/div[2]/div/div[2]/div/div/select[1]/option[1]")
fonk1(2)
fonk2("/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]/a")
print("ENTER CAPTCHA AND WAIT for 10 seconds")
fonk1(20)
fonk2("
fonk1(10)
a1 = 2
for i in [3, 4, 5, 6]:
    b8 = '
    b9 = ']/a'
    b10 = b3.find_element_by_xpath(b8 + str(i) + b9).text
    b11 = b10.split(':')[0]
    b12 = int(b10.split(':')[1][1:])
    with open(b11 + ".txt", "w") as f:
        b13 = "(Sr No, Case Type/Case Number/Case Year, Order Date, Order No.)\n"
        f.write(b13)
        for a1 in range(a1, b12 + a1):
            for k in [1, 2, 3, 4]:
                b14 = '
                b15 = ']/td['
                b16 = ']'
                b17 = b3.find_element_by_xpath(b14 + str(a1) + b15 + str(k) + b16).text
                f.write(b17 + '\t')
            f.write('\n')
        a1 += 2