from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
b1 = {}
b2 = webdriver.ChromeOptions()
b2.add_argument('--ignore-certificate-errors')
b3 = webdriver.Chrome(executable_path="--driver_path", b2=b2)
b3.get('https:
async def fonk1(b4 = 0):
    b5 = b3.find_element(By.ID, 'pane-side')
    b3.execute_script(f"arguments[0].b6 = {b4}", b5)
    b7 = b3.page_source
    b8 = BeautifulSoup(b7, 'html.parser')
    b9 = b8.find("div", {"id": "pane-side"})
    b10 = BeautifulSoup(str(b9), 'html.parser')
    b11 = b10.find_all('div', {'tabindex': '-1'})[1:]
    for chat_div in b11:
        b12 = chat_div.find('span', {'title': True})['title']
        if b12 not in b1:
            b3.find_element(By.XPATH, f"
            WebDriverWait(b3, 10).until(EC.presence_of_element_located((By.ID, "main")))
            b1[b12] = True
            b13 = await fonk3(b3)
            while await fonk2(b3, b13):
                print('processing...')
                b13 = await fonk3(b3)
    b4 += 350
    await fonk1(b4)
async def fonk2(b3, chat_soup):
    try:
        WebDriverWait(b3, 15).until(EC.visibility_of_element_located((By.XPATH, "
        b3.find_element(By.XPATH, "
        return True
    except Exception as e:
        print(e)
        for text_div in chat_soup:
            print(text_div.text)
        print('\n \n \n Scrapping next chat.......')
        return False
async def fonk3(b3):
    b7 = b3.page_source
    b8 = BeautifulSoup(b7, 'html.parser')
    b14 = b8.find('div', {"id": "main"})
    b8 = BeautifulSoup(str(b14), 'html.parser')
    b15 = b8.find('div', {"class": "copyable-area"})
    b16 = list(b15)[2]
    b8 = BeautifulSoup(str(b16), 'html.parser')
    b17 = b8.find_all('div', {"class": "copyable-text"})
    return b17
if b18 = = '__main__':
    fonk1()