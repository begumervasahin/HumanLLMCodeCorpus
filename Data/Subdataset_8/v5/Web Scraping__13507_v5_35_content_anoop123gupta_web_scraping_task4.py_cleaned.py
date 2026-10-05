import requests
from bs4 import BeautifulSoup
from task1 import top_scrape_list
def scrape_movie_details(url):
    movies = top_scrape_list()
    movie_details = {}
    response = requests.get(url)
    html_content = response.text
    parsed_page = BeautifulSoup(html_content, "html.parser")
    title_wrapper = parsed_page.find('div', class_='title_wrapper')
    movie_name = title_wrapper.find('h1').text.split('(')[0].strip()
    movie_details["name"] = movie_name
    plot_summary_wrapper = parsed_page.find('div', class_='plot_summary_wrapper')
    summary_text = plot_summary_wrapper.find('div', class_='summary_text').text.strip()
    movie_details["bio"] = summary_text
    credit_summary_item = plot_summary_wrapper.find('div', class_='credit_summary_item')
    director = credit_summary_item.find('a').text
    movie_details["director"] = [director]
    title_details = parsed_page.find('div', attrs={"class": "article", "id": "titleDetails"})
    details_blocks = title_details.find_all('div', class_='txt-block')
    for block in details_blocks:
        heading = block.find('h4').text
        if heading == 'Country:':
            countries = block.find_all('a')
            country_names = [country.text for country in countries]
            movie_details["country"] = country_names
        elif heading == 'Language:':
            languages = block.find_all('a')
            language_names = [language.text for language in languages]
            movie_details["language"] = language_names
    poster_div = parsed_page.find('div', class_='poster')
    poster_url = poster_div.find('img').get('src')
    movie_details["poster_url"] = poster_url
    subtext_div = parsed_page.find('div', class_='subtext')
    time_tag = subtext_div.find('time')
    runtime_hours = int(time_tag.text.strip('min').strip('h')) * 60 if 'h' in time_tag.text else 0
    runtime_minutes = int(time_tag.text.strip('min').strip()) if 'min' in time_tag.text else 0
    total_runtime = runtime_hours + runtime_minutes
    movie_details["runtime"] = f"{total_runtime} min"
    genre_tags = subtext_div.find_all('a')
    genre_names = [genre.text for genre in genre_tags][:-1]
    movie_details["genre"] = genre_names
    return movie_details
movie_details = scrape_movie_details('https:
print(movie_details)