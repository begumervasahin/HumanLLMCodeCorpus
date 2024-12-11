import sys
import webbrowser
from index_search import index_search, create_index
from linear_search import linear_search
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, results
def fonk1():
    print("Usage:")
    print("$ python search.py linear ~/data/slate")
    print("$ python search.py b1 ~/data/slate")
    print("$ python search.py myhtable ~/data/slate")
def fonk2(b4, b2, b7, b1 = None):
    if b2 = = 'linear':
        return linear_search(b4, b7)
    elif b2 = = 'b1':
        if b1 is None:
            b1 = create_index(b4)
            print("Index creation complete")
        return index_search(b4, b1, b7)
    elif b2 = = 'myhtable':
        if b1 is None:
            b1 = myhtable_create_index(b4)
            print("Index creation complete")
        return myhtable_index_search(b4, b1, b7)
    else:
        print("Invalid search type:", b2)
        return None
def fonk3():
    if len(sys.argv) != 3:
        fonk1()
        return
    b2 = sys.argv[1]
    b3 = sys.argv[2]
    b4 = filelist(b3)
    b5 = len(b4)
    print(f"{b5} b4")
    b1 = None
    while True:
        b6 = input("Search b7: ")
        b7 = words(b6)
        b8 = fonk2(b4, b2, b7, b1)
        b9 = results(b8, b7)
        with open("/tmp/results.html", "w") as f:
            f.write(b9)
        webbrowser.open_new_tab("file:
if b10 = = "__main__":
    fonk3()