import requests
from bs4 import BeautifulSoup
def fetch_html(url):
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        print("Error fetching HTML:", e)
        return None
def get_title(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.title.string
        return title
    except Exception as e:
        print("Error extracting title:", e)
        return None
def get_body(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        body = soup.body
        return body
    except Exception as e:
        print("Error extracting body:", e)
        return None
def get_text_paragraphs(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        text_paragraphs = soup.find_all('p')
        return text_paragraphs
    except Exception as e:
        print("Error extracting text paragraphs:", e)
        return None
def get_head_section(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        head_section = soup.head
        return head_section
    except Exception as e:
        print("Error extracting head section:", e)
        return None
def get_links(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        links = soup.find_all('a')
        return links
    except Exception as e:
        print("Error extracting links:", e)
        return None
def get_images(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        images = soup.find_all('img')
        return images
    except Exception as e:
        print("Error extracting images:", e)
        return None
url = "https:
html_content = fetch_html(url)
if html_content is None:
    print("Failed to fetch HTML content.")
else:
    title = get_title(html_content)
    print("*** Title: ***")
    print(title if title else "Title not found")
    body = get_body(html_content)
    print("\n*** Body: ***")
    print(body if body else "Body not found")
    text_paragraphs = get_text_paragraphs(html_content)
    print("\n*** Text Paragraphs: ***")
    if text_paragraphs:
        for paragraph in text_paragraphs:
            print(paragraph.get_text())
    head_section = get_head_section(html_content)
    print("\n*** Head Section: ***")
    print(head_section if head_section else "Head section not found")
    links = get_links(html_content)
    print("\n*** Links: ***")
    if links:
        for link in links:
            if "href" in link.attrs:
                print(link.attrs["href"])
    images = get_images(html_content)
    print("\n*** Images: ***")
    if images:
        for image in images:
            if "src" in image.attrs:
                print(image.attrs["src"])