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
def main():
    url = 'http:
    webpage_content = fetch_url_content(url)
    if webpage_content:
        page_soup = soup(webpage_content, "html.parser")
        movies = page_soup.findAll("div", {"class": "movie"})
        output_file = "todayHomepage.csv"
        with open(output_file, "w", encoding="utf-8") as save_file:
            headers = "Title, Description, Category, Views, Movie URL\n"
            save_file.write(headers)
            for movie in movies:
                title_list = movie.findAll("div", {"class": "boxcontentFilm"})
                title = title_list[0].h2.text.strip()
                description = title_list[0].p.text.strip()
                category_list = movie.findAll("span", {"class": "category"})
                category = category_list[0].text.strip()
                views_list = movie.findAll("span", {"class": "views"})
                view = views_list[0].text.strip()
                movie_url = movie.a["href"]
                print("Title:", title)
                print("Description:", description)
                print("Category:", category)
                print("Views:", view)
                print("Movie URL:", movie_url)
                save_file.write(f"{title.replace(',', ' ')}, {description.replace(',', ' ')}, {category.replace(',', ' ')}, {view.replace(',', ' ')}, {movie_url.replace(',', ' ')}\n")
        print("Data saved to", output_file)
    else:
        print("Failed to fetch the webpage.")
if __name__ == "__main__":
    main()