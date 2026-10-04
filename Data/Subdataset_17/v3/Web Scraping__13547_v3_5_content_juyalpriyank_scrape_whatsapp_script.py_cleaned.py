from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import asyncio
already_scraped = {}
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(executable_path='path_to_chromedriver', options=options)
driver.get('https:
async def start_scrape(scroll=0):
    scroll_chat_list(scroll)
    chat_div_list = get_chat_list()
    for chat_div in chat_div_list:
        chat_name = get_chat_name(chat_div)
        if chat_name not in already_scraped:
            await process_chat(chat_name)
    await start_scrape(scroll + 350)
def scroll_chat_list(scroll):
    target = driver.find_element(By.ID, 'pane-side')
    driver.execute_script(f"arguments[0].scrollTop = {scroll}", target)
def get_chat_list():
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    left_panel = soup.find("div", {"id": "pane-side"})
    left_panel_soup = BeautifulSoup(str(left_panel), 'html.parser')
    return left_panel_soup.findAll('div', {'tabindex': '-1'})[1:]
def get_chat_name(chat_div):
    return chat_div.find('span', {'title': True})['title']
async def process_chat(chat_name):
    click_chat(chat_name)
    await wait_for_chat_to_load()
    already_scraped[chat_name] = True
    reloaded_soup = await reload_soup(driver)
    while await print_to_console(driver, reloaded_soup):
        reloaded_soup = await reload_soup(driver)
def click_chat(chat_name):
    driver.find_element(By.XPATH, f"
async def wait_for_chat_to_load():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "main")))
async def print_to_console(driver, chat_content):
    if await load_earlier_messages(driver):
        return True
    else:
        for text_div in chat_content:
            print(text_div.text)
        print('\n \n \n Scraping next chat.......')
        return False
async def load_earlier_messages(driver):
    try:
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "
')]")))
        driver.find_element(By.XPATH, "
')]").location_once_scrolled_into_view
        return True
    except Exception:
        return False
async def reload_soup(driver):
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    main_div = soup.find('div', {"id": "main"})
    soup = BeautifulSoup(str(main_div), 'html.parser')
    copyable_area = soup.find('div', {"class": "copyable-area"})
    copyable_area = list(copyable_area)[2]
    soup = BeautifulSoup(str(copyable_area), 'html.parser')
    return soup.findAll('div', {"class": "copyable-text"})
def launch_browser():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_scrape())
if __name__ == '__main__':
    launch_browser()