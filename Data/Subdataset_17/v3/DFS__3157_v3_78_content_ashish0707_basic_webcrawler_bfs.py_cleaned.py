from searcher import Searcher
class BFS(Searcher):
    name = '2.A_bfs.txt'
    def merge_lists(self, list1, list2):
        return list1 + list2
def main():
    bfs_instance = BFS()
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    merged_list = bfs_instance.merge_lists(list1, list2)
    print("Merged List:", merged_list)
    print("BFS Name:", bfs_instance.name)
if __name__ == "__main__":
    main()