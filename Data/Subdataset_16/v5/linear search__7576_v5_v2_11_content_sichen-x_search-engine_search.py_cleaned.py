import sys
import webbrowser
from index_search import index_search, create_index
from linear_search import linear_search
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, results
def fonk1():
    if len(sys.argv) != 3:
        fonk4()
        return
    b1 = sys.argv[1]
    b2 = sys.argv[2]
    b3 = filelist(b2)
    b4 = len(b3)
    print(f"Number of b3 found: {b4}")
    b5 = None
    while True:
        b6 = input("Enter search terms: ")
        b7 = words(b6)
        b8 = fonk2(b1, b3, b7, b5)
        if b8 is None:
            break
        b9 = results(b8, b7)
        fonk3(b9)
        webbrowser.open_new_tab("file:
def fonk2(b1, b3, b7, b5):
    if b1 = = 'linear':
        return linear_search(b3, b7)
    elif b1 = = 'b5':
        if b5 is None:
            b5 = create_index(b3)
            print("Index creation complete")
        return index_search(b3, b5, b7)
    elif b1 = = 'myhtable':
        if b5 is None:
            b5 = myhtable_create_index(b3)
            print("Index creation complete")
        return myhtable_index_search(b3, b5, b7)
    else:
        print(f"Invalid search type: {b1}")
        return None
def fonk3(b9):
    with open("/tmp/results.html", "w") as result_file:
        result_file.write(b9)
def fonk4():
    print("Usage:")
    print("$ python search.py linear <b2>")
    print("$ python search.py b5 <b2>")
    print("$ python search.py myhtable <b2>")
if b10 = = "__main__":
    fonk1()