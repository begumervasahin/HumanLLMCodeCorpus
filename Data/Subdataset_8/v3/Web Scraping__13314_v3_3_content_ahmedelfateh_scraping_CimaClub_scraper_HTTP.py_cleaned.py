from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
def fetch_url_content(url):
    try:
        response = urlopen(url)
        if response.getcode() == 200:
            return response.read()
        else:
            return None
    except Exception as e:
        print("Error fetching URL:", e)
        return None
def extract_movie_details(movie):
    title_elem = movie.find("div", {"class": "boxcontentFilm"}).h2
    title = title_elem.text.strip() if title_elem else "N/A"
    description_elem = movie.find("div", {"class": "boxcontentFilm"}).p
    description = description_elem.text.strip() if description_elem else "N/A"
    category_elem = movie.find("span", {"class": "category"})
    category = category_elem.text.strip() if category_elem else "N/A"
    views_elem = movie.find("span", {"class": "views"})
    views = views_elem.text.strip() if views_elem else "N/A"
    movie_url = movie.a["href"] if movie.a else "N/A"
    return title, description, category, views, movie_url
def write_to_csv(file, data):
    with open(file, "w", encoding="utf-8") as f:
        headers = "Title, Description, Category, Views, Movie URL\n"
        f.write(headers)
        for row in data:
            f.write(",".join(row) + "\n")
def main():
    url = 'http:
    webpage_content = fetch_url_content(url)
    if webpage_content:
        page_soup = soup(webpage_content, "html.parser")
        movies = page_soup.findAll("div", {"class": "movie"})
        output_file = "todayHomepage.csv"
        movie_data = []
        for movie in movies:
            title, description, category, views, movie_url = extract_movie_details(movie)
            movie_data.append([title, description, category, views, movie_url])
        write_to_csv(output_file, movie_data)
        print("Data saved to", output_file)
    else:
        print("Failed to fetch the webpage.")
if __name__ == "__main__":
    main()