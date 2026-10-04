import requests
import re
import json
from bs4 import BeautifulSoup
from stop_words import get_stop_words
from tabulate import tabulate
def get_word_list(url):
    word_list = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    for text in soup.find_all('p'):
        if text.text:
            words = text.text.lower().split()
            cleaned_words = [clean_word(word) for word in words if clean_word(word)]
            word_list.extend(cleaned_words)
    return word_list
def clean_word(word):
    return re.sub('[^A-Za-z]+', '', word)
def create_frequency_table(word_list):
    word_count = {}
    for word in word_list:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
def remove_stop_words(frequency_list):
    stop_words = set(get_stop_words('en'))
    return [item for item in frequency_list if item[0] not in stop_words]
def main(string_query, search_mode=False):
    wikipedia_api_link = "https:
    wikipedia_link = "https:
    url = wikipedia_api_link + string_query
    try:
        response = requests.get(url)
        data = response.json()
        wikipedia_page_tag = data['query']['search'][0]['title']
        page_url = wikipedia_link + wikipedia_page_tag
        word_list = get_word_list(page_url)
        frequency_table = create_frequency_table(word_list)
        sorted_frequency_list = sorted(frequency_table.items(), key=lambda item: item[1], reverse=True)
        if search_mode:
            sorted_frequency_list = remove_stop_words(sorted_frequency_list)
        total_words = sum(count for _, count in sorted_frequency_list)
        top_words = sorted_frequency_list[:20]
        final_list = [[word, count, round((count * 100) / total_words, 4)] for word, count in top_words]
        headers = ['Word', 'Frequency', 'Frequency Percentage']
        print(tabulate(final_list, headers=headers, tablefmt='orgtbl'))
    except requests.exceptions.Timeout:
        print("The server didn't respond. Please, try again later.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Enter a valid string query.")
        exit()
    query = sys.argv[1]
    search_mode = len(sys.argv) > 2
    main(query, search_mode)