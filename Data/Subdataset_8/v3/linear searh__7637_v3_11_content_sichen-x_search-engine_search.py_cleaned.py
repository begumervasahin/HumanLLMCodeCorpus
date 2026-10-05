import sys
import webbrowser
from index_search import index_search, create_index
from linear_search import linear_search
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, results
def print_usage():
    print("Usage:")
    print("$ python search.py linear ~/data/slate")
    print("$ python search.py index ~/data/slate")
    print("$ python search.py myhtable ~/data/slate")
def perform_search(files, impl, terms, index=None):
    if impl == 'linear':
        return linear_search(files, terms)
    elif impl == 'index':
        if index is None:
            index = create_index(files)
            print("Index creation complete")
        return index_search(files, index, terms)
    elif impl == 'myhtable':
        if index is None:
            index = myhtable_create_index(files)
            print("Index creation complete")
        return myhtable_index_search(files, index, terms)
    else:
        print("Invalid search type:", impl)
        return None
def main():
    if len(sys.argv) != 3:
        print_usage()
        return
    impl = sys.argv[1]
    rootdir = sys.argv[2]
    files = filelist(rootdir)
    num_files = len(files)
    print(f"{num_files} files")
    index = None
    while True:
        search_terms = input("Search terms: ")
        terms = words(search_terms)
        docs = perform_search(files, impl, terms, index)
        page = results(docs, terms)
        with open("/tmp/results.html", "w") as f:
            f.write(page)
        webbrowser.open_new_tab("file:
if __name__ == "__main__":
    main()