from webcrawler import Crawler
from bfs import BFS
def main():
    url = "https:
    searcher = BFS()
    my_crawler = Crawler(url, searcher)
    my_crawler.add_to_mandatory_list('/wiki/')
    my_crawler.add_to_disallowed_list(':')
    my_crawler.set_focused_text('solar')
    my_crawler.start()
if __name__ == "__main__":
    main()