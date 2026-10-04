import requests
from bs4 import BeautifulSoup
def fetch_yelp_data(location, max_pages=200, page_increment=10):
    """
    Fetches restaurant data from Yelp for a given location and writes it to a text file.
    Args:
        location (str): The location to search for restaurants (e.g., "New York,NY").
        max_pages (int): The maximum number of pages to fetch.
        page_increment (int): The number of results to skip per page.
    Returns:
        None
    """
    base_url = "https:
    current_page = 0
    file_path = f"yelp-{location}.txt"
    with open(file_path, "w") as textfile:
        while current_page <= max_pages:
            url = f"{base_url}{location}&start={current_page}"
            response = requests.get(url)
            print(f"Fetching page {current_page
            soup = BeautifulSoup(response.text, "html.parser")
            businesses = soup.find_all("div", {"class": "biz-listing-large"})
            for biz in businesses:
                title = extract_title(biz)
                address_1, address_2 = extract_address(biz)
                phone = extract_phone(biz)
                print(title)
                print(address_1)
                print(address_2)
                print(phone)
                textfile.write(f"{title}\n{address_1}\n{address_2}\n{phone}\n\n")
            current_page += page_increment
def extract_title(biz):
    return biz.find("a", {"class": "biz-name"}).text.strip()
def extract_address(biz):
    address = biz.find("address")
    if address:
        address_lines = address.contents
        first_line = address_lines[0].strip(" \n\tr") if address_lines else ""
        second_line = address_lines[1].strip(" \n\tr") if len(address_lines) > 1 else ""
    else:
        first_line = second_line = ""
    return first_line, second_line
def extract_phone(biz):
    phone = biz.find("span", {"class": "biz-phone"})
    return phone.text.strip(" \n\t\r") if phone else "N/A"
if __name__ == "__main__":
    location = "New York,NY"
    fetch_yelp_data(location)