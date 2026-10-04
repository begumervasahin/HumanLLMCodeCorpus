from Webcrawler import Crawler
from bfs import BFS
b1 = "https:
b2 = BFS()
b3 = Crawler(b1, b2)
b3.addToMandatoryList('/wiki/')
b3.addToDisallowedList(':')
b3.setFocusedText('solar')
b3.start()