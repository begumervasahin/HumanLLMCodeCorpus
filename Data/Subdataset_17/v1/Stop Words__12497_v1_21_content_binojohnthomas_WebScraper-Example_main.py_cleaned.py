import requests
import re
import operator
import json
from tabulate import tabulate
from bs4 import BeautifulSoup
from stop_words import get_stop_words
def get_word_list(url):
    word_list = []
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'lxml')
    for text in soup.find_all('p'):
        if text.text is None:
            continue
        content = text.text
        words = content.lower().split()
        for word in words:
            cleaned_word = clean_word(word)
            if len(cleaned_word) > 0:
                word_list.append(cleaned_word)
    return word_list
def clean_word(word):
    return re.sub('[^A-Za-z]+', '', word)
def create_frequency_table(word_list):
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
def remove_stop_words(frequency_list):
    stop_words = get_stop_words('en')
    return [item for item in frequency_list if item[0] not in stop_words]
def main(string_query, search_mode=False):
    wikipedia_api_link = "https:
    wikipedia_link = "https:
    url = wikipedia_api_link + string_query
    try:
        response = requests.get(url)
        data = json.loads(response.content.decode("utf-8"))
        wikipedia_page_tag = data['query']['search'][0]['title']
        url = wikipedia_link + wikipedia_page_tag
        page_word_list = get_word_list(url)
        page_word_count = create_frequency_table(page_word_list)
        sorted_word_frequency_list = sorted(page_word_count.items(), key=operator.itemgetter(1), reverse=True)
        if search_mode:
            sorted_word_frequency_list = remove_stop_words(sorted_word_frequency_list)
        total_words_sum = sum([value for key, value in sorted_word_frequency_list])
        if len(sorted_word_frequency_list) > 20:
            sorted_word_frequency_list = sorted_word_frequency_list[:20]
        final_list = [[key, value, round((value * 100) / total_words_sum, 4)] for key, value in sorted_word_frequency_list]
        print_headers = ['Word', 'Frequency', 'Frequency Percentage']
        print(tabulate(final_list, headers=print_headers, tablefmt='orgtbl'))
    except requests.exceptions.Timeout:
        print("The server didn't respond. Please, try again later.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Enter a valid string query.")
        exit()
    string_query = sys.argv[1]
    search_mode = len(sys.argv) > 2
    main(string_query, search_mode)