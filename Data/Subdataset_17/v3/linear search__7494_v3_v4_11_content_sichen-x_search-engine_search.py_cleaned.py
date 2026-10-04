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
def get_search_function(impl, files):
    index = None
    if impl == 'linear':
        return linear_search, index
    elif impl == 'index':
        if index is None:
            index = create_index(files)
            print("Index complete")
        return lambda f, t: index_search(f, index, t), index
    elif impl == 'myhtable':
        if index is None:
            index = myhtable_create_index(files)
            print("Index complete")
        return lambda f, t: myhtable_index_search(f, index, t), index
    else:
        print("Invalid search type:", impl)
        sys.exit(1)
def main():
    if len(sys.argv) != 3:
        print_usage()
        sys.exit(1)
    impl = sys.argv[1]
    rootdir = sys.argv[2]
    files = filelist(rootdir)
    print(f"{len(files)} files found in the directory.")
    search_function, index = get_search_function(impl, files)
    while True:
        terms = input("Search terms: ")
        tokenized_terms = words(terms)
        docs = search_function(files, tokenized_terms)
        page_content = results(docs, tokenized_terms)
        results_file_path = "/tmp/results.html"
        with open(results_file_path, "w") as results_file:
            results_file.write(page_content)
        webbrowser.open_new_tab(f"file:
if __name__ == "__main__":
    main()