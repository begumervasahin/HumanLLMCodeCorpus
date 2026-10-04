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
def fonk2(b2, b4):
    b1 = None
    if b2 = = 'linear':
        return linear_search, b1
    elif b2 = = 'b1':
        if b1 is None:
            b1 = create_index(b4)
            print("Index complete")
        return lambda f, t: index_search(f, b1, t), b1
    elif b2 = = 'myhtable':
        if b1 is None:
            b1 = myhtable_create_index(b4)
            print("Index complete")
        return lambda f, t: myhtable_index_search(f, b1, t), b1
    else:
        print("Invalid search type:", b2)
        sys.exit(1)
def fonk3():
    if len(sys.argv) != 3:
        fonk1()
        sys.exit(1)
    b2 = sys.argv[1]
    b3 = sys.argv[2]
    b4 = filelist(b3)
    print(f"{len(b4)} b4 found in the directory.")
    search_function, b1 = fonk2(b2, b4)
    while True:
        b5 = input("Search b5: ")
        b6 = words(b5)
        b7 = search_function(b4, b6)
        b8 = results(b7, b6)
        b9 = "/tmp/results.html"
        with open(b9, "w") as results_file:
            results_file.write(b8)
        webbrowser.open_new_tab(f"file:
if b10 = = "__main__":
    fonk3()