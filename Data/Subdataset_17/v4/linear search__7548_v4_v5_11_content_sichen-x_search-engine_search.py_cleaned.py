import sys
import webbrowser
from index_search import index_search, create_index
from linear_search import linear_search
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, results
def main():
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(1)
    impl, rootdir = sys.argv[1], sys.argv[2]
    files = filelist(rootdir)
    num_files = len(files)
    print(f"{num_files} files")
    index = None
    while True:
        search_terms = input("Search terms: ")
        terms = words(search_terms)
        docs = perform_search(impl, files, terms, index)
        if docs is None:
            break
        search_results_page = results(docs, terms)
        with open("/tmp/results.html", "w") as results_file:
            results_file.write(search_results_page)
        webbrowser.open_new_tab("file:
def print_usage():
    print("Usage:")
    print("$ python search.py linear ~/data/slate")
    print("$ python search.py index ~/data/slate")
    print("$ python search.py myhtable ~/data/slate")
def perform_search(impl, files, terms, index):
    if impl == 'linear':
        return linear_search(files, terms)
    elif impl == 'index':
        if index is None:
            index = create_index(files)
            print("Index complete")
        return index_search(files, index, terms)
    elif impl == 'myhtable':
        if index is None:
            index = myhtable_create_index(files)
            print("Index complete")
        return myhtable_index_search(files, index, terms)
    else:
        print("Invalid search type:", impl)
        return None
if __name__ == "__main__":
    main()