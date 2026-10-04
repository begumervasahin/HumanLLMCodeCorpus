from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
b1 = webdriver.Firefox(executable_path='D:\geckodriver\geckodriver.exe')
b1.get("http:
b1.find_element_by_id('fecha_salida').click()
b1.find_element_by_id('fecha_salida').send_keys('2019-08-14')
b1.find_element_by_id('fecha_salida').click()
sleep(1)
b2 = b1.find_element_by_xpath("
b3 = b2.find_elements_by_tag_name("option")
for flight in b3:
    flight.click()
    print(flight.get_attribute('value'))
    sleep(1)
    b4 = b1.find_element_by_xpath("
    b5 = b4.find_elements_by_tag_name("option")
    for hotel in b5:
        hotel.click()
        print(hotel.get_attribute('value'))
sleep(100)
b1.close()