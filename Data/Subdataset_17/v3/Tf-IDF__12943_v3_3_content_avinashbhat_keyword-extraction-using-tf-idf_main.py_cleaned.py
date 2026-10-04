from scraper import linkify, getLinks, getWords
from algorithms import tf, getDocLinkStrength, idf, tfidf
def get_unique_links(docLinks):
    return list({link for link, _ in docLinks})
def fetch_words_from_links(links):
    words_list = []
    for link in links:
        linked_page = linkify(link)
        words_list.append(getWords(linked_page))
    return words_list
def calculate_tf_idf(tf_dict, words_dump):
    idf_dict = idf(tf_dict, words_dump)
    return tfidf(tf_dict, idf_dict)
def get_sorted_tfidf_list(tfidf_dict):
    return sorted(tfidf_dict.items(), key=lambda x: x[1], reverse=True)
def main():
    name = input("Enter the Name of the Personality: ")
    page_link = linkify(name)
    word_list = getWords(page_link)
    link_list = getLinks(page_link)
    tf_dict = tf(word_list)
    doc_links = getDocLinkStrength(link_list, tf_dict)
    unique_links = get_unique_links(doc_links)
    words_dump = fetch_words_from_links(unique_links[:10])
    tfidf_dict = calculate_tf_idf(tf_dict, words_dump)
    sorted_tfidf_list = get_sorted_tfidf_list(tfidf_dict)
    keywords = getDocLinkStrength(link_list, tfidf_dict)
    final_keyword_list = list({keyword for keyword, _ in keywords})
    for keyword in final_keyword_list:
        print(keyword)
if __name__ == "__main__":
    main()