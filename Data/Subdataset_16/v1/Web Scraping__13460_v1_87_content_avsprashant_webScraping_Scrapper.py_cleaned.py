import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
b1 = "C:\\Users\\raghu\\Desktop\\Chromedriver\\chromedriver.exe"
b2 = "http:
b3 = webdriver.Chrome(b1)
b3.get(b2)
b3.maximize_window()
b4 = Select(b3.find_element_by_class_name("selectdistrict"))
b4.select_by_value("25")
b3.find_element_by_xpath('
time.sleep(3)
b3.find_element_by_xpath('
time.sleep(5)
b3.switch_to.frame('data')
b3.find_element_by_xpath('
b5 = Select(b3.find_element_by_xpath('
b5.select_by_visible_text("District and Sessions Court, Shivajinagar, Pune - 411 005")
b3.find_element_by_xpath('
b6 = Select(b3.find_element_by_class_name("datepick-month-year"))
b6.select_by_value("1/2019")
b3.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/a').click()
time.sleep(2)
b3.find_element_by_xpath('
time.sleep(2)
b3.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/select[1]/option[1]').click()
time.sleep(2)
b3.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]/a').click()
print("ENTER CAPTCHA AND WAIT for 20 seconds")
time.sleep(20)
b3.find_element_by_xpath('
time.sleep(10)
a1 = 2
for i in range(3, 7):
    b7 = f'
    b8 = b3.find_element_by_xpath(b7).text
    b9 = b8.split(':')[0]
    b10 = int(b8.split(':')[1][1:])
    with open(f"{b9}.txt", "w") as f:
        b11 = "(Sr No, Case Type/Case Number/Case Year, Order Date, Order No.)\n"
        f.write(b11)
        for row in range(a1, a1 + b10):
            b12 = []
            for col in range(1, 5):
                b13 = f'
                b14 = b3.find_element_by_xpath(b13).text
                b12.append(b14)
            f.write('\t'.join(b12) + '\n')
        a1 += b10
b3.quit()