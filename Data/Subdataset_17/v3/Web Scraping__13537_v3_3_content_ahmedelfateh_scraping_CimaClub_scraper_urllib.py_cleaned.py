import requests
from bs4 import BeautifulSoup
import csv
def fetch_page_content(url):
    response = requests.get(url)
    return response.content
def parse_movies(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.findAll("div", {"class": "movie"})
def extract_movie_details(movie):
    title_container = movie.find("div", {"class": "boxcontentFilm"})
    title = title_container.h2.text if title_container and title_container.h2 else "No Title"
    description = title_container.p.text if title_container and title_container.p else "No Description"
    category_container = movie.find("span", {"class": "category"})
    category = category_container.text if category_container else "No Category"
    views_container = movie.find("span", {"class": "views"})
    view = views_container.text if views_container else "No Views"
    movie_url = movie.a["href"] if movie.a else "No URL"
    return title, description, category, view, movie_url
def write_to_csv(file_name, headers, movies):
    with open(file_name, "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for movie in movies:
            details = extract_movie_details(movie)
            writer.writerow([detail.replace(",", " ") for detail in details])
def main():
    url = 'http:
    output_file = "todayHomepage.csv"
    headers = ["Title", "Description", "Category", "View", "Movie URL"]
    html_content = fetch_page_content(url)
    movies = parse_movies(html_content)
    write_to_csv(output_file, headers, movies)
    print(f"Data has been written to {output_file}")
if __name__ == "__main__":
    main()