
class Searcher:
    def __init__(self):
        pass
    def search(self):
        raise NotImplementedError("Subclasses should implement this method.")
from searcher import Searcher
class BFS(Searcher):
    name = '2.A_bfs.txt'
    def merge_list(self, list1, list2):
        return list1 + list2
if __name__ == "__main__":
    bfs = BFS()
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    merged_list = bfs.merge_list(list1, list2)
    print("Merged List:", merged_list)
    print("BFS Name:", bfs.name)