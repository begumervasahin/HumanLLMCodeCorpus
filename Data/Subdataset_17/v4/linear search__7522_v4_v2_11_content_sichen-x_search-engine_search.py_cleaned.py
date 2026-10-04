import sys
import webbrowser
from index_search import index_search, create_index
from linear_search import linear_search
from myhtable_search import myhtable_index_search, myhtable_create_index
from words import filelist, words, results
def main():
    if len(sys.argv) != 3:
        print_usage()
        return
    search_type = sys.argv[1]
    root_directory = sys.argv[2]
    files = filelist(root_directory)
    num_files = len(files)
    print(f"Number of files found: {num_files}")
    index = None
    while True:
        search_query = input("Enter search terms: ")
        search_terms = words(search_query)
        if search_type == 'linear':
            matched_docs = linear_search(files, search_terms)
        elif search_type == 'index':
            if index is None:
                index = create_index(files)
                print("Index creation complete")
            matched_docs = index_search(files, index, search_terms)
        elif search_type == 'myhtable':
            if index is None:
                index = myhtable_create_index(files)
                print("Index creation complete")
            matched_docs = myhtable_index_search(files, index, search_terms)
        else:
            print(f"Invalid search type: {search_type}")
            break
        html_page = results(matched_docs, search_terms)
        with open("/tmp/results.html", "w") as result_file:
            result_file.write(html_page)
        webbrowser.open_new_tab("file:
def print_usage():
    print("Usage:")
    print("$ python search.py linear <root_directory>")
    print("$ python search.py index <root_directory>")
    print("$ python search.py myhtable <root_directory>")
if __name__ == "__main__":
    main()