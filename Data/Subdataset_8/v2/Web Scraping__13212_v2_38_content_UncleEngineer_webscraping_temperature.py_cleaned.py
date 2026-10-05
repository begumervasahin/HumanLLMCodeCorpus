
from urllib.request import urlopen as open_url
from bs4 import BeautifulSoup as parse_html
import songline
def get_province_temperature(province_id):
    try:
        url = 'https:
        with open_url(url) as web_data:
            page_html = web_data.read()
        web_data.close()
        parsed_data = parse_html(page_html, 'html.parser')
        temperature = parsed_data.findAll('td', {'class': 'strokeme'})[0].text
        province_name = parsed_data.findAll('span', {'class': 'title'})[0].text.replace('Â ', '')
        print(f'Province: {province_name}, Temperature: {temperature}')
        message_text = f'Province: {province_name}, Temperature: {temperature}'
        return message_text
    except Exception as e:
        print('Error:', e)
        return 'No Result'
def main():
    songline_token = 'Your_Songline_Token_Here'
    messenger = songline.Sendline(songline_token)
    province_id = 2
    province_temperature = get_province_temperature(province_id)
    if province_temperature != 'No Result':
        messenger.sendtext(province_temperature)
if __name__ == "__main__":
    main()