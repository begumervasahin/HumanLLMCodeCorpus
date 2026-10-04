from Webcrawler import Crawler
from bfs import BFS
def fonk1(url, searcher):
    b1 = Crawler(url, searcher)
    b1.add_to_mandatory_list('/wiki/')
    b1.add_to_disallowed_list(':')
    b1.set_focused_text('solar')
    return b1
def fonk2():
    b2 = "https:
    b3 = BFS()
    b1 = fonk1(b2, b3)
    b1.start()
if b4 = = "__main__":
    fonk2()