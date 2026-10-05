import wikipedia
def search_shortest_path(start_page, target_page):
    start_page = wikipedia.check(start_page)
    target_page = wikipedia.check(target_page)
    if not start_page or not target_page:
        print("Invalid start or target page.")
        return
    if start_page == target_page:
        print("Start and target pages are the same.")
        return
    print("Finding the shortest route from '{}' to '{}'...".format(start_page, target_page))
    visited = set([start_page])
    queue = [[start_page]]
    result = None
    while queue:
        try:
            path = queue.pop(0)
            current = path[-1]
            print(" > ".join(path))
            if current == target_page:
                result = path
                break
            links = wikipedia.get_links(current)
            for link in links:
                if link not in visited:
                    visited.add(link)
                    new_path = path + [link]
                    queue.append(new_path)
        except KeyboardInterrupt:
            exit("Keyboard Interrupt")
    if result:
        print("Shortest path:")
        print(" > ".join(result))
    else:
        print("No possible route")
if __name__ == "__main__":
    start_page = input("Page to start at: ")
    if start_page == "?":
        start_page, target_page = wikipedia.random(2)
    else:
        target_page = input("Page to find: ")
    search_shortest_path(start_page, target_page)