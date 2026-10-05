import wikipedia
def find_shortest_path(start_page, target_page):
    start_page = wikipedia.check(start_page)
    target_page = wikipedia.check(target_page)
    if start_page and target_page:
        if start_page != target_page:
            visited = set([start_page])
            queue = [[start_page]]
            found = False
            print(f"Finding the shortest route from '{start_page}' to '{target_page}'...")
            while queue and not found:
                try:
                    path = queue[0]
                    current_page = path[-1]
                    print(" > ".join(path))
                    queue = queue[1:]
                    linked_pages = wikipedia.get_links(current_page)
                    for linked_page in linked_pages:
                        if linked_page not in visited:
                            if linked_page == target_page:
                                result = path + [linked_page]
                                found = True
                            visited.add(linked_page)
                            new_path = path + [linked_page]
                            queue.append(new_path)
                except KeyboardInterrupt:
                    exit("Keyboard Interrupt")
            if found:
                print("Shortest path: ")
                print(" > ".join(result))
            else:
                print("No possible route")
        else:
            print("Start page and target page are the same")
if __name__ == "__main__":
    start_page = input("Page to start at: ")
    if start_page == "?":
        start_page, target_page = wikipedia.random(2)
    else:
        target_page = input("Page to find: ")
    find_shortest_path(start_page, target_page)