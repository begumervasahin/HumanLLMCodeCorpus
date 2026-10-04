import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
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
from_date_select = Select(driver.find_element_by_class_name("datepick-month-year"))
from_date_select.select_by_value("1/2019")
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/a').click()
time.sleep(2)
driver.find_element_by_xpath('
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/select[1]/option[1]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]/a').click()
print("ENTER CAPTCHA AND WAIT for 20 seconds")
time.sleep(20)
driver.find_element_by_xpath('
time.sleep(10)
start = 2
for i in range(3, 7):
    case_info_xpath = f'
    case_info = driver.find_element_by_xpath(case_info_xpath).text
    filename = case_info.split(':')[0]
    rows = int(case_info.split(':')[1][1:])
    with open(f"{filename}.txt", "w") as f:
        headers = "(Sr No, Case Type/Case Number/Case Year, Order Date, Order No.)\n"
        f.write(headers)
        for row in range(start, start + rows):
            row_data = []
            for col in range(1, 5):
                cell_xpath = f'
                cell_data = driver.find_element_by_xpath(cell_xpath).text
                row_data.append(cell_data)
            f.write('\t'.join(row_data) + '\n')
        start += rows
driver.quit()