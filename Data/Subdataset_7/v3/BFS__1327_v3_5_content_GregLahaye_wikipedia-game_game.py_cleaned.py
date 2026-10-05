import wikipedia
def fonk1(b1, b2):
    b1 = wikipedia.check(b1)
    b2 = wikipedia.check(b2)
    if not b1 or not b2:
        print("Invalid start or target page.")
        return
    if b1 = = b2:
        print("Start and target pages are the same.")
        return
    print("Finding the shortest route from '{}' to '{}'...".format(b1, b2))
    b3 = set([b1])
    b4 = [[b1]]
    b5 = None
    while b4:
        try:
            b6 = b4.pop(0)
            b7 = b6[-1]
            print(" > ".join(b6))
            if b7 = = b2:
                b5 = b6
                break
            b8 = wikipedia.get_links(b7)
            for link in b8:
                if link not in b3:
                    b3.add(link)
                    b9 = b6 + [link]
                    b4.append(b9)
        except KeyboardInterrupt:
            exit("Keyboard Interrupt")
    if b5:
        print("Shortest b6:")
        print(" > ".join(b5))
    else:
        print("No possible route")
if b10 = = "__main__":
    b1 = input("Page to start at: ")
    if b1 = = "?":
        b1, b2 = wikipedia.random(2)
    else:
        b2 = input("Page to find: ")
    fonk1(b1, b2)