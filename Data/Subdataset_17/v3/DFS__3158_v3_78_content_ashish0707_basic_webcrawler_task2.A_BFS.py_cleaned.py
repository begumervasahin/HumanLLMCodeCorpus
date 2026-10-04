from webcrawler import Crawler
from bfs import BFS
def configure_crawler(crawler):
    crawler.add_to_mandatory_list('/wiki/')
    crawler.add_to_disallowed_list(':')
    crawler.set_focused_text('solar')
def main():
    target_url = "https:
    bfs_searcher = BFS()
    crawler = Crawler(target_url, bfs_searcher)
    configure_crawler(crawler)
    crawler.start()
if __name__ == "__main__":
    main()