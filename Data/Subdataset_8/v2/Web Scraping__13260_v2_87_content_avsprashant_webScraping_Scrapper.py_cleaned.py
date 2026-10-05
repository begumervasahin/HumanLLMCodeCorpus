import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
chromedriver_path = "C:\\Users\\raghu\\Desktop\\Chromedriver\\chromedriver.exe"
url = "http:
driver = webdriver.Chrome(chromedriver_path)
driver.get(url)
driver.maximize_window()
district_select = Select(driver.find_element_by_class_name("selectdistrict"))
district_select.select_by_value("25")
driver.find_element_by_xpath("
time.sleep(3)
driver.find_element_by_xpath("
time.sleep(5)
driver.switch_to.frame('data')
driver.find_element_by_id("radCourtComplex").click()
court_complex_select = Select(driver.find_element_by_xpath("
court_complex_select.select_by_visible_text("District and Sessions Court, Shivajinagar, Pune - 411 005")
driver.find_element_by_id("from_date").click()
month_year_select = Select(driver.find_element_by_class_name("datepick-month-year"))
month_year_select.select_by_value("1/2019")
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/a").click()
time.sleep(2)
driver.find_element_by_id("to_date").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/select[1]/option[1]").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]/a").click()
print("Please enter CAPTCHA and wait for 10 seconds...")
time.sleep(10)
driver.find_element_by_xpath("
time.sleep(10)
start_row = 2
for i in [3, 4, 5, 6]:
    xpath_prefix = '
    xpath_suffix = ']/a'
    page_info = driver.find_element_by_xpath(xpath_prefix + str(i) + xpath_suffix).text
    filename = page_info.split(':')[0]
    rows = int(page_info.split(':')[1][1:])
    with open(filename + ".txt", "w") as file:
        headers = "(Sr No, Case Type/Case Number/Case Year, Order Date, Order No.)\n"
        file.write(headers)
        for row_num in range(start_row, rows + start_row):
            for col_num in [1, 2, 3, 4]:
                data_xpath = '
                data = driver.find_element_by_xpath(data_xpath).text
                file.write(data + '\t')
            file.write('\n')
        start_row += 2
driver.quit()
print("Scraping Completed.")