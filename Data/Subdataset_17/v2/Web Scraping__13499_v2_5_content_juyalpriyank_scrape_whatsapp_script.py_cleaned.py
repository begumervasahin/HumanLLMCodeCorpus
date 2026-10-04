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
    target = driver.find_element(By.ID, 'pane-side')
    driver.execute_script(f"arguments[0].scrollTop = {scroll}", target)
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    left_panel = soup.find("div", {"id": "pane-side"})
    left_panel_soup = BeautifulSoup(str(left_panel), 'html.parser')
    chat_div_list = left_panel_soup.findAll('div', {'tabindex': '-1'})[1:]
    for chat_div in chat_div_list:
        chat_name = chat_div.find('span', {'title': True})['title']
        if chat_name not in already_scraped:
            driver.find_element(By.XPATH, f"
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "main")))
            already_scraped[chat_name] = True
            reloaded_soup = await reload_soup(driver)
            while await print_to_console(driver, reloaded_soup):
                reloaded_soup = await reload_soup(driver)
    scroll += 350
    await start_scrape(scroll)
async def print_to_console(driver, chat_content):
    try:
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "
')]")))
        driver.find_element(By.XPATH, "
')]").location_once_scrolled_into_view
        return True
    except Exception as e:
        reloaded_soup = await reload_soup(driver)
        print(e)
        for text_div in reloaded_soup:
            print(text_div.text)
        print('\n \n \n Scrapping next chat.......')
        return False
async def reload_soup(driver):
    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')
    main_div = soup.find('div', {"id": "main"})
    soup = BeautifulSoup(str(main_div), 'html.parser')
    copyable_area = soup.find('div', {"class": "copyable-area"})
    copyable_area = list(copyable_area)[2]
    soup = BeautifulSoup(str(copyable_area), 'html.parser')
    chat_texts = soup.findAll('div', {"class": "copyable-text"})
    return chat_texts
def launch_browser():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_scrape())
if __name__ == '__main__':
    launch_browser()