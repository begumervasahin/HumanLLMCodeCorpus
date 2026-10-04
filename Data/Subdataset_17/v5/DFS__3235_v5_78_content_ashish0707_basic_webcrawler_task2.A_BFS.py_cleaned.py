from Webcrawler import Crawler
from bfs import BFS
def setup_crawler(url, searcher):
    crawler = Crawler(url, searcher)
    crawler.add_to_mandatory_list('/wiki/')
    crawler.add_to_disallowed_list(':')
    crawler.set_focused_text('solar')
    return crawler
def main():
    target_url = "https:
    bfs_searcher = BFS()
    crawler = setup_crawler(target_url, bfs_searcher)
    crawler.start()
if __name__ == "__main__":
    main()