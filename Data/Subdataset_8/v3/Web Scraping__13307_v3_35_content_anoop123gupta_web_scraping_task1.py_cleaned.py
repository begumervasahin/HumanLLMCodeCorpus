import requests
import json
import os
from bs4 import BeautifulSoup
def load_or_scrape_data():
    cache_file = "cache_file_for_task_1.json"
    if os.path.isfile(cache_file):
        return load_data_from_cache(cache_file)
    else:
        return scrape_imdb_website(cache_file)
def load_data_from_cache(cache_file):
    with open(cache_file, "r") as data_file:
        return json.load(data_file)
def scrape_imdb_website(cache_file):
    endpoint = 'https:
    response = requests.get(endpoint)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('tbody', class_='lister-list')
    if not table:
        raise ValueError("Failed to find movie data table on the webpage.")
    movies_list = []
    for rank, row in enumerate(table.find_all('tr'), start=1):
        movie_data = extract_movie_data(rank, row)
        movies_list.append(movie_data)
    write_to_cache(cache_file, movies_list)
    return movies_list
def extract_movie_data(rank, row):
    title_column = row.find('td', class_='titleColumn')
    title = title_column.find('a').text.strip()
    year = int(title_column.find('span').text[1:5])
    link = "https:
    rating = row.find('td', class_='ratingColumn imdbRating').text.strip()
    return {'Title': title, 'Rank': rank, 'Year': year, 'URL': link, 'Rating': rating}
def write_to_cache(cache_file, data):
    with open(cache_file, "w") as data_file:
        json.dump(data, data_file, indent=4)
def main():
    try:
        movies = load_or_scrape_data()
        print("Top-rated Indian movies data has been scraped and stored.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    main()