import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
CHROMEDRIVER_PATH = "C:\\Users\\raghu\\Desktop\\Chromedriver\\chromedriver.exe"
URL = "http:
def initialize_driver():
    driver = webdriver.Chrome(CHROMEDRIVER_PATH)
    driver.get(URL)
    driver.maximize_window()
    return driver
def select_district(driver, district_value):
    district_select = Select(driver.find_element_by_class_name("selectdistrict"))
    district_select.select_by_value(district_value)
def navigate_menus(driver):
    driver.find_element_by_xpath('
    time.sleep(3)
    driver.find_element_by_xpath('
    time.sleep(5)
def select_court_complex(driver):
    driver.switch_to.frame('data')
    driver.find_element_by_xpath('
    court_complex_select = Select(driver.find_element_by_xpath('
    court_complex_select.select_by_visible_text("District and Sessions Court, Shivajinagar, Pune - 411 005")
def select_date_range(driver, from_month_year, from_day, to_day):
    driver.find_element_by_xpath('
    from_date_select = Select(driver.find_element_by_class_name("datepick-month-year"))
    from_date_select.select_by_value(from_month_year)
    driver.find_element_by_xpath(f'/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[{from_day}]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/select[1]/option[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath(f'/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[{to_day}]/a').click()
def search_cases(driver):
    print("ENTER CAPTCHA AND WAIT for 20 seconds")
    time.sleep(20)
    driver.find_element_by_xpath('
    time.sleep(10)
def save_case_details(driver, start_index):
    for i in range(3, 7):
        case_info_xpath = f'
        case_info = driver.find_element_by_xpath(case_info_xpath).text
        filename, rows = case_info.split(':')[0], int(case_info.split(':')[1][1:])
        with open(f"{filename}.txt", "w") as file:
            headers = "(Sr No, Case Type/Case Number/Case Year, Order Date, Order No.)\n"
            file.write(headers)
            for row in range(start_index, start_index + rows):
                row_data = [
                    driver.find_element_by_xpath(f'
                    for col in range(1, 5)
                ]
                file.write('\t'.join(row_data) + '\n')
            start_index += rows
def main():
    driver = initialize_driver()
    select_district(driver, "25")
    navigate_menus(driver)
    select_court_complex(driver)
    select_date_range(driver, "1/2019", 3, 4)
    search_cases(driver)
    save_case_details(driver, 2)
    driver.quit()
if __name__ == "__main__":
    main()