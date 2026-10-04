from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
def fetch_page_html(url):
    with uReq(url) as uClient:
        return uClient.read()
def parse_html_to_soup(html):
    return soup(html, "html.parser")
def extract_movie_data(movie):
    title = movie.find("div", {"class": "boxcontentFilm"}).h2.text
    description = movie.find("div", {"class": "boxcontentFilm"}).p.text
    category = movie.find("span", {"class": "category"}).text
    view = movie.find("span", {"class": "views"}).text
    movieUrl = movie.a["href"]
    return {
        "title": title,
        "description": description,
        "category": category,
        "view": view,
        "movieUrl": movieUrl
    }
def save_movies_to_csv(movies, filename):
    with open(filename, "w") as file:
        headers = "title,description,category,view,movieUrl\n"
        file.write(headers)
        for movie in movies:
            movie_data = extract_movie_data(movie)
            file.write(f"{movie_data['title'].replace(',', ' ')},"
                       f"{movie_data['description'].replace(',', ' ')},"
                       f"{movie_data['category'].replace(',', ' ')},"
                       f"{movie_data['view'].replace(',', ' ')},"
                       f"{movie_data['movieUrl'].replace(',', ' ')}\n")
def main():
    url = 'http:
    page_html = fetch_page_html(url)
    page_soup = parse_html_to_soup(page_html)
    movies = page_soup.findAll("div", {"class": "movie"})
    save_movies_to_csv(movies, "todayHomepage.csv")
if __name__ == "__main__":
    main()