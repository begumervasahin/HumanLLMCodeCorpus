from bs4 import BeautifulSoup as soup
from workfiles.getUrlData import simple_get
def fetch_movie_data(url):
    response = simple_get(url)
    page_soup = soup(response, "html.parser")
    movies = page_soup.findAll("div", {"class": "movie"})
    movie_data = []
    for movie in movies:
        title = movie.find("div", {"class": "boxcontentFilm"}).h2.text
        description = movie.find("div", {"class": "boxcontentFilm"}).p.text
        category = movie.find("span", {"class": "category"}).text
        view = movie.find("span", {"class": "views"}).text
        movie_url = movie.a["href"]
        movie_data.append({
            "title": title.replace(",", " "),
            "description": description.replace(",", " "),
            "category": category.replace(",", " "),
            "view": view.replace(",", " "),
            "movieUrl": movie_url.replace(",", " ")
        })
        print(f"title: {title}")
        print(f"description: {description}")
        print(f"category: {category}")
        print(f"views: {view}")
        print(f"movieUrl: {movie_url}")
    return movie_data
def save_to_csv(file_path, headers, data):
    with open(file_path, "w") as file:
        file.write(headers)
        for entry in data:
            row = f"{entry['title']}, {entry['description']}, {entry['category']}, {entry['view']}, {entry['movieUrl']}\n"
            file.write(row)
def main():
    url = 'http:
    headers = "title, description, category, view, movieUrl\n"
    file_path = "todayHomepage.csv"
    movie_data = fetch_movie_data(url)
    save_to_csv(file_path, headers, movie_data)
if __name__ == "__main__":
    main()