import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
def initialize_webdriver(chromedriver_path):
    driver = webdriver.Chrome(chromedriver_path)
    driver.maximize_window()
    return driver
def navigate_to_page(driver, url):
    driver.get(url)
def select_district(driver, district_value):
    district_select = Select(driver.find_element_by_class_name("selectdistrict"))
    district_select.select_by_value(district_value)
def navigate_to_court_page(driver):
    driver.find_element_by_xpath('
    time.sleep(3)
    driver.find_element_by_xpath('
    time.sleep(5)
def switch_to_frame(driver, frame_name):
    driver.switch_to.frame(frame_name)
def select_court_complex(driver, complex_name):
    driver.find_element_by_xpath('
    court_complex_select = Select(driver.find_element_by_xpath('
    court_complex_select.select_by_visible_text(complex_name)
def set_date(driver, date_element_xpath, month_year_value, day_xpath):
    driver.find_element_by_xpath(date_element_xpath).click()
    month_year_select = Select(driver.find_element_by_class_name("datepick-month-year"))
    month_year_select.select_by_value(month_year_value)
    driver.find_element_by_xpath(day_xpath).click()
    time.sleep(2)
def wait_for_captcha():
    print("ENTER CAPTCHA AND WAIT for 10 seconds\n")
    time.sleep(20)
def click_show_case_details(driver):
    driver.find_element_by_xpath('
    time.sleep(10)
def save_case_details(driver, start_index, end_index):
    for i in range(start_index, end_index):
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
def main():
    chromedriver_path = "C:\\Users\\raghu\\Desktop\\Chromedriver\\chromedriver.exe"
    url = "http:
    district_value = "25"
    complex_name = "District and Sessions Court, Shivajinagar, Pune - 411 005"
    from_date_xpath = '
    from_month_year_value = "1/2019"
    from_day_xpath = '/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/a'
    to_date_xpath = '
    to_month_year_value = "1/2019"
    to_day_xpath = '/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]/a'
    driver = initialize_webdriver(chromedriver_path)
    navigate_to_page(driver, url)
    select_district(driver, district_value)
    navigate_to_court_page(driver)
    switch_to_frame(driver, 'data')
    select_court_complex(driver, complex_name)
    set_date(driver, from_date_xpath, from_month_year_value, from_day_xpath)
    set_date(driver, to_date_xpath, to_month_year_value, to_day_xpath)
    wait_for_captcha()
    click_show_case_details(driver)
    save_case_details(driver, start_index=2, end_index=7)
    driver.quit()
if __name__ == "__main__":
    main()