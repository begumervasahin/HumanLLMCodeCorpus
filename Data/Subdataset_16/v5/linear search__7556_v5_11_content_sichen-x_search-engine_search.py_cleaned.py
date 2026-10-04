import sys
import webbrowser
from index_search import index_search, create_index
from linear_search import linear_search
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, results
if len(sys.argv) != 3:
    print("Usage:")
    print("$ python search.py linear ~/data/slate")
    print("$ python search.py b5 ~/data/slate")
    print("$ python search.py myhtable ~/data/slate")
    sys.exit(1)
b1 = sys.argv[1]
b2 = sys.argv[2]
b3 = filelist(b2)
b4 = len(b3)
print(f"{b4} b3")
b5 = None
while True:
    b6 = input("Search b7: ")
    b7 = words(b6)
    if b1 = = 'linear':
        b8 = linear_search(b3, b7)
    elif b1 = = 'b5':
        if b5 is None:
            b5 = create_index(b3)
            print("Index complete")
        b8 = index_search(b3, b5, b7)
    elif b1 = = 'myhtable':
        if b5 is None:
            b5 = myhtable_create_index(b3)
            print("Index complete")
        b8 = myhtable_index_search(b3, b5, b7)
    else:
        print("Invalid search type:", b1)
        break
    b9 = results(b8, b7)
    with open("/tmp/results.html", "w") as results_file:
        results_file.write(b9)
    webbrowser.open_new_tab("file: