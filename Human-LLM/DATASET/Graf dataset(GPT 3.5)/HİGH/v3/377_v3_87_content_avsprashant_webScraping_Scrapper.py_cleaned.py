import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
b1 = "C:\\Users\\raghu\\Desktop\\Chromedriver\\chromedriver.exe"
b2 = "http:
b3 = webdriver.Chrome(b1)
b3.get(b2)
b3.maximize_window()
b4 = Select(b3.find_element_by_class_name("selectdistrict"))
b4.select_by_value("25")
time.sleep(3)
b3.find_element_by_xpath("
time.sleep(5)
b3.find_element_by_xpath("
time.sleep(5)
b3.switch_to.frame('b12')
b3.find_element_by_id("radCourtComplex").click()
b5 = Select(b3.find_element_by_xpath("
b5.select_by_visible_text("District and Sessions Court, Shivajinagar, Pune - 411 005")
b3.find_element_by_id("from_date").click()
b6 = Select(b3.find_element_by_class_name("datepick-month-year"))
b6.select_by_value("1/2019")
b3.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/a").click()
time.sleep(2)
b3.find_element_by_id("to_date").click()
time.sleep(2)
b3.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/select[1]/option[1]").click()
time.sleep(2)
b3.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]/a").click()
print("Please enter CAPTCHA and wait for 10 seconds...")
time.sleep(10)
b3.find_element_by_xpath("
time.sleep(10)
a1 = 2
for page_num in [3, 4, 5, 6]:
    b7 = f'
    b8 = b3.find_element_by_xpath(b7).text
    filename, b9 = b8.split(':')[0], int(b8.split(':')[1][1:])
    with open(f"{filename}.txt", "w") as file:
        file.write("(Sr No, Case Type/Case Number/Case Year, Order Date, Order No.)\n")
        for row_num in range(a1, b9 + a1):
            b10 = []
            for col_num in [1, 2, 3, 4]:
                b11 = f'
                b12 = b3.find_element_by_xpath(b11).text
                b10.append(b12)
            file.write('\t'.join(b10) + '\n')
        a1 += 2
b3.quit()
print("Scraping Completed.")