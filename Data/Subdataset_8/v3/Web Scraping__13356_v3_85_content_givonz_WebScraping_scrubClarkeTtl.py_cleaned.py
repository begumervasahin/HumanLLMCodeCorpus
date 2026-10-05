from bs4 import BeautifulSoup
from urllib.request import urlopen
def get_all_links(web_page, file_names, file_common_names, file_symptoms):
    clarke_start = urlopen(web_page).read()
    soup = BeautifulSoup(clarke_start, "html.parser")
    links = soup.find_all("a")
    if not links:
        return
    for link in links[:-1]:
        href = link.get("href")
        if len(href) != 5 or href.endswith("index.htm"):
            continue
        page_url = "http:
        remedy_read = urlopen(page_url).read()
        soup2 = BeautifulSoup(remedy_read, "html.parser")
        paragraphs = soup2.find_all("p")
        name = extract_text(paragraphs[2])
        common_names = extract_text(paragraphs[3])
        diseases = extract_diseases(soup2)
        file_names.write(name + "\n")
        file_common_names.write(format_common_names(common_names) + "\n")
        file_symptoms.write(clean_text(diseases) + "\n")
        break
def extract_text(tag_text):
    return tag_text.get_text()
def format_common_names(common_names):
    return common_names[1:].replace("(", "").replace(")", "")
def extract_diseases(soup):
    info = soup.get_text()
    start = info.find("Clinical")
    end = info.find("</blockquote>", start)
    return info[start + 8:end].strip()
def clean_text(text):
    return text.replace("<i>", " 2").replace('<font color="', "").replace("</font>", "").replace("</i>", "").replace("\n", "").replace("        ", " ")
def main():
    with open("h-remedies.csv", "w") as file_names, \
         open("commonRemedyNames.csv", "w") as file_common_names, \
         open("remedy-symptoms.csv", "w") as file_symptoms:
        for char_code in range(97, 123):
            web_page = "http:
            get_all_links(web_page, file_names, file_common_names, file_symptoms)
if __name__ == "__main__":
    main()