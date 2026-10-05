import pandas as pd
import requests
from bs4 import BeautifulSoup
def scrape_mlb_pitchers():
    mlb_url = "http:
    mlb_response = requests.get(mlb_url)
    mlb_soup = BeautifulSoup(mlb_response.content, 'lxml')
    pitchers = mlb_soup.find_all('a')
    del pitchers[:243]
    stopwords = ['x', '\n\n', '', 'Facebook', 'Twitter', 'Google Plus', 'Terms of Use', 'Career stats',
                 'Privacy Policy (updated January 20, 2016)', 'MLB.TV', 'About Our Ads', 'At Bat with Audio',
                 'Legal Notices', 'Back To Top', 'Contact Us', 'View MLB.com in English', 'En EspaÃ±ol']
    filtered_pitchers = [pitcher.text for pitcher in pitchers if pitcher.text not in stopwords]
    return filtered_pitchers
def scrape_fangraphs():
    fangraphs_url = "https:
    fangraphs_response = requests.get(fangraphs_url)
    fangraphs_soup = BeautifulSoup(fangraphs_response.content, 'lxml')
    table = fangraphs_soup.find_all('table', id="LeaderBoard1_dg1_ctl00")
    df = pd.read_html(str(table))[0]
    df.drop(df.tail(1).index, inplace=True)
    return df
def main():
    mlb_pitchers = scrape_mlb_pitchers()
    print("Today's Starting Pitchers:")
    for pitcher in mlb_pitchers:
        print(pitcher)
    fangraphs_data = scrape_fangraphs()
    print("\nFangraphs Data:")
    print(fangraphs_data)
if __name__ == "__main__":
    main()