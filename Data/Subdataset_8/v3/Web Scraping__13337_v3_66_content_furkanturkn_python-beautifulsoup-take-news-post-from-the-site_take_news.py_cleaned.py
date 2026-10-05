import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import datetime
from unidecode import unidecode
def fetch_news_urls():
    world_url = "http:
    tech_url = "http:
    politics_url = "http:
    response_world = requests.get(world_url)
    response_tech = requests.get(tech_url)
    response_politics = requests.get(politics_url)
    soup_world = BeautifulSoup(response_world.content, "xml")
    soup_tech = BeautifulSoup(response_tech.content, "xml")
    soup_politics = BeautifulSoup(response_politics.content, "xml")
    items_world = soup_world.findAll('item')
    items_tech = soup_tech.findAll('item')
    items_politics = soup_politics.findAll('item')
    news_urls = []
    for i in range(20):
        news_urls.append(items_world[i].contents[5].text)
        news_urls.append(items_politics[i].contents[5].text)
        news_urls.append(items_tech[i].contents[5].text)
    return news_urls
def download_images(img_list, haber_url_control, PathControl):
    for i, img_url in enumerate(img_list):
        img_filename = os.path.join(PathControl, f"{i}_{haber_url_control}.jpg")
        urllib.request.urlretrieve(img_url, img_filename)
def extract_content(soup_content):
    title = soup_content.find("h1", {"class": "story-body__h1"})
    wp_title = title.text if title else ''
    description = soup_content.find("meta", {"name": "description"}).get("content")
    wp_description = description
    html_content = ""
    for paragraph in soup_content.find("div", {"class": "story-body__inner"}).findAll(['p', 'h2']):
        if paragraph.name == "h2":
            html_content += f"<h2>{paragraph.text}</h2><br><br>"
        else:
            html_content += f"{paragraph.text}<br><br>"
    return wp_title, wp_description, html_content
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
def process_news_article(news_url):
    try:
        Path = "C:/Users/Administrator/Desktop/Haberler/BBC_News/"
        haber_url_control = news_url[-8:]
        print('Haber ID:', haber_url_control)
        response_content = requests.get(news_url)
        soup_content = BeautifulSoup(response_content.content, "html.parser")
        images = soup_content.findAll("span", {"class": "image-and-copyright-container"})
        img_list = [img.split('src="')[1].split('"')[0] for img in images if "BBC Stories logo" not in img]
        PathControl = os.path.join(Path, haber_url_control)
        create_directory(PathControl)
        download_images(img_list, haber_url_control, PathControl)
        wp_title, wp_description, html_content = extract_content(soup_content)
        with open(os.path.join(PathControl, "Content.html"), "w", encoding='utf-8') as file:
            file.write(html_content)
    except Exception as e:
        print(f"Error processing article {news_url}: {e}")
def main():
    print("BBC News\n")
    news_urls = fetch_news_urls()
    for yazisayi in range(60):
        if yazisayi < len(news_urls):
            process_news_article(news_urls[yazisayi])
if __name__ == "__main__":
    main()