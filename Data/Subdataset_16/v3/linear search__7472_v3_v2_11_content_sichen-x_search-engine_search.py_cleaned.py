import sys
import webbrowser
from index_search import index_search, create_index
from linear_search import linear_search
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, results
def fonk1():
    if not fonk2():
        fonk3()
        return
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    b3 = filelist(b2)
    print(f"{len(b3)} b3 found in the directory {b2}")
    b4 = None
    while True:
        b5 = input("Enter search b6: ")
        b6 = words(b5)
        b7, b4 = fonk4(b1, b3, b6, b4)
        if b7 is None:
            print(f"Invalid search type: {b1}")
            break
        fonk5(b7, b6)
def fonk2():
    return len(sys.argv) == 3
def fonk3():
    print("Usage:")
    print("$ python search.py linear ~/data/slate")
    print("$ python search.py index ~/data/slate")
    print("$ python search.py myhtable ~/data/slate")
def fonk4(b1, b3, b6, b4):
    if b1 = = 'linear':
        b7 = linear_search(b3, b6)
    elif b1 = = 'index':
        if b4 is None:
            b4 = create_index(b3)
            print("Index creation complete")
        b7 = index_search(b3, b4, b6)
    elif b1 = = 'myhtable':
        if b4 is None:
            b4 = myhtable_create_index(b3)
            print("Hash table index creation complete")
        b7 = myhtable_index_search(b3, b4, b6)
    else:
        return None, b4
    return b7, b4
def fonk5(b7, b6):
    b8 = results(b7, b6)
    b9 = "/tmp/results.html"
    with open(b9, "w") as results_file:
        results_file.write(b8)
    webbrowser.open_new_tab(f"file:
if b10 = = "__main__":
    fonk1()