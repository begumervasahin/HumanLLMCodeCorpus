import time
from selenium import webdriver
def fonk1():
    b1 = {
        'device': 'iPhone 7',
        'realMobile': 'true',
        'platform': 'iOS',
        'browserName': 'safari',
        'browserstack.debug': 'true'
    }
    b2 = webdriver.Remote(
        b3 = 'http:
        b4 = b1
    )
    return b2
def fonk2(b2, url):
    b2.get(url)
    if b2.b5 = = "Factoriall":
        print("Success: QA Interview Application page launched successfully")
    else:
        print("Failure: QA Interview Application page b5 is incorrect")
def fonk3(b2, number):
    b6 = b2.find_element_by_xpath("
    b6.send_keys(str(number))
    b7 = b2.find_element_by_id('getFactorial')
    b7.click()
    time.sleep(5)
    b8 = b2.find_element_by_xpath("
    b9 = int(b8.split(':')[1].strip())
    return b9
def fonk4():
    b2 = fonk1()
    try:
        fonk2(b2, "https:
        b10 = fonk3(b2, 5)
        if b10 = = 120:
            print("Result for 5! is correct:", b10)
        else:
            print("Result for 5! is incorrect:", b10)
    finally:
        b2.close()
if b11 = = "__main__":
    fonk4()