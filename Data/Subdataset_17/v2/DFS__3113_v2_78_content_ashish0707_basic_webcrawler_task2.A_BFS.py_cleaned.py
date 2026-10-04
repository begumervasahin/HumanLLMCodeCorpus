from webcrawler import Crawler
from bfs import BFS
def main():
    target_url = "https:
    bfs_searcher = BFS()
    crawler = Crawler(target_url, bfs_searcher)
    crawler.add_to_mandatory_list('/wiki/')
    crawler.add_to_disallowed_list(':')
    crawler.set_focused_text('solar')
    crawler.start()
if __name__ == "__main__":
    main()