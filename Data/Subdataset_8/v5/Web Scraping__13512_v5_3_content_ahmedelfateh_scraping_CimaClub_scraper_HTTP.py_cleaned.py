from bs4 import BeautifulSoup as soup
from workfiles.getUrlData import simple_get
def extract_text_from_element(element):
    return element.text.strip() if element else ""
url = 'http:
html_content = simple_get(url)
page_soup = soup(html_content, "html.parser")
movies = page_soup.find_all("div", class_="movie")
csv_filename = "todayHomepage.csv"
csv_header = "title, description, category, view, movieUrl\n"
with open(csv_filename, "w") as csv_file:
    csv_file.write(csv_header)
    for movie in movies:
        title_element = movie.find("div", class_="boxcontentFilm").h2
        title = extract_text_from_element(title_element)
        description_element = movie.find("div", class_="boxcontentFilm").p
        description = extract_text_from_element(description_element)
        category_element = movie.find("span", class_="category")
        category = extract_text_from_element(category_element)
        view_element = movie.find("span", class_="views")
        view = extract_text_from_element(view_element)
        movie_url = movie.a["href"]
        print("Title:", title)
        print("Description:", description)
        print("Category:", category)
        print("Views:", view)
        print("Movie URL:", movie_url)
        csv_file.write(f"{title.replace(',', ' ')}, {description.replace(',', ' ')}, "
                       f"{category.replace(',', ' ')}, {view.replace(',', ' ')}, {movie_url.replace(',', ' ')}\n")
print("Data extraction completed.")