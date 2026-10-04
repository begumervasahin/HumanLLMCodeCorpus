from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
b1 = {}
b2 = webdriver.ChromeOptions()
b2.add_argument('--ignore-certificate-errors')
b3 = webdriver.Chrome("--driver_path", b2=b2)
b3.get('https:
async def fonk1(b4 = 0):
    b5 = b3.find_element_by_id('pane-side')
    b3.execute_script(f"arguments[0].b6 = {b4}", b5)
    b7 = b3.page_source
    b8 = BeautifulSoup(b7, 'html.parser')
    b9 = b8.findAll("div", {"id": "pane-side"})[0]
    b10 = BeautifulSoup(str(b9), 'html.parser')
    b11 = b10.findAll('div', {'tabindex' : '-1'})[1:]
    for chat_div in b11:
        b12 = chat_div.find('span', {'title': True})['title']
        if b12 not in b1.keys():
            b3.find_element_by_xpath(f"
            b13 = WebDriverWait(b3, 10).until(EC.presence_of_element_located((By.ID, "main")))
            b1.update({b12: True})
            b14 = await fonk3(b3)
            while await fonk2(b3, b14):
                print('processing...')
                b14 = await fonk3(b3)
    b4 += 350
    fonk1(b4)
async def fonk2(b3, c):
    try:
        b13 = WebDriverWait(b3, 15).until(EC.visibility_of_element_located((By.XPATH, "
        b3.find_element_by_xpath("
        return True
    except Exception as e:
        b14 = await fonk3(b3)
        print(e)
        for text_div in b14:
            print(text_div.text)
        print('\n \n \n Scrapping next chat.......')
        return False
async def fonk3(b3):
    b7 = b3.page_source
    b8 = BeautifulSoup(b7, 'html.parser')
    b15 = b8.find('div', {"id" : "main"})
    b8 = BeautifulSoup(str(b15), 'html.parser')
    b16 = b8.find('div', {"class" : "copyable-area"})
    b16 = list(b16)[2]
    b8 = BeautifulSoup(str(b16), 'html.parser')
    b17 = b8.findAll('div',{"class" : "copyable-text"})
    return b17
if b18 = = '__main__':
    launch_browser()