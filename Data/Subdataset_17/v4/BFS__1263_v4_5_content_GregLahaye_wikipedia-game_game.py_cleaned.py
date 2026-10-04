import wikipedia
def search(root, target):
    root = wikipedia.check(root)
    target = wikipedia.check(target)
    if not root or not target:
        print("Invalid root or target page.")
        return
    if root == target:
        print("Root and target are the same.")
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
            nodes = wikipedia.get_links(current)
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
        start, end = wikipedia.random(2)
    else:
        end = input("Page to find: ")
    search(start, end)