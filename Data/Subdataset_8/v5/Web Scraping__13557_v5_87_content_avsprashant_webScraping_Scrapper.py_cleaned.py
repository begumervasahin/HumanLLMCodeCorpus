import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
chromedriver_path = "C:\\Users\\raghu\\Desktop\\Chromedriver\\chromedriver.exe"
url = "http:
driver = webdriver.Chrome(chromedriver_path)
driver.get(url)
driver.maximize_window()
def wait(seconds):
    time.sleep(seconds)
def click_element(xpath):
    driver.find_element_by_xpath(xpath).click()
def select_by_value(selector, value):
    dropdown = Select(selector)
    dropdown.select_by_value(value)
def select_by_visible_text(selector, text):
    dropdown = Select(selector)
    dropdown.select_by_visible_text(text)
district_selector = driver.find_element_by_class_name("selectdistrict")
select_by_value(district_selector, "25")
click_element("
wait(3)
click_element("
wait(5)
driver.switch_to.frame('data')
click_element("
court_complex_selector = driver.find_element_by_xpath("
select_by_visible_text(court_complex_selector, "District and Sessions Court, Shivajinagar, Pune - 411 005")
click_element("
wait(2)
month_year_selector = driver.find_element_by_class_name("datepick-month-year")
select_by_value(month_year_selector, "1/2019")
click_element("/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[3]/a")
wait(2)
click_element("
wait(2)
click_element("/html/body/div[2]/div/div[2]/div/div/select[1]/option[1]")
wait(2)
click_element("/html/body/div[2]/div/div[2]/div/table/tbody/tr[1]/td[4]/a")
print("ENTER CAPTCHA AND WAIT for 10 seconds")
wait(20)
click_element("
wait(10)
start_row = 2
for i in [3, 4, 5, 6]:
    xpath_prefix = '
    xpath_suffix = ']/a'
    element_text = driver.find_element_by_xpath(xpath_prefix + str(i) + xpath_suffix).text
    filename = element_text.split(':')[0]
    rows = int(element_text.split(':')[1][1:])
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