
from scraper import linkify, getLinks, getWords
from algorithms import tf, getDocLinkStrength, idf, tfidf
def main():
    name = input("Enter the Name of Personality: ")
    page_link = linkify(name)
    word_list = getWords(page_link)
    link_list = getLinks(page_link)
    tf_dict = tf(word_list)
    doc_links = getDocLinkStrength(link_list, tf_dict)
    links_for_tfidf = [link[0] for link in doc_links[:10]]
    linked_word_lists = [getWords(linkify(link)) for link in links_for_tfidf]
    idf_dict = idf(tf_dict, linked_word_lists)
    tfidf_dict = tfidf(tf_dict, idf_dict)
    tfidf_list = sorted(tfidf_dict.items(), key=lambda x: x[1], reverse=True)
    keywords = [link[0] for link in getDocLinkStrength(link_list, tfidf_dict)]
    final_keyword_list = list(set(keywords))
    for keyword in final_keyword_list:
        print(keyword)
if __name__ == "__main__":
    main()