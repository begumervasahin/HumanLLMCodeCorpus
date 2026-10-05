import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def start():
    browser = webdriver.Chrome('chromedriver.exe')
    url = 'http:
    tag = 'gerbun.htm'
    browser.get(url + tag)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    divTag = soup.find_all("div", {"id": "main"})
    h5Tag = divTag[0].find_all('h5')
    p_list = []
    for i in h5Tag:
        team = i.text
        team_url = url + i.find("a").get("href")
        browser.get(team_url)
        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")
        divTag = soup.find_all("div", {"id": "main"})
        tableTag = divTag[0].find_all('table')
        trTag = tableTag[0].find('tbody').find_all('tr')
        for j in range(1, len(trTag)):
            temp = []
            tdTag = trTag[j].find_all('td')
            try:
                if tdTag[1].text:
                    temp.append(tdTag[1].text)
                    temp.append(tdTag[2].text)
                    temp.append(tdTag[3].text)
                    temp.append(team)
                    p_list.append(temp)
            except:
                break
    browser.quit()
    return p_list
player_list = start()
for player_info in player_list:
    print(player_info)