import requests
from bs4 import BeautifulSoup
from task1 import top_scrape_list
import json
def extract_directors(plot_summary_wrapper):
    director_tags = plot_summary_wrapper.find('div', class_='credit_summary_item').find_all('a')
    return [director.text for director in director_tags]
def extract_country_and_language(title_details_section):
    country, language = [], []
    for txt_block in title_details_section.find_all('div', class_='txt-block'):
        h4_tag = txt_block.find('h4')
        if h4_tag:
            h4_text = h4_tag.text.strip()
            if h4_text == 'Country:':
                country = [a_tag.text for a_tag in txt_block.find_all('a')]
            elif h4_text == 'Language:':
                language = [a_tag.text for a_tag in txt_block.find_all('a')]
    return country, language
def scrape_movie_details(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    movie_details = {}
    title_wrapper = soup.find('div', class_='title_wrapper')
    movie_name = title_wrapper.find('h1').text.strip().split('(')[0].strip()
    movie_details["name"] = movie_name
    plot_summary_wrapper = soup.find('div', class_='plot_summary_wrapper')
    bio_text = plot_summary_wrapper.find('div', class_='summary_text').text.strip()
    movie_details["bio"] = bio_text
    directors = extract_directors(plot_summary_wrapper)
    movie_details["director"] = directors
    title_details_section = soup.find('div', {'class': 'article', 'id': 'titleDetails'})
    country, language = extract_country_and_language(title_details_section)
    movie_details["country"] = country
    movie_details["language"] = language
    poster_url = soup.find('div', class_='poster').find('img')['src']
    movie_details["poster_url"] = poster_url
    runtime_text = soup.find('div', class_='subtext').find('time').text.strip()
    movie_details["runtime"] = runtime_text
    genre_tags = soup.find('div', class_='subtext').find_all('a')
    genres = [genre.text for genre in genre_tags][:-1]
    movie_details["genre"] = genres
    return movie_details
if __name__ == "__main__":
    movie_url = 'https:
    movie_details = scrape_movie_details(movie_url)
    print(json.dumps(movie_details, indent=4))