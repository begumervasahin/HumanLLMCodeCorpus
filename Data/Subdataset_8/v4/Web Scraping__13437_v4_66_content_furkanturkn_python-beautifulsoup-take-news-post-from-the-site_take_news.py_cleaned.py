import requests
from bs4 import BeautifulSoup
import urllib.request
import collections
import os
import errno
import datetime
from unidecode import unidecode
print("BBC News" + "\n")
for article_count in range(60):
    try:
        base_path = "C:/Users/Administrator/Desktop/Haberler/BBC_News/"
        bbc_world_url = "http:
        bbc_tech_url = "http:
        bbc_politics_url = "http:
        r_world = requests.get(bbc_world_url)
        r_tech = requests.get(bbc_tech_url)
        r_politics = requests.get(bbc_politics_url)
        soup_world = BeautifulSoup(r_world.content, "xml")
        soup_tech = BeautifulSoup(r_tech.content, "xml")
        soup_politics = BeautifulSoup(r_politics.content, "xml")
        items_world = soup_world.findAll('item')
        items_tech = soup_tech.findAll('item')
        items_politics = soup_politics.findAll('item')
        world_list = []
        for i in range(20):
            world_list.append(items_world[i].contents[5].text)
            world_list.append(items_politics[i].contents[5].text)
            world_list.append(items_tech[i].contents[5].text)
        article_url = world_list[article_count]
        article_id = article_url[-8:]
        print('Article ID: ' + article_id)
        r_article_content = requests.get(article_url)
        soup_article = BeautifulSoup(r_article_content.content, "html.parser")
        image_list = []
        alt_text_list = []
        wp_category = "World"
        image_all = soup_article.findAll("span", {"class": "image-and-copyright-container"})
        for i in range(len(image_all)):
            if i % 2 == 0:
                img_px = str(image_all[i - 1])
                img_px = img_px.split('height="')
                img_px = int(img_px[1].split('"')[0])
                if img_px > 200:
                    img_src = str(image_all[i - 1]).split('src="')[1].split('"')[0]
                    alt_text = str(image_all[i - 1]).split('alt="')[1].split('"')[0]
                    if alt_text != "BBC Stories logo":
                        image_list.append(img_src)
                        alt_text_list.append(alt_text)
            else:
                continue
        thumbnail_img = soup_article.findAll('img', {"class": "js-image-replace"})
        if thumbnail_img:
            image_list.append(thumbnail_img[0]['src'])
            alt_text_list.append(thumbnail_img[0]['alt'])
        description = soup_article.find("meta", {"name": "description"}).get("content")
        wp_description = description
        article_text = soup_article.find("div", {"class": "story-body__inner"})
        if article_text:
            article_text = article_text.findAll(['p', 'h2'])
        else:
            continue
        title = soup_article.find("h1", {"class": "story-body__h1"})
        if title:
            wp_title = title.text
        else:
            wp_title = ""
        article_directory = base_path + article_id + "/"
        if not os.path.exists(os.path.dirname(article_directory)):
            os.makedirs(os.path.dirname(article_directory))
        for i in range(len(image_list)):
            urllib.request.urlretrieve(image_list[i], article_directory + "image_" + str(i) + ".jpg")
        stopwords = set()
        wordcount = {}
        for word in article_text.lower().split():
            word = word.strip(".,:!?*Ã¢â¬ÅÃ¢â¬Ë")
            if word not in stopwords:
                wordcount[word] = wordcount.get(word, 0) + 1
        sorted_wordcount = sorted(wordcount.items(), key=lambda x: x[1], reverse=True)
        keywords = [word for word, _ in sorted_wordcount[:1]]
        tags = ','.join([word for word, _ in sorted_wordcount[:7]])
        wp_title = wp_title.replace(":", "").replace("<", "").replace(">", "").replace("*", "").replace("?", "").replace("/", "").replace("|", "").replace('"', '')
        with open(article_directory + "Content.txt", "w", encoding='utf-8') as file:
            file.write(f"{wp_title}<--->{wp_description}<--->{keywords}<--->{tags}<--->{wp_category}<--->{','.join(alt_text_list)}")
        if not os.listdir(article_directory):
            os.rmdir(article_directory)
    except Exception as e:
        print("Error occurred:", e)
        if not os.listdir(article_directory):
            os.rmdir(article_directory)
        continue