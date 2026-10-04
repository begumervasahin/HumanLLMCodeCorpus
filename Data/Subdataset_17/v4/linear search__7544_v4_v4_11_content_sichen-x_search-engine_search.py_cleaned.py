import sys
import webbrowser
from index_search import index_search, create_index
from linear_search import linear_search
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, results
def main():
    if len(sys.argv) != 3:
        print("Usage:")
        print("$ python search.py linear ~/data/slate")
        print("$ python search.py index ~/data/slate")
        print("$ python search.py myhtable ~/data/slate")
        sys.exit(1)
    impl = sys.argv[1]
    rootdir = sys.argv[2]
    files = filelist(rootdir)
    N = len(files)
    print(f"{N} files")
    index = None
    while True:
        try:
            terms = input("Search terms: ")
            if not terms.strip():
                print("Empty search term. Please enter valid search terms.")
                continue
            terms = words(terms)
            if impl == 'linear':
                docs = linear_search(files, terms)
            elif impl == 'index':
                if index is None:
                    index = create_index(files)
                    print("Index complete")
                docs = index_search(files, index, terms)
            elif impl == 'myhtable':
                if index is None:
                    index = myhtable_create_index(files)
                    print("Index complete")
                docs = myhtable_index_search(files, index, terms)
            else:
                print(f"Invalid search type: {impl}")
                break
            page = results(docs, terms)
            with open("/tmp/results.html", "w") as f:
                f.write(page)
            webbrowser.open_new_tab("file:
        except KeyboardInterrupt:
            print("\nSearch terminated by user.")
            break
if __name__ == "__main__":
    main()