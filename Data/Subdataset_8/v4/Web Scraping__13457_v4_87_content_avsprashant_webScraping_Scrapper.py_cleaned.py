import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
chromedriver = "C:\\Users\\raghu\\Desktop\\Chromedriver\\chromedriver.exe"
url = "http:
driver = webdriver.Chrome(chromedriver)
driver.get(url)
driver.maximize_window()
district_selector = Select(driver.find_element_by_class_name("selectdistrict"))
district_selector.select_by_value("25")
driver.find_element_by_xpath("
time.sleep(3)
driver.find_element_by_xpath("
time.sleep(5)
driver.switch_to.frame('data')
driver.find_element_by_xpath("
court_complex_selector = Select(driver.find_element_by_xpath("
court_complex_selector.select_by_visible_text("District and Sessions Court, Shivajinagar, Pune - 411 005")
driver.find_element_by_xpath("
time.sleep(2)
month_year_selector = Select(driver.find_element_by_class_name("datepick-month-year"))
month_year_selector.select_by_value("1/2019")
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/a").click()
time.sleep(2)
driver.find_element_by_xpath("
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/select[1]/option[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]/a").click()
print(" ENTER CAPTCHA AND WAIT for 10sec \n")
time.sleep(20)
driver.find_element_by_xpath("
time.sleep(10)
start_row = 2
for i in [3, 4, 5, 6]:
    xpath_prefix = '
    xpath_suffix = ']/a'
    a = driver.find_element_by_xpath(xpath_prefix + str(i) + xpath_suffix).text
    filename = a.split(':')[0]
    rows = int(a.split(':')[1][1:])
    with open(filename + ".txt", "w") as f:
        headers = "(Sr No, Case Type/Case Number/Case Year, Order Date, Order No.)\n"
        f.write(headers)
        for start_row in range(start_row, rows + start_row):
            for k in [1, 2, 3, 4]:
                x = '
                y = ']/td['
                z = ']'
                data = driver.find_element_by_xpath(x + str(start_row) + y + str(k) + z).text
                f.write(data + '\t')
            f.write('\n')
        start_row += 2