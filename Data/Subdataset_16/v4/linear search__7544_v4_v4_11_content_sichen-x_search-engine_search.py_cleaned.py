import sys
import webbrowser
from index_search import index_search, create_index
from linear_search import linear_search
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, results
def fonk1():
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
        try:
            b6 = input("Search b6: ")
            if not b6.strip():
                print("Empty search term. Please enter valid search b6.")
                continue
            b6 = words(b6)
            if b1 = = 'linear':
                b7 = linear_search(b3, b6)
            elif b1 = = 'b5':
                if b5 is None:
                    b5 = create_index(b3)
                    print("Index complete")
                b7 = index_search(b3, b5, b6)
            elif b1 = = 'myhtable':
                if b5 is None:
                    b5 = myhtable_create_index(b3)
                    print("Index complete")
                b7 = myhtable_index_search(b3, b5, b6)
            else:
                print(f"Invalid search type: {b1}")
                break
            b8 = results(b7, b6)
            with open("/tmp/results.html", "w") as f:
                f.write(b8)
            webbrowser.open_new_tab("file:
        except KeyboardInterrupt:
            print("\nSearch terminated by user.")
            break
if b9 = = "__main__":
    fonk1()