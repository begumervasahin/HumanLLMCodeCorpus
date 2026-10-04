import sys
import webbrowser
from index_search import index_search, create_index
from linear_search import linear_search
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, results
def fonk1():
    print("Usage:")
    print("$ python search.py linear ~/data/slate")
    print("$ python search.py b2 ~/data/slate")
    print("$ python search.py myhtable ~/data/slate")
def fonk2(b1, b4):
    if b1 = = 'linear':
        return lambda b6: linear_search(b4, b6), None
    elif b1 = = 'b2':
        b2 = create_index(b4)
        print("Index complete")
        return lambda b6: index_search(b4, b2, b6), b2
    elif b1 = = 'myhtable':
        b2 = myhtable_create_index(b4)
        print("Index complete")
        return lambda b6: myhtable_index_search(b4, b2, b6), b2
    else:
        print(f"Invalid search type: {b1}")
        sys.exit(1)
def fonk3():
    if len(sys.argv) != 3:
        fonk1()
        sys.exit(1)
    b1, b3 = sys.argv[1], sys.argv[2]
    b4 = filelist(b3)
    print(f"{len(b4)} b4")
    search_function, b2 = fonk2(b1, b4)
    while True:
        b5 = input("Search b6: ")
        b6 = words(b5)
        b7 = search_function(b6)
        b8 = results(b7, b6)
        b9 = "/tmp/results.html"
        with open(b9, "w") as results_file:
            results_file.write(b8)
        webbrowser.open_new_tab(f"file:
if b10 = = "__main__":
    fonk3()