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
driver.find_element_by_xpath('
time.sleep(3)
driver.find_element_by_xpath('
time.sleep(5)
driver.switch_to.frame('data')
driver.find_element_by_xpath('
court_complex_select = Select(driver.find_element_by_xpath('
court_complex_select.select_by_visible_text("District and Sessions Court, Shivajinagar, Pune - 411 005")
driver.find_element_by_xpath('
month_year_select = Select(driver.find_element_by_class_name("datepick-month-year"))
month_year_select.select_by_value("1/2019")
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/a').click()
time.sleep(2)
driver.find_element_by_xpath('
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/select[1]/option[1]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]/a').click()
print("ENTER CAPTCHA AND WAIT for 10 seconds\n")
time.sleep(20)
driver.find_element_by_xpath('
time.sleep(10)
start_index = 2
for i in range(3, 7):
    x_path_base = '
    case_details = driver.find_element_by_xpath(f"{x_path_base}{i}]/a").text
    filename, rows = case_details.split(':')[0], int(case_details.split(':')[1][1:])
    with open(f"{filename}.txt", "w") as file:
        headers = "(Sr No, Case Type/Case Number/Case Year, Order Date, Order No.)\n"
        file.write(headers)
        for row_index in range(start_index, rows + start_index):
            for column_index in range(1, 5):
                x_path_cell = f'
                cell_text = driver.find_element_by_xpath(x_path_cell).text
                file.write(cell_text + '\t')
            file.write('\n')
    start_index += 2
driver.quit()