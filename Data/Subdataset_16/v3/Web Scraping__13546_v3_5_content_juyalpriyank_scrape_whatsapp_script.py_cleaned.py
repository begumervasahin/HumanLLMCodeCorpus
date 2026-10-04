from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import asyncio
b1 = {}
b2 = webdriver.ChromeOptions()
b2.add_argument('--ignore-certificate-errors')
b3 = webdriver.Chrome(executable_path='path_to_chromedriver', b2=b2)
b3.get('https:
async def fonk1(b4 = 0):
    fonk2(b4)
    b5 = fonk3()
    for chat_div in b5:
        b6 = fonk4(chat_div)
        if b6 not in b1:
            await fonk5(b6)
    await fonk1(b4 + 350)
def fonk2(b4):
    b7 = b3.find_element(By.ID, 'pane-side')
    b3.execute_script(f"arguments[0].b8 = {b4}", b7)
def fonk3():
    b9 = b3.page_source
    b10 = BeautifulSoup(b9, 'html.parser')
    b11 = b10.find("div", {"id": "pane-side"})
    b12 = BeautifulSoup(str(b11), 'html.parser')
    return b12.findAll('div', {'tabindex': '-1'})[1:]
def fonk4(chat_div):
    return chat_div.find('span', {'title': True})['title']
async def fonk5(b6):
    fonk6(b6)
    await fonk7()
    b1[b6] = True
    b13 = await fonk10(b3)
    while await fonk8(b3, b13):
        b13 = await fonk10(b3)
def fonk6(b6):
    b3.find_element(By.XPATH, f"
async def fonk7():
    WebDriverWait(b3, 10).until(EC.presence_of_element_located((By.ID, "main")))
async def fonk8(b3, chat_content):
    if await fonk9(b3):
        return True
    else:
        for text_div in chat_content:
            print(text_div.text)
        print('\n \n \n Scraping next chat.......')
        return False
async def fonk9(b3):
    try:
        WebDriverWait(b3, 15).until(EC.visibility_of_element_located((By.XPATH, "
')]")))
        b3.find_element(By.XPATH, "
')]").location_once_scrolled_into_view
        return True
    except Exception:
        return False
async def fonk10(b3):
    b9 = b3.page_source
    b10 = BeautifulSoup(b9, 'html.parser')
    b14 = b10.find('div', {"id": "main"})
    b10 = BeautifulSoup(str(b14), 'html.parser')
    b15 = b10.find('div', {"class": "copyable-area"})
    b15 = list(b15)[2]
    b10 = BeautifulSoup(str(b15), 'html.parser')
    return b10.findAll('div', {"class": "copyable-text"})
def fonk11():
    b16 = asyncio.get_event_loop()
    b16.run_until_complete(fonk1())
if b17 = = '__main__':
    fonk11()