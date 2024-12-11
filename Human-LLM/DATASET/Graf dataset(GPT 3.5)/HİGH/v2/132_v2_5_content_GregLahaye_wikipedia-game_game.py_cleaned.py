import wikipedia
def fonk1(b1, b2):
    b1 = wikipedia.check(b1)
    b2 = wikipedia.check(b2)
    if b1 and b2:
        if b1 != b2:
            b3 = set([b1])
            b4 = [[b1]]
            b5 = False
            print("Finding the shortest route from '{}' to '{}'...".format(b1, b2))
            while b4 and not b5:
                try:
                    b6 = b4[0]
                    b7 = b6[-1]
                    print(" > ".join(b6))
                    b4 = b4[1:]
                    b8 = wikipedia.get_links(b7)
                    for b9 in b8:
                        if b9 not in b3:
                            if b9 = = b2:
                                b10 = b6 + [b9]
                                b5 = True
                            b3.add(b9)
                            b11 = b6 + [b9]
                            b4.append(b11)
                except KeyboardInterrupt:
                    exit("Keyboard Interrupt")
            if b5:
                print("Shortest b6: ")
                print(" > ".join(b10))
            else:
                print("No possible route")
        else:
            print("Start and target pages are the same")
if b12 = = "__main__":
    b1 = input("Page to start at: ")
    if b1 = = "?":
        b1, b2 = wikipedia.random(2)
    else:
        b2 = input("Page to find: ")
    fonk1(b1, b2)