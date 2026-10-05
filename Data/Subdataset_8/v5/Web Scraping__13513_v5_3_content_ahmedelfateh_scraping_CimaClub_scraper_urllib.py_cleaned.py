import urllib.request
from bs4 import BeautifulSoup
url = 'http:
with urllib.request.urlopen(url) as response:
    html_content = response.read()
soup = BeautifulSoup(html_content, "html.parser")
movies = soup.find_all("div", class_="movie")
file_name = "todayHomepage.csv"
with open(file_name, "w") as file:
    headers = "title, description, category, view, movieUrl\n"
    file.write(headers)
    for movie in movies:
        title = movie.find("div", class_="boxcontentFilm").h2.text
        description = movie.find("div", class_="boxcontentFilm").p.text
        category = movie.find("span", class_="category").text
        view = movie.find("span", class_="views").text
        movie_url = movie.a["href"]
        print("Title:", title)
        print("Description:", description)
        print("Category:", category)
        print("Views:", view)
        print("Movie URL:", movie_url)
        file.write(f"{title.replace(',', ' ')}, {description.replace(',', ' ')}, "
                   f"{category.replace(',', ' ')}, {view.replace(',', ' ')}, {movie_url.replace(',', ' ')}\n")
print("Data has been successfully written to", file_name)