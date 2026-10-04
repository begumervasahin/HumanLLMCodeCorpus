import sys
import webbrowser
from index_search import index_search, create_index
from linear_search import linear_search
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, results
def display_usage():
    print("Usage:")
    print("$ python search.py linear ~/data/slate")
    print("$ python search.py index ~/data/slate")
    print("$ python search.py myhtable ~/data/slate")
    sys.exit(1)
def initialize_index(impl, files):
    if impl == 'index':
        return create_index(files)
    elif impl == 'myhtable':
        return myhtable_create_index(files)
    return None
def perform_search(impl, files, terms, index):
    if impl == 'linear':
        return linear_search(files, terms)
    elif impl == 'index':
        return index_search(files, index, terms)
    elif impl == 'myhtable':
        return myhtable_index_search(files, index, terms)
    else:
        print(f"Invalid search type: {impl}")
        sys.exit(1)
def main():
    if len(sys.argv) != 3:
        display_usage()
    impl = sys.argv[1]
    rootdir = sys.argv[2]
    files = filelist(rootdir)
    print(f"{len(files)} files")
    index = None
    while True:
        try:
            terms = input("Search terms: ")
            if not terms.strip():
                print("Empty search term. Please enter valid search terms.")
                continue
            terms = words(terms)
            if index is None and impl in ['index', 'myhtable']:
                index = initialize_index(impl, files)
                print("Index complete")
            docs = perform_search(impl, files, terms, index)
            page = results(docs, terms)
            with open("/tmp/results.html", "w") as f:
                f.write(page)
            webbrowser.open_new_tab("file:
        except KeyboardInterrupt:
            print("\nSearch terminated by user.")
            break
if __name__ == "__main__":
    main()