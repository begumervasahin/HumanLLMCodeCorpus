import wikipediaapi
def get_wikipedia_page_links(page):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(page)
    if not page.exists():
        return None, None
    links = list(page.links.keys())
    return page.title, links
def search(root, target):
    root, root_links = get_wikipedia_page_links(root)
    target, target_links = get_wikipedia_page_links(target)
    if not root or not target:
        print("One or both of the specified pages do not exist.")
        return
    if root == target:
        print("Root and target are the same")
        return
    visited = set([root])
    queue = [[root]]
    found = False
    print(f"Finding the shortest route from '{root}' to '{target}'...")
    while queue and not found:
        try:
            path = queue.pop(0)
            current = path[-1]
            print(" > ".join(path))
            current_title, nodes = get_wikipedia_page_links(current)
            for node in nodes:
                if node not in visited:
                    if node == target:
                        result = path + [node]
                        found = True
                        break
                    visited.add(node)
                    new_path = path + [node]
                    queue.append(new_path)
        except KeyboardInterrupt:
            exit("Keyboard Interrupt")
    if found:
        print("Shortest path: ")
        print(" > ".join(result))
    else:
        print("No possible route")
if __name__ == "__main__":
    start = input("Page to start at: ")
    if start == "?":
        wiki_wiki = wikipediaapi.Wikipedia('en')
        start, end = wiki_wiki.random(2)
    else:
        end = input("Page to find: ")
    search(start, end)