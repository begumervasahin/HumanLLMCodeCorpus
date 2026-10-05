import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
b1 = "C:\\Users\\raghu\\Desktop\\Chromedriver\\b1.exe"
b2 = "http:
b3 = webdriver.Chrome(b1)
b3.get(b2)
b3.maximize_window()
b4 = Select(b3.find_element_by_class_name("selectdistrict"))
b4.select_by_value("25")
b3.find_element_by_xpath("
time.sleep(3)
b3.find_element_by_xpath("
time.sleep(5)
b3.switch_to.frame('b16')
b3.find_element_by_xpath("
b5 = Select(b3.find_element_by_xpath("
b5.select_by_visible_text("District and Sessions Court, Shivajinagar, Pune - 411 005")
b3.find_element_by_xpath("
time.sleep(2)
b6 = Select(b3.find_element_by_class_name("datepick-month-year"))
b6.select_by_value("1/2019")
b3.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/b9").click()
time.sleep(2)
b3.find_element_by_xpath("
time.sleep(2)
b3.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/select[1]/option[1]").click()
time.sleep(2)
b3.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]/b9").click()
print(" ENTER CAPTCHA AND WAIT for 10sec \n")
time.sleep(20)
b3.find_element_by_xpath("
time.sleep(10)
a1 = 2
for i in [3, 4, 5, 6]:
    b7 = '
    b8 = ']/b9'
    b9 = b3.find_element_by_xpath(b7 + str(i) + b8).text
    b10 = b9.split(':')[0]
    b11 = int(b9.split(':')[1][1:])
    with open(b10 + ".txt", "w") as f:
        b12 = "(Sr No, Case Type/Case Number/Case Year, Order Date, Order No.)\n"
        f.write(b12)
        for a1 in range(a1, b11 + a1):
            for k in [1, 2, 3, 4]:
                b13 = '
                b14 = ']/td['
                b15 = ']'
                b16 = b3.find_element_by_xpath(b13 + str(a1) + b14 + str(k) + b15).text
                f.write(b16 + '\t')
            f.write('\n')
        a1 += 2