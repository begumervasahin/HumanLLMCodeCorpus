import csv
from bs4 import BeautifulSoup
from workfiles.getUrlData import simple_get
def fetch_movie_data(url):
    try:
        response = simple_get(url)
        if response is None:
            print(f"Failed to retrieve data from {url}")
            return None
        return response
    except Exception as e:
        print(f"An error occurred while fetching data: {e}")
        return None
def parse_movie_data(page_html):
    page_soup = BeautifulSoup(page_html, "html.parser")
    return page_soup.findAll("div", {"class": "movie"})
def extract_movie_details(movie):
    title = movie.find("div", {"class": "boxcontentFilm"}).h2.text
    description = movie.find("div", {"class": "boxcontentFilm"}).p.text
    category = movie.find("span", {"class": "category"}).text
    view = movie.find("span", {"class": "views"}).text
    movie_url = movie.a["href"]
    return title, description, category, view, movie_url
def save_movie_data(file_name, headers, movies):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for movie in movies:
            writer.writerow(movie)
def main():
    my_url = 'http:
    page_html = fetch_movie_data(my_url)
    if page_html is None:
        print("No data to process. Exiting.")
        return
    movies = parse_movie_data(page_html)
    if not movies:
        print("No movies found on the page.")
        return
    movie_details = []
    for movie in movies:
        try:
            details = extract_movie_details(movie)
            movie_details.append(details)
        except AttributeError as e:
            print(f"An error occurred while parsing movie details: {e}")
            continue
    headers = ["Title", "Description", "Category", "Views", "Movie URL"]
    save_movie_data("todayHomepage.csv", headers, movie_details)
    print(f"Data saved to todayHomepage.csv")
if __name__ == "__main__":
    main()