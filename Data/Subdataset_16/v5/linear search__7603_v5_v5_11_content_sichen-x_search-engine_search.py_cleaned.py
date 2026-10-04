import sys
import webbrowser
from index_search import index_search, create_index
from linear_search import linear_search
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, results
def fonk1():
    if len(sys.argv) != 3:
        fonk2()
        sys.exit(1)
    b6, b1 = sys.argv[1], sys.argv[2]
    b2 = filelist(b1)
    print(f"{len(b2)} b2")
    b3 = None
    while True:
        b4 = input("Search b5: ")
        b5 = words(b4)
        docs, b3 = fonk3(b6, b2, b5, b3)
        if docs is None:
            break
        fonk4(docs, b5)
def fonk2():
    print("Usage:")
    print("$ python search.py linear ~/data/slate")
    print("$ python search.py b3 ~/data/slate")
    print("$ python search.py myhtable ~/data/slate")
def fonk3(b6, b2, b5, b3):
    if b6 = = 'linear':
        return linear_search(b2, b5), b3
    elif b6 = = 'b3':
        if b3 is None:
            b3 = create_index(b2)
            print("Index complete")
        return index_search(b2, b3, b5), b3
    elif b6 = = 'myhtable':
        if b3 is None:
            b3 = myhtable_create_index(b2)
            print("Index complete")
        return myhtable_index_search(b2, b3, b5), b3
    else:
        print("Invalid search type:", b6)
        return None, b3
def fonk4(docs, b5):
    b7 = results(docs, b5)
    b8 = "/tmp/results.html"
    with open(b8, "w") as results_file:
        results_file.write(b7)
    webbrowser.open_new_tab(f"file:
if b9 = = "__main__":
    fonk1()